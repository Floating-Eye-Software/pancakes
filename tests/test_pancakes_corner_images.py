from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "fetch_pancakes_corner_images.py"
SPEC = importlib.util.spec_from_file_location("pancakes_corner_images", SCRIPT)
assert SPEC and SPEC.loader
pci = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = pci
SPEC.loader.exec_module(pci)


class PancakesCornerImageTests(unittest.TestCase):
    def test_commons_filename_decodes_url(self) -> None:
        page = "https://commons.wikimedia.org/wiki/File:Nale%C5%9Bniki.jpg"
        self.assertEqual(pci.commons_filename(page), "Naleśniki.jpg")

    def test_initial_set_uses_stable_local_names(self) -> None:
        self.assertEqual(
            pci.local_filename("Injera_with_eight_kinds_of_stew.jpg"),
            "injera-eight-stews.jpg",
        )
        self.assertEqual(
            pci.local_filename("البغرير_المغربي.jpg"),
            "baghrir-moroccan.jpg",
        )

    def test_generic_local_name_is_safe_and_preserves_extension(self) -> None:
        self.assertEqual(
            pci.generic_local_filename("Future_pancake_photo.PNG"),
            "future-pancake-photo.png",
        )

    def test_sync_rewrites_only_when_local_file_exists(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            document = root / "article.md"
            image = root / "images" / "dosa.jpg"
            page = "https://commons.wikimedia.org/wiki/File:Dosa.jpg"
            remote = (
                "https://commons.wikimedia.org/wiki/Special:Redirect/file/"
                "Dosa.jpg?width=1200"
            )
            document.write_text(
                f"[![Dosa.]({remote})]({page})\r\n",
                encoding="utf-8",
                newline="",
            )
            reference = pci.ImageReference(
                document=document,
                alt="Dosa.",
                display=remote,
                commons_page=page,
                commons_file="Dosa.jpg",
                local_file=image,
            )

            self.assertEqual(pci.sync_local_links([reference]), 0)
            image.parent.mkdir()
            image.write_bytes(b"\xff\xd8\xfftest")
            self.assertEqual(pci.sync_local_links([reference]), 1)
            with document.open("r", encoding="utf-8", newline="") as handle:
                updated = handle.read()
            self.assertIn("](images/dosa.jpg)]", updated)
            self.assertTrue(updated.endswith("\r\n"))

    def test_valid_image_recognizes_supported_formats(self) -> None:
        self.assertTrue(pci.valid_image(b"\xff\xd8\xffjpeg"))
        self.assertTrue(pci.valid_image(b"\x89PNG\r\n\x1a\npng"))
        self.assertFalse(pci.valid_image(b"<!doctype html>not an image"))


if __name__ == "__main__":
    unittest.main()
