import pandas as pd


def get_csv_tickers(file):
    data = pd.read_csv(file).Symbol
    return data
