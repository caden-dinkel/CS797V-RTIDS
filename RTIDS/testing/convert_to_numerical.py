import pandas as pd
import sys
import zipfile
from pathlib import Path
import os
import gc


def dir_has_matching_data(dir_path: Path):
    datatypes = []
    for file in dir_path.rglob("*.csv"):
        if file.is_file():
            
            print(f"Loading file: {file}")
            df = pd.read_csv(file, nrows=100)  # small sample
            datatypes.append(df.dtypes)
            del df
            gc.collect()     

    truth = compare_dtypes(datatypes)
    print(f"{dir_path}")
    
    print(f"All CSVs in {dir_path} have the same schema. Status: {truth}.")

def compare_dtypes(collection: list[pd.Series]) -> bool:
    first = collection[0]
    truth = True
    for i, other in enumerate(collection[1:], start=1):
        if not first.equals(other):
            print(f"Mismatch found in file #{i}")
            print("Differences:")
            print(first.compare(other))
            truth = False
        else:
            print(f"Schema matches in file #{i}")
    return truth

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: utils.py <path/to/file.csv|parquet>", file=sys.stderr)
        sys.exit(1)

    path = Path(sys.argv[1])
    
    dir_has_matching_data(path)
    
