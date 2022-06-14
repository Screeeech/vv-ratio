import nasdaq_api as na
import read_csv as rc
import time


for ticker in rc.get_csv_tickers("constituents.csv"):
    na.get_historical_data(ticker)
    time.sleep(13)
