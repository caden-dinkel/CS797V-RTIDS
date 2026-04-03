import pandas as pd
import sys
import zipfile
from pathlib import Path
import os
import gc


df = pd.read_csv("./data/CIC-DDoS2019/03-11/Portmap.csv", dtype={"SimillarHTTP":"object"})

col = df["SimillarHTTP"]

numeric = pd.to_numeric(col, errors="coerce")

string_mask = numeric.isna()

string_values = col[string_mask]
string_indices = col.index[string_mask]

for i, val in string_values.items():
    print(f"{i}.  {val}")