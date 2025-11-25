"""Read data/metadata/sources.yaml and download non-placeholder sources into data/raw/."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import List, Dict

import requests
import yaml

PLACEHOLDER_URL = "TODO_FILL_IN_MANUALLY"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 "
    "madrigal-equity-research/0.1 (contact: example@example.com)"
)
REQUEST_TIMEOUT = (10, 180)  # connect, read timeouts in seconds


def load_sources(config_path: Path) -> List[Dict]:
    """Load source metadata from YAML."""
    with config_path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    return data.get("sources", [])


def download_one(session: requests.Session, source: Dict, raw_root: Path, force: bool = False) -> str:
    """Download a single source file; returns status string."""
    target = raw_root / source["local_path"]
    target.parent.mkdir(parents=True, exist_ok=True)

    if target.exists() and not force:
        print(f"[skip] {source['id']} already exists at {target}")
        return "skipped"

    try:
        response = session.get(
            source["url"],
            stream=True,
            timeout=REQUEST_TIMEOUT,
            headers={"User-Agent": USER_AGENT},
        )
        response.raise_for_status()
        with target.open("wb") as fh:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    fh.write(chunk)
        print(f"[ok] Downloaded {source['id']} -> {target}")
        return "downloaded"
    except requests.RequestException as exc:
        print(f"[warn] Failed to download {source['id']} from {source['url']}: {exc}")
        return "failed"


def main() -> None:
    parser = argparse.ArgumentParser(description="Download core Madrigal documents.")
    parser.add_argument("--force", action="store_true", help="Re-download even if file exists")
    args = parser.parse_args()

    data_dir = Path(__file__).resolve().parent
    metadata_path = data_dir / "metadata" / "sources.yaml"
    raw_root = data_dir / "raw"

    sources = load_sources(metadata_path)

    downloaded = skipped = failed = 0

    with requests.Session() as session:
        for source in sources:
            url = source.get("url", "")
            if not url or url == PLACEHOLDER_URL:
                print(f"[skip] {source['id']} has placeholder URL")
                skipped += 1
                continue

            status = download_one(session, source, raw_root, force=args.force)
            if status == "downloaded":
                downloaded += 1
            elif status == "failed":
                failed += 1
            else:
                skipped += 1

    print(
        f"Summary: downloaded={downloaded}, skipped={skipped}, failed={failed}")


if __name__ == "__main__":
    main()
