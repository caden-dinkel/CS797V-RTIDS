# This file is for processing the simmilarHTTP column


def convert(val):
    if type(val) is not str:
        return 0
    else:
        return 1


def binary_conversion(df):
    df["SimillarHTTP"] = df["SimillarHTTP"].apply(convert)
