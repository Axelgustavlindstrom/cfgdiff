from __future__ import annotations

from cfgdiff.cli import main as _cli_main
from cfgdiff.diff import DiffEntry, diff_files, load_config, normalize_value

__all__ = [
    "DiffEntry",
    "diff_files",
    "load_config",
    "normalize_value",
]


def main(argv: list[str] | None = None) -> int:
    import sys

    args = sys.argv[1:] if argv is None else argv
    return _cli_main(args)


if __name__ == "__main__":
    raise SystemExit(main())
