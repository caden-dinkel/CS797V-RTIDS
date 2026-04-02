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
    
    


def csv_to_parquet(csv_path: Path):
    parquet_path = csv_path.with_suffix(".parquet")
    try:
        df = pd.read_csv(csv_path, low_memory=False, encoding="latin-1")

        # Normalize column names: strip surrounding whitespace
        df.columns = df.columns.str.strip()

        # Drop spurious pandas index columns (e.g. "Unnamed: 0")
        df = df.loc[:, ~df.columns.str.match(r"^Unnamed")]

        # Fix mixed-type object columns (e.g. SimillarHTTP has both int 0 and str '0').
        # If every non-null value converts to a number without introducing new NaNs,
        # store as float. Otherwise keep as string (handles IPs, labels, etc.).
        for col in df.select_dtypes(include="object").columns:
            converted = pd.to_numeric(df[col], errors="coerce")
            newly_null = converted.isna() & df[col].notna()
            if not newly_null.any():
                df[col] = converted
            else:
                df[col] = df[col].astype(str)

        df.to_parquet(parquet_path, index=False)
    except Exception as e:
        print(f"Error converting '{csv_path}': {e}", file=sys.stderr)
