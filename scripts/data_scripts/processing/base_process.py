import pandas as pd


# Given some dataframe, returns all unique values in Label column.
def find_unique(df, column):
    value_set = set()
    value_set.update(df[column].dropna().unique())
    return value_set
