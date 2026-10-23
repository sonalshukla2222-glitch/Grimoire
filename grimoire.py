#!/usr/bin/env python3
"""Grimoire: scan a local, authorized codebase for password-related keyword hits."""

import argparse
from pathlib import Path

TEXT_EXTENSIONS = {
    ".py", ".js", ".ts", ".java", ".kt", ".go", ".rs", ".php",
    ".rb", ".cs", ".cpp", ".c", ".h", ".html", ".xml", ".json",
    ".yaml", ".yml", ".toml", ".ini", ".env", ".properties", ".sh",
    ".sql", ".md", ".txt",
}
SKIP_DIRS = {
    ".git", "node_modules", ".venv", "venv", "env",
    "__pycache__", "dist", "build",
}


def scan_file(path: Path):
    """Yield (line_number, line_text) for lines containing 'password'."""
    try:
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            for line_number, line in enumerate(handle, start=1):
                if "password" in line.casefold():
                    yield line_number, line.rstrip()
    except (OSError, UnicodeError) as exc:
        print(f"[!] Could not read {path}: {exc}")


def scan_directory(root: Path) -> int:
    matches = 0

    for current_dir, dirs, filenames in __import__("os").walk(root):
        dirs[:] = [name for name in dirs if name not in SKIP_DIRS]
        for filename in filenames:
            path = Path(current_dir) / filename
            if path.suffix.lower() not in TEXT_EXTENSIONS and filename not in {
                ".env", "Dockerfile", "Makefile"
            }:
                continue

            for line_number, line in scan_file(path):
                matches += 1
                relative_path = path.relative_to(root)
                print(f"[!] Possible keyword match: {relative_path}:{line_number}")
                print(f"    {line}")

    print(f"\nScan complete. {matches} matching line(s).")
    return matches


def main():
    parser = argparse.ArgumentParser(
        description="Search a local codebase you own or are authorized to review "
                    "for lines containing the word 'password'."
    )
    parser.add_argument("directory", help="Path to the local repository to scan")
    args = parser.parse_args()

    root = Path(args.directory).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        parser.error(f"Not a directory: {root}")

    scan_directory(root)


if __name__ == "__main__":
    main()
