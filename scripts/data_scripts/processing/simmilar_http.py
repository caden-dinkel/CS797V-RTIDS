# This file is for processing the simmilarHTTP column

# Method 1: Direct binary conversion
# The authors aren't very clear on what they did. We will try and compare a variety of approaches
# This approach is a direct binary conversion. If there is a string present: 1, else: 0.


def binary_conversion(df):
    df["SimillarHTTP"] = 0 ? df["SimillarHTTP"] == 0 : 1
