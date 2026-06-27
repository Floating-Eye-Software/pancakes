#!/usr/bin/env python3
"""Assemble deterministic, non-authoritative context from named repositories."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import yaml


ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CLASSIFICATIONS = {"public", "private-review-required"}
DIRTY_POLICIES = {"allow", "warn", "error"}


class CompositeError(RuntimeError):
    pass


@dataclass(frozen=True)
class Repo:
    repo_id: str
    root: Path
    authority: str
    revision: str
    commit_epoch: int
    dirty: bool


@dataclass(frozen=True)
class Source:
    repo: Repo
    relpath: str
    path: Path
    classification: str

    @property
    def qualified(self) -> str:
        return f"{self.repo.repo_id}:{self.relpath}"


@dataclass(frozen=True)
class Composite:
    comp_id: str
    out_name: str
    note: str
    sources: tuple[Source, ...]


@dataclass(frozen=True)
class Registry:
    version: int
    plan_path: Path
    outdir: Path
    index_name: str
    upload_file_budget: int
    max_output_bytes: int
    max_total_bytes: int
    dirty_policy: str
    repos: dict[str, Repo]
    composites: tuple[Composite, ...]


def fail(message: str) -> None:
    raise CompositeError(message)


def read_utf8(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing file: {path}")
    except UnicodeDecodeError as exc:
        fail(f"non-UTF-8 file: {path} ({exc})")
    return text.replace("\r\n", "\n").replace("\r", "\n")


def trailing_newline(text: str) -> str:
    return text if text.endswith("\n") else text + "\n"


def run_git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            ["git", "-C", os.fspath(root), *args],
            check=check,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        fail("git is required")
    except subprocess.CalledProcessError as exc:
        detail = exc.stderr.strip() or exc.stdout.strip()
        fail(f"git command failed for {root}: {detail}")


def ensure_mapping(value: Any, context: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        fail(f"{context} must be a mapping")
    return value


def require_string(mapping: dict[str, Any], key: str, context: str) -> str:
    value = mapping.get(key)
    if not isinstance(value, str) or not value.strip():
        fail(f"{context}.{key} must be a non-empty string")
    return value.strip()


def require_positive_int(mapping: dict[str, Any], key: str, context: str) -> int:
    value = mapping.get(key)
    if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
        fail(f"{context}.{key} must be a positive integer")
    return value


def validate_relative(value: str, context: str, *, filename_only: bool = False) -> str:
    normalized = value.replace("\\", "/").strip()
    while normalized.startswith("./"):
        normalized = normalized[2:]
    path = Path(normalized)
    if not normalized or path.is_absolute() or ".." in path.parts:
        fail(f"{context} must be a contained relative path: {value}")
    if filename_only and len(path.parts) != 1:
        fail(f"{context} must be a filename: {value}")
    return normalized


def contained(path: Path, parent: Path, context: str) -> Path:
    resolved = path.resolve()
    try:
        resolved.relative_to(parent.resolve())
    except ValueError:
        fail(f"{context} escapes {parent}: {resolved}")
    return resolved


def parse_root_overrides(values: Iterable[str]) -> dict[str, Path]:
    overrides: dict[str, Path] = {}
    for raw in values:
        if "=" not in raw:
            fail(f"--repo-root must use ID=PATH: {raw}")
        repo_id, path = raw.split("=", 1)
        repo_id = repo_id.strip()
        if not repo_id or not path.strip():
            fail(f"--repo-root must use ID=PATH: {raw}")
        if repo_id in overrides:
            fail(f"duplicate --repo-root override: {repo_id}")
        overrides[repo_id] = Path(path).expanduser()
    return overrides


def load_yaml(plan_path: Path) -> dict[str, Any]:
    try:
        raw = yaml.safe_load(read_utf8(plan_path))
    except yaml.YAMLError as exc:
        fail(f"invalid YAML in {plan_path}: {exc}")
    return ensure_mapping(raw, "registry")


def inspect_repo(repo_id: str, root: Path, authority: str) -> Repo:
    root = root.resolve()
    if not root.is_dir():
        fail(f"repository {repo_id} is missing: {root}")
    top = Path(run_git(root, "rev-parse", "--show-toplevel").stdout.strip()).resolve()
    if top != root:
        fail(f"repository root for {repo_id} is not a Git top level: {root}")
    revision = run_git(root, "rev-parse", "--verify", "HEAD").stdout.strip()
    epoch_text = run_git(root, "show", "-s", "--format=%ct", "HEAD").stdout.strip()
    try:
        epoch = int(epoch_text)
    except ValueError:
        fail(f"invalid Git commit timestamp for {repo_id}: {epoch_text}")
    dirty = bool(run_git(root, "status", "--porcelain", "--untracked-files=no").stdout.strip())
    return Repo(repo_id, root, authority, revision, epoch, dirty)


def validate_tracked(source: Source) -> None:
    result = run_git(
        source.repo.root,
        "ls-files",
        "--error-unmatch",
        "--",
        source.relpath,
        check=False,
    )
    if result.returncode != 0:
        fail(f"source must be a tracked file: {source.qualified}")


def load_registry(
    control_root: Path,
    plan_arg: str,
    root_overrides: dict[str, Path] | None = None,
) -> Registry:
    control_root = control_root.resolve()
    if not control_root.is_dir():
        fail(f"control root is missing: {control_root}")
    plan_path = Path(plan_arg)
    if not plan_path.is_absolute():
        plan_path = control_root / plan_path
    plan_path = contained(plan_path, control_root, "plan")
    raw = load_yaml(plan_path)

    version = raw.get("version")
    if not isinstance(version, int) or isinstance(version, bool):
        fail("registry.version must be an integer")
    outdir_rel = validate_relative(require_string(raw, "outdir", "registry"), "registry.outdir")
    outdir = contained(control_root / outdir_rel, control_root, "registry.outdir")
    index_name = validate_relative(
        require_string(raw, "index", "registry"), "registry.index", filename_only=True
    )
    upload_budget = require_positive_int(raw, "upload_file_budget", "registry")
    max_output = require_positive_int(raw, "max_output_bytes", "registry")
    max_total = require_positive_int(raw, "max_total_bytes", "registry")
    dirty_policy = require_string(raw, "dirty_policy", "registry")
    if dirty_policy not in DIRTY_POLICIES:
        fail(f"registry.dirty_policy must be one of {sorted(DIRTY_POLICIES)}")

    repo_defs = ensure_mapping(raw.get("repositories"), "registry.repositories")
    if not repo_defs:
        fail("registry.repositories must not be empty")
    root_overrides = root_overrides or {}
    unknown_overrides = set(root_overrides) - set(repo_defs)
    if unknown_overrides:
        fail(f"unknown repository root override: {sorted(unknown_overrides)[0]}")

    repos: dict[str, Repo] = {}
    for repo_id, value in repo_defs.items():
        if not isinstance(repo_id, str) or not ID_RE.fullmatch(repo_id):
            fail(f"invalid repository ID: {repo_id}")
        definition = ensure_mapping(value, f"repositories.{repo_id}")
        authority = require_string(definition, "authority", f"repositories.{repo_id}")
        default_root = require_string(definition, "default_root", f"repositories.{repo_id}")
        root = root_overrides.get(repo_id)
        if root is None:
            root = control_root / default_root
        repos[repo_id] = inspect_repo(repo_id, root, authority)

    comp_defs = raw.get("composites")
    if not isinstance(comp_defs, list) or not comp_defs:
        fail("registry.composites must be a non-empty list")

    seen_ids: set[str] = set()
    seen_outputs: set[str] = {index_name}
    all_source_paths: set[Path] = set()
    composites: list[Composite] = []
    for comp_index, value in enumerate(comp_defs):
        context = f"composites[{comp_index}]"
        definition = ensure_mapping(value, context)
        comp_id = require_string(definition, "id", context)
        if not ID_RE.fullmatch(comp_id):
            fail(f"{context}.id must be kebab-case: {comp_id}")
        if comp_id in seen_ids:
            fail(f"duplicate composite ID: {comp_id}")
        seen_ids.add(comp_id)
        out_name = validate_relative(
            require_string(definition, "out", context), f"{context}.out", filename_only=True
        )
        if out_name in seen_outputs:
            fail(f"duplicate output name: {out_name}")
        seen_outputs.add(out_name)
        note = require_string(definition, "note", context)
        source_defs = definition.get("sources")
        if not isinstance(source_defs, list) or not source_defs:
            fail(f"{context}.sources must be a non-empty list")
        sources: list[Source] = []
        seen_sources: set[str] = set()
        for source_index, source_value in enumerate(source_defs):
            source_context = f"{context}.sources[{source_index}]"
            source_def = ensure_mapping(source_value, source_context)
            repo_id = require_string(source_def, "repo", source_context)
            if repo_id not in repos:
                fail(f"{source_context}.repo is unknown: {repo_id}")
            relpath = validate_relative(
                require_string(source_def, "path", source_context),
                f"{source_context}.path",
            )
            qualified = f"{repo_id}:{relpath}"
            if qualified in seen_sources:
                fail(f"duplicate source in {comp_id}: {qualified}")
            seen_sources.add(qualified)
            classification = require_string(source_def, "classification", source_context)
            if classification not in CLASSIFICATIONS:
                fail(
                    f"{source_context}.classification must be one of "
                    f"{sorted(CLASSIFICATIONS)}"
                )
            if source_def.get("reviewed") is not True:
                fail(f"{source_context} must have reviewed: true")
            repo = repos[repo_id]
            path = contained(repo.root / relpath, repo.root, qualified)
            if not path.exists():
                fail(f"missing source: {qualified}")
            if not path.is_file():
                fail(f"source is not a regular file: {qualified}")
            source = Source(repo, relpath, path, classification)
            validate_tracked(source)
            read_utf8(path)
            sources.append(source)
            all_source_paths.add(path)
        composites.append(Composite(comp_id, out_name, note, tuple(sources)))

    output_count = 1 + len(composites)
    if output_count > upload_budget:
        fail(f"upload set has {output_count} files; budget is {upload_budget}")
    for out_name in seen_outputs:
        out_path = contained(outdir / out_name, outdir, f"output {out_name}")
        if out_path in all_source_paths:
            fail(f"output collides with a source file: {out_path}")

    dirty_repos = [repo.repo_id for repo in repos.values() if repo.dirty]
    if dirty_repos and dirty_policy == "error":
        fail(f"dirty repositories are not allowed: {', '.join(dirty_repos)}")
    return Registry(
        version,
        plan_path,
        outdir,
        index_name,
        upload_budget,
        max_output,
        max_total,
        dirty_policy,
        repos,
        tuple(composites),
    )


def snapshot_at(registry: Registry) -> str:
    epoch = max(repo.commit_epoch for repo in registry.repos.values())
    return datetime.fromtimestamp(epoch, tz=timezone.utc).isoformat().replace("+00:00", "Z")


def render_composite(registry: Registry, composite: Composite) -> str:
    repo_ids = list(dict.fromkeys(source.repo.repo_id for source in composite.sources))
    lines = [
        "---",
        "context_composite:",
        f"  schema_version: {registry.version}",
        f"  id: {composite.comp_id}",
        f"  output: {composite.out_name}",
        "  authority: none",
        f"  snapshot_at: {snapshot_at(registry)}",
        "  repositories:",
    ]
    for repo_id in repo_ids:
        repo = registry.repos[repo_id]
        lines.extend(
            [
                f"    {repo_id}:",
                f"      revision: {repo.revision}",
                f"      dirty: {str(repo.dirty).lower()}",
            ]
        )
    lines.extend(["  sources:"])
    for source in composite.sources:
        lines.extend(
            [
                f"    - path: {source.qualified}",
                f"      classification: {source.classification}",
            ]
        )
    lines.extend(
        [
            "---",
            "",
            "# Generated Context Composite",
            "",
            composite.note,
            "",
            "This file is a mechanical, non-authoritative aggregation for external",
            "context packaging. It does not transfer ownership or modify any source.",
            "Each source remains authoritative in its named repository. If this",
            "snapshot differs from a source, the source prevails.",
            "",
            "## Included Sources",
            "",
        ]
    )
    for number, source in enumerate(composite.sources, 1):
        lines.append(f"{number}. `{source.qualified}` ({source.classification})")
    lines.append("")
    parts = ["\n".join(lines) + "\n"]
    for source in composite.sources:
        marker = "=" * 72
        parts.append(
            f"{marker}\nBEGIN SOURCE: {source.qualified}\n{marker}\n\n"
            + trailing_newline(read_utf8(source.path))
            + f"\n{marker}\nEND SOURCE: {source.qualified}\n{marker}\n\n"
        )
    return trailing_newline("".join(parts))


def review_required(composite: Composite) -> bool:
    return any(source.classification == "private-review-required" for source in composite.sources)


def render_index(registry: Registry, rendered: dict[str, str]) -> str:
    total_composite_bytes = sum(len(text.encode("utf-8")) for text in rendered.values())
    dirty = [repo.repo_id for repo in registry.repos.values() if repo.dirty]
    lines = [
        "# Context Snapshot Index",
        "",
        "This index and the listed composites form one non-authoritative upload",
        "snapshot. Replace them together; source repositories remain authoritative.",
        "",
        f"- Registry schema: `{registry.version}`",
        f"- Snapshot timestamp: `{snapshot_at(registry)}`",
        f"- Upload files: `{1 + len(registry.composites)}` / `{registry.upload_file_budget}`",
        f"- Composite bytes: `{total_composite_bytes}`",
        f"- Dirty repositories: `{', '.join(dirty) if dirty else 'none'}`",
        "",
        "## Repository Provenance",
        "",
        "| Repository | Revision | Dirty | Authority |",
        "| --- | --- | --- | --- |",
    ]
    for repo in registry.repos.values():
        authority = repo.authority.replace("|", "\\|")
        lines.append(
            f"| {repo.repo_id} | `{repo.revision}` | "
            f"{str(repo.dirty).lower()} | {authority} |"
        )
    lines.extend(
        [
            "",
            "## Upload Order",
            "",
            "1. `context-index.md`",
        ]
    )
    for number, composite in enumerate(registry.composites, 2):
        size = len(rendered[composite.out_name].encode("utf-8"))
        review = "required" if review_required(composite) else "standard"
        lines.append(
            f"{number}. `{composite.out_name}` — {len(composite.sources)} sources, "
            f"{size} bytes, pre-upload review: {review}"
        )
    lines.extend(
        [
            "",
            "## Upload Gate",
            "",
            "Before upload, inspect every generated file for credentials, secrets,",
            "private user data, raw private records, and inappropriate health-related",
            "disclosure. Dirty repositories and every `private-review-required` source",
            "require deliberate review. Do not upload a partial snapshot.",
            "",
        ]
    )
    return "\n".join(lines)


def build_outputs(registry: Registry) -> dict[str, str]:
    rendered: dict[str, str] = {}
    for composite in registry.composites:
        text = render_composite(registry, composite)
        size = len(text.encode("utf-8"))
        if size > registry.max_output_bytes:
            fail(
                f"{composite.out_name} is {size} bytes; "
                f"maximum is {registry.max_output_bytes}"
            )
        rendered[composite.out_name] = text
    index_text = render_index(registry, rendered)
    index_size = len(index_text.encode("utf-8"))
    if index_size > registry.max_output_bytes:
        fail(
            f"{registry.index_name} is {index_size} bytes; "
            f"maximum is {registry.max_output_bytes}"
        )
    outputs = {registry.index_name: index_text, **rendered}
    total = sum(len(text.encode("utf-8")) for text in outputs.values())
    if total > registry.max_total_bytes:
        fail(f"upload set is {total} bytes; maximum is {registry.max_total_bytes}")
    return outputs


def unknown_outputs(registry: Registry) -> list[Path]:
    if not registry.outdir.exists():
        return []
    declared = {registry.index_name, *(comp.out_name for comp in registry.composites)}
    return sorted(
        path for path in registry.outdir.glob("*.md") if path.name not in declared
    )


def write_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(f".{path.name}.tmp")
    temp.write_text(text, encoding="utf-8", newline="\n")
    temp.replace(path)


def generate(registry: Registry, *, check: bool) -> None:
    outputs = build_outputs(registry)
    unknown = unknown_outputs(registry)
    if unknown:
        for path in unknown:
            print(f"unknown generated Markdown file: {path}", file=sys.stderr)
        if check:
            fail(f"{len(unknown)} unknown generated Markdown file(s)")
    if registry.dirty_policy == "warn":
        for repo in registry.repos.values():
            if repo.dirty:
                print(f"warning: repository is dirty: {repo.repo_id}", file=sys.stderr)
    stale: list[str] = []
    if check:
        for name, expected in outputs.items():
            path = registry.outdir / name
            if not path.is_file() or trailing_newline(read_utf8(path)) != expected:
                stale.append(name)
        if stale:
            fail(f"{len(stale)} generated file(s) are stale: {', '.join(stale)}")
        print(f"composites are current ({len(outputs)} files)")
        return
    for name, text in outputs.items():
        write_atomic(registry.outdir / name, text)
        print(f"wrote {registry.outdir / name}")


def clean(registry: Registry) -> None:
    names = [registry.index_name, *(comp.out_name for comp in registry.composites)]
    removed = 0
    for name in names:
        path = registry.outdir / name
        if path.exists():
            path.unlink()
            removed += 1
            print(f"removed {path}")
    for path in unknown_outputs(registry):
        print(f"left unknown generated Markdown file: {path}", file=sys.stderr)
    print(f"removed {removed} declared file(s)")


def list_registry(registry: Registry) -> None:
    print(f"output directory: {registry.outdir}")
    print(
        f"upload files: {1 + len(registry.composites)} / "
        f"{registry.upload_file_budget}"
    )
    print(f"index -> {registry.index_name}")
    for composite in registry.composites:
        print(f"{composite.comp_id} -> {composite.out_name}")
        for source in composite.sources:
            print(f"  - {source.qualified} [{source.classification}]")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--control-root", default=".")
    parser.add_argument("--plan", default="_work/context/composites.yml")
    parser.add_argument(
        "--repo-root",
        action="append",
        default=[],
        metavar="ID=PATH",
        help="override a named repository root; may be repeated",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--list", action="store_true")
    mode.add_argument("--clean", action="store_true")
    args = parser.parse_args(argv)
    try:
        overrides = parse_root_overrides(args.repo_root)
        registry = load_registry(Path(args.control_root), args.plan, overrides)
        if args.list:
            list_registry(registry)
        elif args.clean:
            clean(registry)
        else:
            generate(registry, check=args.check)
    except CompositeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
