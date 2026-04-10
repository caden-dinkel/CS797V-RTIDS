import pandas as pd
import sys
import zipfile
from pathlib import Path
import os
import gc

def dir_has_matching_data(file: Path):
    if file.is_file():
            
        print(f"Loading file: {file}")
        df = pd.read_csv(file, nrows=100)  # small sample
        for col, dtype in df.dtypes.items():
            print(f"Column Name: {col:<30} Date Type: {dtype}")
        del df
        gc.collect()     
    



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: utils.py <path/to/file.csv|parquet>", file=sys.stderr)
        sys.exit(1)

    path = Path(sys.argv[1])
    
    dir_has_matching_data(path)
