import ipaddress

# This file defines methods of processing the IP columns


# Method 1: IP to numerical
# This method is a naive conversion from the IP to a number, stripping any non-numerical data
# Based on the phrasing in the paper, this is believe to be the choice of the authors.


def ip_to_int(ip):
    try:
        return int(ipaddress.ip_address(ip))
    except ValueError:
        return 0  # or np.nan


def ip_to_num(df):
    df["Source IP"] = df["Source IP"].apply(ip_to_int)
    df["Destination IP"] = df["Destination IP"].apply(ip_to_int)
