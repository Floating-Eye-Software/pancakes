from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from copy import deepcopy
from io import StringIO
from pathlib import Path

import yaml


SCRIPT = Path(__file__).parents[1] / "scripts" / "assemble_context_composites.py"
SPEC = importlib.util.spec_from_file_location("context_composites", SCRIPT)
assert SPEC and SPEC.loader
cc = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = cc
SPEC.loader.exec_module(cc)


def git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


class ContextCompositeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        git(self.root, "init", "-q")
        git(self.root, "config", "user.email", "tests@example.invalid")
        git(self.root, "config", "user.name", "Composite Tests")
        (self.root / "docs").mkdir()
        (self.root / "docs" / "a.md").write_text("# A\n\nAlpha.\n", encoding="utf-8")
        (self.root / "docs" / "b.md").write_text("# B\n\nBeta.\n", encoding="utf-8")
        git(self.root, "add", "docs")
        git(self.root, "commit", "-q", "-m", "fixtures")
        self.plan = self.root / "plan.yml"
        self.data = {
            "version": 1,
            "outdir": "generated",
            "index": "context-index.md",
            "upload_file_budget": 3,
            "max_output_bytes": 100000,
            "max_total_bytes": 200000,
            "dirty_policy": "warn",
            "repositories": {
                "control": {
                    "default_root": ".",
                    "authority": "test authority",
                }
            },
            "composites": [
                {
                    "id": "test",
                    "out": "test-context.md",
                    "note": "test context",
                    "sources": [
                        {
                            "repo": "control",
                            "path": "docs/a.md",
                            "classification": "public",
                            "reviewed": True,
                        },
                        {
                            "repo": "control",
                            "path": "docs/b.md",
                            "classification": "public",
                            "reviewed": True,
                        },
                    ],
                }
            ],
        }
        self.write_plan()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_plan(self) -> None:
        self.plan.write_text(yaml.safe_dump(self.data, sort_keys=False), encoding="utf-8")

    def load(self) -> cc.Registry:
        return cc.load_registry(self.root, "plan.yml")

    def assert_load_error(self, text: str) -> None:
        with self.assertRaisesRegex(cc.CompositeError, text):
            self.load()

    def test_generation_is_deterministic_and_contains_provenance(self) -> None:
        registry = self.load()
        cc.generate(registry, check=False)
        first = {
            path.name: path.read_bytes() for path in registry.outdir.glob("*.md")
        }
        cc.generate(registry, check=True)
        cc.generate(registry, check=False)
        second = {
            path.name: path.read_bytes() for path in registry.outdir.glob("*.md")
        }
        self.assertEqual(first, second)
        composite = first["test-context.md"].decode()
        self.assertIn("control:docs/a.md", composite)
        self.assertIn("BEGIN SOURCE: control:docs/a.md", composite)
        self.assertIn(git(self.root, "rev-parse", "HEAD"), composite)
        self.assertIn("authority: none", composite)

    def test_check_detects_changed_source_and_dirty_state_is_recorded(self) -> None:
        registry = self.load()
        cc.generate(registry, check=False)
        (self.root / "docs" / "a.md").write_text("# A\n\nChanged.\n", encoding="utf-8")
        dirty_registry = self.load()
        self.assertTrue(dirty_registry.repos["control"].dirty)
        with self.assertRaisesRegex(cc.CompositeError, "stale"):
            cc.generate(dirty_registry, check=True)
        cc.generate(dirty_registry, check=False)
        text = (dirty_registry.outdir / "test-context.md").read_text()
        self.assertIn("dirty: true", text)

    def test_missing_repository_fails(self) -> None:
        self.data["repositories"]["control"]["default_root"] = "missing"
        self.write_plan()
        self.assert_load_error("repository control is missing")

    def test_missing_source_fails(self) -> None:
        self.data["composites"][0]["sources"][0]["path"] = "docs/missing.md"
        self.write_plan()
        self.assert_load_error("missing source")

    def test_planned_source_is_manifested_then_included_when_tracked(self) -> None:
        planned = {
            "repo": "control",
            "path": "docs/planned.md",
            "classification": "public",
            "reviewed": True,
            "required": False,
        }
        self.data["composites"][0]["sources"].append(planned)
        self.write_plan()
        registry = self.load()
        source = registry.composites[0].sources[-1]
        self.assertFalse(source.available)
        output = cc.render_composite(registry, registry.composites[0])
        self.assertIn("planned; source not yet present", output)
        self.assertNotIn("BEGIN SOURCE: control:docs/planned.md", output)

        (self.root / "docs" / "planned.md").write_text(
            "# Planned\n\nNow available.\n", encoding="utf-8"
        )
        git(self.root, "add", "docs/planned.md")
        git(self.root, "commit", "-q", "-m", "planned source")
        registry = self.load()
        source = registry.composites[0].sources[-1]
        self.assertTrue(source.available)
        output = cc.render_composite(registry, registry.composites[0])
        self.assertIn("BEGIN SOURCE: control:docs/planned.md", output)
        self.assertIn("Now available.", output)

    def test_required_flag_must_be_boolean(self) -> None:
        self.data["composites"][0]["sources"][0]["required"] = "no"
        self.write_plan()
        self.assert_load_error("required must be a boolean")

    def test_unknown_repository_fails(self) -> None:
        self.data["composites"][0]["sources"][0]["repo"] = "unknown"
        self.write_plan()
        self.assert_load_error("repo is unknown")

    def test_absolute_and_parent_paths_fail(self) -> None:
        for path in ("/etc/passwd", "../outside.md"):
            with self.subTest(path=path):
                self.data["composites"][0]["sources"][0]["path"] = path
                self.write_plan()
                self.assert_load_error("contained relative path")

    def test_symlink_escape_fails(self) -> None:
        outside = self.root.parent / f"{self.root.name}-outside.md"
        outside.write_text("outside\n", encoding="utf-8")
        try:
            (self.root / "docs" / "escape.md").symlink_to(outside)
            git(self.root, "add", "docs/escape.md")
            git(self.root, "commit", "-q", "-m", "symlink")
            self.data["composites"][0]["sources"][0]["path"] = "docs/escape.md"
            self.write_plan()
            self.assert_load_error("escapes")
        finally:
            outside.unlink(missing_ok=True)

    def test_duplicate_source_and_output_fail(self) -> None:
        self.data["composites"][0]["sources"].append(
            deepcopy(self.data["composites"][0]["sources"][0])
        )
        self.write_plan()
        self.assert_load_error("duplicate source")
        self.data["composites"][0]["sources"].pop()
        other = deepcopy(self.data["composites"][0])
        other["id"] = "other"
        self.data["composites"].append(other)
        self.write_plan()
        self.assert_load_error("duplicate output")

    def test_invalid_utf8_fails(self) -> None:
        (self.root / "docs" / "a.md").write_bytes(b"\xff\xfe")
        git(self.root, "add", "docs/a.md")
        git(self.root, "commit", "-q", "-m", "invalid utf8")
        self.assert_load_error("non-UTF-8")

    def test_untracked_source_fails(self) -> None:
        (self.root / "docs" / "new.md").write_text("new\n", encoding="utf-8")
        self.data["composites"][0]["sources"][0]["path"] = "docs/new.md"
        self.write_plan()
        self.assert_load_error("tracked file")

    def test_dirty_policy_error_fails(self) -> None:
        self.data["dirty_policy"] = "error"
        self.write_plan()
        (self.root / "docs" / "a.md").write_text("dirty\n", encoding="utf-8")
        self.assert_load_error("dirty repositories are not allowed")

    def test_unknown_output_fails_check_and_survives_clean(self) -> None:
        registry = self.load()
        cc.generate(registry, check=False)
        unknown = registry.outdir / "notes.md"
        unknown.write_text("keep\n", encoding="utf-8")
        with self.assertRaisesRegex(cc.CompositeError, "unknown"):
            cc.generate(registry, check=True)
        cc.clean(registry)
        self.assertTrue(unknown.exists())
        self.assertFalse((registry.outdir / "test-context.md").exists())

    def test_upload_budget_and_size_limits_fail(self) -> None:
        self.data["upload_file_budget"] = 1
        self.write_plan()
        self.assert_load_error("budget")
        self.data["upload_file_budget"] = 3
        self.data["max_output_bytes"] = 10
        self.write_plan()
        with self.assertRaisesRegex(cc.CompositeError, "maximum"):
            cc.build_outputs(self.load())

    def test_total_size_limit_fails(self) -> None:
        self.data["max_total_bytes"] = 10
        self.write_plan()
        with self.assertRaisesRegex(cc.CompositeError, "upload set"):
            cc.build_outputs(self.load())

    def test_output_source_collision_fails(self) -> None:
        self.data["outdir"] = "docs"
        self.data["composites"][0]["out"] = "a.md"
        self.write_plan()
        self.assert_load_error("collides")

    def test_override_validation(self) -> None:
        with self.assertRaisesRegex(cc.CompositeError, "unknown repository root override"):
            cc.load_registry(self.root, "plan.yml", {"other": self.root})
        with self.assertRaisesRegex(cc.CompositeError, "duplicate"):
            cc.parse_root_overrides(["control=.", "control=elsewhere"])

    def test_main_reports_errors_without_traceback(self) -> None:
        self.data["upload_file_budget"] = 1
        self.write_plan()
        stderr = StringIO()
        with redirect_stderr(stderr), redirect_stdout(StringIO()):
            result = cc.main(
                ["--control-root", str(self.root), "--plan", "plan.yml", "--check"]
            )
        self.assertEqual(2, result)
        self.assertIn("error:", stderr.getvalue())
        self.assertNotIn("Traceback", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
