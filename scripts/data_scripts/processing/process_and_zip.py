from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow.parquet as pq
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

dirpath = Path("data/intermediate/CICIDS2017")

files = dirpath.rglob("*.parquet")

df = pd.concat([pd.read_parquet(f) for f in files], ignore_index=True)

numeric_df = df.select_dtypes(include=[np.number])

df = df[~np.isinf(numeric_df).any(axis=1)]

# 1. Scale ONLY the features
X = df.drop(columns=["Label"])
y = df["Label"].reset_index(drop=True)  # Reset index to ensure alignment

scaler = MinMaxScaler()
X_scaled_array = scaler.fit_transform(X)

# 2. Convert back to DataFrame to keep column names
X_scaled_df = pd.DataFrame(X_scaled_array, columns=X.columns)

# 3. Recombine
final_df = pd.concat([X_scaled_df, y], axis=1)

# 4. Export
# Use Parquet instead of CSV if your group's environment allows (like Nix/Python)
# It handles the "Label" string/category type much better than CSV.
final_df.to_parquet("CICIDS2017.parquet", index=False)
final_df.to_csv("CICIDS2017.csv", index=False)

"""
X = df.drop(columns=["Label"])


y = df["Label"]

scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)


X_normalized.to_csv("CICIDS2017.csv", index=False)

"""

"""
X_train, X_test, y_train, y_test = train_test_split(
    X_normalized, y, test_size=0.2, stratify=y, random_state=42
)

smote = SMOTE(sampling_strategy="minority", random_state=42)

X_train_sm, y_train_sm = smote.fit_resample(X_train, y_train)

X_train_sm.to_csv("X_train.csv", index=False)
y_train_sm.to_csv("y_train.csv", index=False)
X_test[0].to_csv("X_test.csv", index=False)
y_test[0].to_csv("y_test.csv", index=False)
"""
