"""Report the example data listed in data/example-data.json."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def manifest(root: Path) -> dict:
    return json.loads((root / "data/example-data.json").read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    data = manifest(root)
    for dataset in data["datasets"]:
        path = root / dataset["local_path"]
        status = "available" if path.exists() else "absent (optional)"
        print(f"{dataset['id']}: {status}; source={dataset['source']}; scope={dataset['scope']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
