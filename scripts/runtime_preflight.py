"""Check optional model-runtime prerequisites without running a model."""
from __future__ import annotations

import argparse
import os
import shutil

BINARIES = {"swan": ("ROMPY_SWAN_BIN", "swan"), "xbeach": ("ROMPY_XBEACH_BIN", "xbeach"), "schism": ("ROMPY_SCHISM_BIN", "pschism")}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model", choices=sorted(BINARIES))
    args = parser.parse_args()
    variable, default = BINARIES[args.model]
    candidate = os.environ.get(variable, default)
    resolved = shutil.which(candidate) if os.path.basename(candidate) == candidate else candidate if os.path.isfile(candidate) else None
    if not resolved:
        print(f"{args.model} runtime unavailable: set {variable} to the executable path or install '{default}'")
        return 1
    print(f"{args.model} runtime prerequisite available: {resolved}")
    print("Preflight only; scientific/model integration validation still requires an explicit runtime test.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
