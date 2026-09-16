"""Report or explicitly acquire optional example data."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def manifest(root: Path) -> dict:
    return json.loads((root / "data/example-data.json").read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--acquire-schism", action="store_true", help="explicitly download the optional SCHISM fixture bundle")
    args = parser.parse_args()
    root = args.root.resolve()
    data = manifest(root)
    for dataset in data["datasets"]:
        path = root / dataset["local_path"]
        status = "available" if path.exists() else "absent (optional)"
        print(f"{dataset['id']}: {status}; source={dataset['source']}; scope={dataset['scope']}")
    if args.acquire_schism:
        from schism_case_data import ensure_schism_data
        print(f"Acquiring schism-regional into {ensure_schism_data(root / 'tests/data/schism')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
