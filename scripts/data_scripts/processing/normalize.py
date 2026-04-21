# Data normalization techniques
import pandas as pd

# Method 1: Min-Max normalization
from sklearn.preprocessing import MinMaxScaler


# Parameter df should not have label/str data within it, this might ignore it anyway, not sure.
def min_max_norm(df: pd.DataFrame):
    # Should be done independently for each column in the dataframe:
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df)
    return df_scaled
