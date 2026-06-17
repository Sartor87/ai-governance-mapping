#!/usr/bin/env python3
"""Thin entry point: `python tools/compliance_check.py <project.yaml>`.

The implementation lives in the installable ``aigov`` package; this shim exists
so the script is runnable from a checkout without installing. Prefer the
``compliance-check`` console script after ``pip install -e .``.
"""

from aigov.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
