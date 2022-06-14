# read consitutients.csv and store as list to feed into nasdaq_api.py
import pandas as pd
import datetime


def get_csv_tickers(file):
    data = pd.read_csv(file).Symbol
    return data
