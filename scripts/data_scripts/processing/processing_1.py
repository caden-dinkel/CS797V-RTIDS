import ipaddress
import sys
from pathlib import Path

import pandas as pd
from base_process import find_unique

# from methods.process_ips import ip_to_num
from pandas import DataFrame
from sklearn.preprocessing import MinMaxScaler

# Columns to drop
"""
|  0 | Flow ID                     | str*        |
|  6 | Timestamp                   | str*        |

If CIC-DDoS2019:
| 85 | SimillarHTTP                | int, str* |
"""

# Column to consider
# I think I'll write it into the parquets as well, but will likely need special considerations.
"""
| 87 | Label                       | str*      |
"""

# Columns to transform
"""
|  1 | Source IP                   | str*        |
|  3 | Destination IP              | str*        |
"""


# Parameter df should not have label/str data within it, this might ignore it anyway, not sure.
def min_max_norm(df: pd.DataFrame):

    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df)
    return df_scaled


def ip_to_int(ip):
    try:
        return int(ipaddress.ip_address(ip))
    except ValueError:
        return 0


def ip_to_num(df):
    df["Source IP"] = df["Source IP"].apply(ip_to_int)
    df["Destination IP"] = df["Destination IP"].apply(ip_to_int)


def process(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.strip()
    ip_to_num(df)

    df = df.drop(columns=["Timestamp", "Flow ID"], errors="ignore")

    if "SimillarHTTP" in df.columns:
        df = df.drop(columns=["SimillarHTTP"])

    return df


def write_partitioned_parquet(df: pd.DataFrame, base_path: Path):
    for label, group in df.groupby("Label"):
        label_path = base_path / f"Label={label}"
        label_path.mkdir(parents=True, exist_ok=True)

        file_path = label_path / f"part-{pd.Timestamp.now().value}.parquet"
        group.to_parquet(file_path, index=False)


def load_process_csv(dir_path: Path, out_path: Path, chunksize=1_000_000):
    for file in dir_path.rglob("*.csv"):
        if not file.is_file():
            continue

        print(f"Processing: {file}")

        for chunk in pd.read_csv(
            file,
            encoding="cp1252",
            low_memory=False,
            skip_blank_lines=True,
            chunksize=chunksize,
        ):
            chunk = process(chunk)
            write_partitioned_parquet(chunk, out_path)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python processing_1.py src/data dest/data", file=sys.stderr)
        sys.exit(1)
    path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])

    load_process_csv(path, out_path)
