#!/usr/bin/env python3
"""Verify runtime dependencies for export-doc (.docx build, audit, and optional Drive upload)."""

from __future__ import annotations

import json
import shutil
import sys


def main() -> int:
    required = {"docx": "python-docx", "lxml": "lxml", "PIL": "Pillow"}
    results: dict[str, str] = {}
    missing: list[str] = []

    for mod, pkg in required.items():
        try:
            __import__(mod)
            results[pkg] = "ok"
        except ImportError:
            results[pkg] = "missing"
            missing.append(pkg)

    gdrive_bin = shutil.which("gdrive")
    results["gdrive_cli"] = gdrive_bin if gdrive_bin else "not_on_path"

    payload = {
        "passed": len(missing) == 0,
        "python": sys.version.split()[0],
        "dependencies": results,
        "missing_required": missing,
    }
    print(json.dumps(payload, indent=2))
    return 0 if payload["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
