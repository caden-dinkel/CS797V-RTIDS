# Load/Preprocess dataset

import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Standardize Column Names


def standardize_columns(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(r"\s+", "_", regex=True)
    return df


# Find columns with only zeros or constant values


def find_const_columns(df):
    constant_cols = [col for col in df.columns if df[col].nunique() == 1]
    return constant_cols


# Coerce string values into numerics if possible

# Label encode ips


def convert_ips(df):
    df["source_ip"] = df["source_ip"].astype("category").cat.codes
    df["destination_ip"] = df["destination_ip"].astype("category").cat.codes
    return df


# Remove any rows that are still not allowed.


def normalize(df):
    numeric_df = df.select_dtypes(include=[np.number])
    df = df[~numeric_df.isin([np.inf, -np.inf]).any(axis=1)]

    X = df.drop(columns=["label"])
    y = df["label"].reset_index(drop=True)

    scaler = MinMaxScaler()

    X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

    comb_df = pd.concat([X_scaled, y], axis=1)

    return comb_df


def preprocess(df):
    # 1: Standardize column names
    df = standardize_columns(df)

    # 2: Find/remove const/zero columns
    const_cols = find_const_columns(df)

    df = df.drop(columns=const_cols)

    # 3: Remove flow_id and timestamp
    drop_cols = ["flow_id", "timestamp", "simillarHTTP"]
    df = df.drop(columns=drop_cols, errors="ignore")

    # 3: Encode IPs
    df = convert_ips(df)

    # 4: Normalize Dataset
    preprocessed_dataset = normalize(df)

    return preprocessed_dataset


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python processing_1.py src/data/ dest/data/", file=sys.stderr)
        sys.exit(1)
    path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])

    out_path.mkdir(parents=True, exist_ok=True)
    files = path.rglob("*.csv")
    df = pd.concat(
        [
            pd.read_csv(f, encoding="cp1252", skip_blank_lines=True, low_memory=False)
            for f in files
        ],
        ignore_index=True,
    )
    processed_df = preprocess(df)
    processed_df.to_parquet(out_path / Path("CICIDS2017.parquet"), index=False)
    processed_df.to_csv(out_path / Path("CICIDS2017.csv"), index=False)
