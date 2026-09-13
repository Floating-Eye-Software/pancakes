#!/usr/bin/env python3
"""Download Wikimedia images referenced by Pancakes Corner in small batches."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CORNER_ROOT = REPO_ROOT / "docs" / "pancakes-corner"
IMAGES_ROOT = CORNER_ROOT / "images"
ACTIVITY_LOG = REPO_ROOT / "_work" / "pancakes-corner-image-activity.md"
DEFAULT_MAX_DOWNLOADS = 3
DEFAULT_SLEEP = 15.0
DEFAULT_WIDTH = 1200
USER_AGENT = os.environ.get(
    "WIKIMEDIA_USER_AGENT",
    "pancakes-corner-images/1.0 (https://github.com/Floating-Eye-Software/pancakes)",
)

IMAGE_LINK = re.compile(
    r"\[!\[(?P<alt>[^]]*)\]\((?P<display>[^)]+)\)\]"
    r"\((?P<page>https://commons\.wikimedia\.org/wiki/File:[^)]+)\)"
)

# Stable, readable names for the initial Pancakes Corner image set.
LOCAL_FILENAME_OVERRIDES = {
    "Dosa-chutney-sambhar.jpg": "dosa-chutney-sambhar.jpg",
    "Injera_with_eight_kinds_of_stew.jpg": "injera-eight-stews.jpg",
    "Blini-Demidoff.jpg": "blini-demidoff.jpg",
    "Strawberry_crepes_with_zabaglione.jpg": "strawberry-crepes-zabaglione.jpg",
    "البغرير_المغربي.jpg": "baghrir-moroccan.jpg",
    "Okonomiyaki_006.jpg": "okonomiyaki.jpg",
    "Korean_pancake-Various_jeon-01.jpg": "korean-jeon.jpg",
    "Scallion_pancakes.jpg": "scallion-pancakes.jpg",
    "Colombian_Food,_Arepas.jpg": "colombian-arepas.jpg",
    "Johnnycakes.jpg": "johnnycakes.jpg",
    "Poffertjes_001.jpg": "poffertjes.jpg",
    "Pannkakor_m_sylt_o_grädde_1457.jpg": "swedish-pancakes.jpg",
    "Naleśniki.jpg": "nalesniki.jpg",
    "Banh-xeo,-roving-street-vendor,-Quy-Nhon,-Vietnam.jpg": "banh-xeo.jpg",
    "Egg_hopper.jpg": "egg-hopper.jpg",
    "Isparta_museum_preparing_gözleme_4976.jpg": "gozleme-preparation.jpg",
    "Raggmunk_med_fläsk_och_lingonsylt.jpg": "raggmunk.jpg",
    "Pancakes_with_syrup.jpg": "pancakes-with-syrup.jpg",
    "Casabe.jpg": "casabe.jpg",
    "Making_bread_in_Stone_Age.jpg": "stone-age-bread.jpg",
    "Dosa-Preparation.jpg": "dosa-preparation.jpg",
    "Sourdough_starter.jpg": "sourdough-starter.jpg",
    "Saddle_quern.jpg": "saddle-quern.jpg",
}


@dataclass(frozen=True)
class ImageReference:
    document: Path
    alt: str
    display: str
    commons_page: str
    commons_file: str
    local_file: Path

    @property
    def download_url(self) -> str:
        encoded = urllib.parse.quote(self.commons_file, safe="")
        return (
            "https://commons.wikimedia.org/wiki/Special:Redirect/file/"
            f"{encoded}?width={DEFAULT_WIDTH}"
        )

    @property
    def local_link(self) -> str:
        return os.path.relpath(self.local_file, self.document.parent).replace(
            os.sep, "/"
        )


def commons_filename(page_url: str) -> str:
    marker = "/wiki/File:"
    if marker not in page_url:
        raise ValueError(f"not a Commons file page: {page_url}")
    return urllib.parse.unquote(page_url.split(marker, 1)[1]).replace(" ", "_")


def generic_local_filename(commons_file: str) -> str:
    source = Path(commons_file)
    stem = unicodedata.normalize("NFKD", source.stem)
    stem = stem.encode("ascii", "ignore").decode("ascii")
    stem = re.sub(r"[^a-zA-Z0-9]+", "-", stem).strip("-").lower()
    if not stem:
        stem = "commons-" + hashlib.sha256(commons_file.encode()).hexdigest()[:12]
    suffix = source.suffix.lower()
    if suffix not in {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"}:
        suffix = ".jpg"
    return stem + suffix


def local_filename(commons_file: str) -> str:
    return LOCAL_FILENAME_OVERRIDES.get(
        commons_file, generic_local_filename(commons_file)
    )


def read_preserving_newlines(path: Path) -> str:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return handle.read()


def write_preserving_newlines(path: Path, text: str) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def discover_references(corner_root: Path = CORNER_ROOT) -> list[ImageReference]:
    references: list[ImageReference] = []
    for document in sorted(corner_root.rglob("*.md")):
        if IMAGES_ROOT in document.parents:
            continue
        text = read_preserving_newlines(document)
        for match in IMAGE_LINK.finditer(text):
            page = match.group("page")
            source_name = commons_filename(page)
            references.append(
                ImageReference(
                    document=document,
                    alt=match.group("alt"),
                    display=match.group("display"),
                    commons_page=page,
                    commons_file=source_name,
                    local_file=IMAGES_ROOT / local_filename(source_name),
                )
            )
    return references


def unique_references(references: list[ImageReference]) -> list[ImageReference]:
    unique: dict[Path, ImageReference] = {}
    for reference in references:
        existing = unique.get(reference.local_file)
        if existing and existing.commons_file != reference.commons_file:
            raise ValueError(
                f"local filename collision: {reference.local_file.name} maps to "
                f"both {existing.commons_file} and {reference.commons_file}"
            )
        unique.setdefault(reference.local_file, reference)
    return list(unique.values())


def append_activity(event: str, reference: ImageReference, detail: str = "") -> None:
    timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    clean_detail = detail.replace("|", "\\|").replace("\n", " ")
    row = (
        f"| {timestamp} | {event} | `{reference.local_file.relative_to(REPO_ROOT)}` "
        f"| {clean_detail} |\n"
    )
    with ACTIVITY_LOG.open("a", encoding="utf-8") as handle:
        handle.write(row)


def valid_image(data: bytes) -> bool:
    stripped = data.lstrip()
    return any(
        (
            data.startswith(b"\xff\xd8\xff"),
            data.startswith(b"\x89PNG\r\n\x1a\n"),
            data.startswith((b"GIF87a", b"GIF89a")),
            data.startswith(b"RIFF") and data[8:12] == b"WEBP",
            stripped.startswith(b"<svg"),
            stripped.startswith(b"<?xml") and b"<svg" in stripped[:500],
        )
    )


def download(reference: ImageReference) -> tuple[str, str]:
    request = urllib.request.Request(
        reference.download_url,
        headers={"User-Agent": USER_AGENT},
    )
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            data = response.read()
    except urllib.error.HTTPError as exc:
        if exc.code == 429:
            retry_after = exc.headers.get("Retry-After", "not provided")
            return "throttled", f"HTTP 429; Retry-After={retry_after}"
        return "failed", f"HTTP {exc.code}"
    except urllib.error.URLError as exc:
        return "failed", str(exc.reason)

    if not valid_image(data):
        return "failed", f"response was not a recognized image ({len(data)} bytes)"

    reference.local_file.parent.mkdir(parents=True, exist_ok=True)
    partial = reference.local_file.with_suffix(reference.local_file.suffix + ".part")
    partial.write_bytes(data)
    partial.replace(reference.local_file)
    return "done", f"{len(data)} bytes"


def sync_local_links(references: list[ImageReference]) -> int:
    by_document: dict[Path, list[ImageReference]] = {}
    for reference in references:
        if reference.local_file.exists() and reference.display != reference.local_link:
            by_document.setdefault(reference.document, []).append(reference)

    changes = 0
    for document, document_references in by_document.items():
        text = read_preserving_newlines(document)
        updated = text
        for reference in document_references:
            old = f"]({reference.display})]({reference.commons_page})"
            new = f"]({reference.local_link})]({reference.commons_page})"
            updated = updated.replace(old, new)
        if updated != text:
            write_preserving_newlines(document, updated)
            changes += 1
    return changes


def print_status(references: list[ImageReference]) -> tuple[int, int]:
    unique = unique_references(references)
    complete = sum(reference.local_file.exists() for reference in unique)
    missing = len(unique) - complete
    print(f"Pancakes Corner Commons images: {complete}/{len(unique)} local; {missing} missing")
    for reference in unique:
        state = "local" if reference.local_file.exists() else "missing"
        print(f"  {state:7} {reference.local_file.name} <- {reference.commons_file}")
    return complete, missing


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--download", action="store_true", help="download a bounded batch")
    mode.add_argument("--sync-links", action="store_true", help="use existing local files")
    mode.add_argument("--status", action="store_true", help="report progress without writes")
    parser.add_argument(
        "--max-downloads",
        type=int,
        default=DEFAULT_MAX_DOWNLOADS,
        help="maximum download attempts in one run; 0 means uncapped",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=DEFAULT_SLEEP,
        help="seconds to wait between download attempts",
    )
    args = parser.parse_args()
    if args.max_downloads < 0:
        parser.error("--max-downloads must be at least 0")
    if args.sleep < 0:
        parser.error("--sleep must be at least 0")
    if not (args.download or args.sync_links or args.status):
        args.status = True
    return args


def main() -> int:
    args = parse_args()
    references = discover_references()
    unique = unique_references(references)
    if not unique:
        print("No Wikimedia Commons image links found in Pancakes Corner.")
        return 0

    if args.status:
        print_status(references)
        return 0

    if args.sync_links:
        changed = sync_local_links(references)
        print(f"Updated local image links in {changed} document(s).")
        print_status(discover_references())
        return 0

    missing = [reference for reference in unique if not reference.local_file.exists()]
    limit = len(missing) if args.max_downloads == 0 else args.max_downloads
    batch = missing[:limit]
    if not batch:
        changed = sync_local_links(references)
        print("All referenced Commons images are already local.")
        print(f"Updated local image links in {changed} document(s).")
        return 0

    failures = 0
    throttled = False
    IMAGES_ROOT.mkdir(parents=True, exist_ok=True)
    for index, reference in enumerate(batch, start=1):
        print(f"Downloading {reference.commons_file} -> {reference.local_file.name}")
        append_activity("download_start", reference)
        state, detail = download(reference)
        append_activity(f"download_{state}", reference, detail)
        print(f"  {state}: {detail}")
        if state == "throttled":
            throttled = True
            break
        if state == "failed":
            failures += 1
        if index < len(batch):
            print(f"Sleeping {args.sleep:g}s before the next attempt.")
            time.sleep(args.sleep)

    changed = sync_local_links(references)
    print(f"Updated local image links in {changed} document(s).")
    print_status(discover_references())
    if throttled:
        print("Wikimedia throttled the run; stop and allow a long cooldown.")
        return 75
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
