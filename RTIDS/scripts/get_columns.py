import pandas as pd
from pandas import Series
import sys
import zipfile
from pathlib import Path
import os
import gc


def get_columns(file: Path) -> [str]:
    if file.is_file():
        header = pd.read_csv(file, nrows=0).columns.to_list()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: utils.py <path/to/file.csv|parquet>", file=sys.stderr)
        sys.exit(1)

    path = Path(sys.argv[1])
    
    (path)
    
    
    