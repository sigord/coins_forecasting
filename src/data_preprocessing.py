
import numpy as np
import pandas as pd
from typing import List, Optional, Callable

from src.utils import conf

# feature engineering functions for time series

def add_lags(df: pd.DataFrame, column: str,
             lags: List[int], dropna: bool = True) -> pd.DataFrame:
    for lag in lags:
        df.loc[:, f'{column}_lag_{lag}'] = pd.Series(df[column].shift(lag))

    if dropna:
        df.dropna(inplace=True)
    return df


def add_rolling_mean(df: pd.DataFrame, column: str,
                     windows: List[int], dropna: bool = True) -> pd.DataFrame:
    for window in windows:
        df.loc[:, f'{column}_rolling_mean_{window}'] = pd.Series(df[column].rolling(window).mean())

    if dropna:
        df.dropna(inplace=True)
    return df


def get_X_y_timeseries(df: pd.DataFrame,
                       column: str,
                       test_size: float = 0.2,
                       lags: Optional[List[int]] = None,
                       windows_mean: Optional[List[int]] = None,
                       dropna: bool = True) -> pd.DataFrame:

    df = df[[column]]
    
    test_values = int(len(df) * test_size)
    
    if lags is not None:
        df = add_lags(df, column, lags, dropna)

    if windows_mean is not None:
        df = add_rolling_mean(df, column, windows_mean, dropna)

    df.loc[:, 'Time'] = np.arange(len(df))

    X = df.drop(column, axis=1)
    y = df.loc[:, column]

    return X, y

# main function for data preprocessing

def data_preprocessing(path_to_data: str = conf.dataset_path) -> List[pd.DataFrame]:
    df = pd.read_csv(path_to_data, index_col='Date')
    # invert the order of the dataframe
    df = df.iloc[::-1]
    df = df[['Close', 'High', 'Low']]
    df.index = pd.to_datetime(df.index)
    
    
    
if __name__ == '__main__':
    data_preprocessing()