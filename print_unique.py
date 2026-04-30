from pathlib import Path

import pandas as pd

dirpath = Path("data/preprocessed/CICIDS2017/CICIDS2017.parquet")

df = pd.read_parquet(dirpath)

"""
files = dirpath.rglob("*.csv")

df = pd.concat(
    [
        pd.read_csv(f, encoding="cp1252", skip_blank_lines=True, low_memory=False)
        for f in files
    ],
    ignore_index=True,
)
"""

print(df["label"].value_counts())
