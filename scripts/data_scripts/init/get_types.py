import gc
import sys
from collections import defaultdict
from pathlib import Path

import pandas as pd
from numpy.random import seed

# This file contains a script to analyze some set of csvs, and create an aggregate schema table of the csvs.
#


def analyze_types(df):
    sample = df.sample(min(1000, len(df)))

    type_sets = {}
    for col in sample.columns:
        types = {type(val).__name__ for val in sample[col]}
        type_sets[col] = types if types else {"N/A"}

    return type_sets


def create_aggregate(datatypes):
    aggregate = defaultdict(set)
    for datatype in datatypes:
        for col, dtypes in datatype.items():
            aggregate[col].update(dtypes)
    return aggregate


def analyze_types_dir(dir_path: Path):
    datatypes = []
    for file in dir_path.rglob("*.csv"):
        if file.is_file():
            print(f"Loading file: {file}")
            df = pd.read_csv(file, nrows=1000)  # small sample
            datatypes.append(analyze_types(df))
            del df
            gc.collect()
    return datatypes


HIGHLIGHT = {"str": "*", "float": "†"}


def format_type(t):
    return f"{t}{HIGHLIGHT.get(t, '')}"


def to_markdown_table(aggregate):
    df = pd.DataFrame(
        {
            "Column": list(aggregate.keys()),
            "Types": [
                ", ".join(format_type(t) for t in sorted(v)) for v in aggregate.values()
            ],
        }
    )
    return df.to_markdown(index=True)


def print_dir_agg_types(dir_path: Path):
    datatypes = analyze_types_dir(dir_path)
    aggregate = create_aggregate(datatypes)
    md = to_markdown_table(aggregate)
    filepath = Path(dir_path / "schema.md")
    filepath.write_text(
        "** `*` indicates string values present in the column \n `†` \
        indicates float values present in the column ** \n"
        + md,
        newline="\n",
    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: get_types.py <path/to/csv_dir>", file=sys.stderr)
        sys.exit(1)
    path = Path(sys.argv[1])

    print_dir_agg_types(path)
