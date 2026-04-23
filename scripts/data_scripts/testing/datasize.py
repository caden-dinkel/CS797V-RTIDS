# This is a script to determine the total size of individual csv's and whole datasets.

import os
import sys
from pathlib import Path

import pandas as pd


def get_file_sizes(dir_path: Path):
    filesizes = {}
    for file in dir_path.rglob("*.csv"):
        if file.is_file():
            filesizes[file.name] = os.path.getsize(file) / (2**30)
    return filesizes


def to_markdown_table(filesizes):
    files = list(filesizes.keys())
    files.append("Total")
    sizes = list(filesizes.values())
    sizes.append(sum(sizes))
    df = pd.DataFrame(
        {
            "File": list(files),
            "Size (GB)": list(sizes),
        }
    )
    return df.to_markdown(index=True)


def print_dir_file_sizes(dir_path: Path):
    filesizes = get_file_sizes(dir_path)
    md = to_markdown_table(filesizes)
    filepath = Path(dir_path / "file-size.md")
    filepath.write_text(md)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: get_types.py <path/to/csv_dir>", file=sys.stderr)
        sys.exit(1)
    path = Path(sys.argv[1])

    print_dir_file_sizes(path)
