import gc
import sys
from pathlib import Path

import pandas as pd


def print_simillar_http_values(dir_path):
    value_set = set()

    for file in dir_path.rglob("*.csv"):
        if file.is_file():
            print(f"Loading file: {file}")

            df = pd.read_csv(file, usecols=["Source IP"], low_memory=False)

            value_set.update(df["SimillarHTTP"].dropna().unique())

            del df
            gc.collect()

    pd.Series(list(value_set)).to_csv("SourceIP_ValueSet.csv", index=False)


def bad_files(path):
    for file in path.rglob("*.csv"):
        print("loading: ", file)
        try:
            pd.read_csv(file, nrows=10000)
        except Exception as e:
            print("BAD FILE:", file)
            print(e)
            break


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: get_types.py <path/to/csv_dir>", file=sys.stderr)
        sys.exit(1)
    path = Path(sys.argv[1])

    print_simillar_http_values(path)
