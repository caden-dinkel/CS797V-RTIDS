import pandas as pd
import sys
import zipfile
from pathlib import Path
import os
import gc


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: find_string_entries.py <path/to/file.csv|parquet> <column_name>", file=sys.stderr)
        sys.exit(1)

    path = Path(sys.argv[1])
    
    (path)