#!/usr/bin/env python3
"""Check that the feedstock's Rust compiler matches Zenoh's toolchain."""

from __future__ import annotations

import argparse
import re
import sys
import tomllib
from pathlib import Path


DEFAULT_CONFIG = Path(__file__).with_name("conda_build_config.yaml")


def configured_rust_version(config_path: Path) -> str:
    matches = re.findall(
        r"^rust_compiler_version:\s*\n\s*-\s*['\"]?([^'\"\s#]+)['\"]?"
        r"\s*(?:#.*)?$",
        config_path.read_text(encoding="utf-8"),
        flags=re.MULTILINE,
    )
    if len(matches) != 1:
        raise ValueError(
            f"Could not find a single rust_compiler_version in {config_path}"
        )
    return matches[0]


def upstream_rust_version(toolchain_path: Path) -> str:
    parsed = tomllib.loads(toolchain_path.read_text(encoding="utf-8"))
    try:
        return str(parsed["toolchain"]["channel"])
    except KeyError as error:
        raise ValueError(
            f"Could not find toolchain.channel in {toolchain_path}"
        ) from error


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("toolchain", type=Path)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    args = parser.parse_args()

    configured = configured_rust_version(args.config)
    upstream = upstream_rust_version(args.toolchain)

    print(f"Feedstock rust_compiler_version: {configured}")
    print(f"Zenoh rust-toolchain channel:    {upstream}")

    if configured != upstream:
        print(
            "Rust compiler version mismatch: update "
            f"{args.config} from {configured} to {upstream}.",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
