import sys
from pathlib import Path

import pandas as pd

# Methods for processing `Timestamp` column

# Method 1: Dropping column


def drop_timestamp(df):
    df.drop("Timestamp")


# Method 2: Parsing time of day, day of week, time delta from constant.
# This is not very applicable, considering the method by which the dataset was generated.
# If this was in a real system however, this could be impactful.


def get_time_difference(time):
    return pd.Timestamp(time) - pd.Timestamp("2017-01-01 00:00:01")


def preprocess_timestamps_2017(df):
    df[" Timestamp"] = df[" Timestamp"].apply(get_time_difference)


def load_dataset(path: Path):
    if path.is_file():
        df = pd.read_csv(path, nrows=100, low_memory=False)
        preprocess_timestamps_2017(df)
        print(df[" Timestamp"])
