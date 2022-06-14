from polygon import RESTClient
from typing import cast
from urllib3 import HTTPResponse
import datetime
import json
import csv


def get_historical_data(ticker):
    print("getting data for " + ticker)
    client = RESTClient("9P7ogpJgyLF1lauT17eqrTAL7YiKriH0")  # api_key is used

    year_ago = datetime.date.today() - datetime.timedelta(days=365)
    aggs = json.loads(cast(
                HTTPResponse,
                client.get_aggs(
                    ticker,
                    1,
                    "day",
                    year_ago.strftime("%Y-%m-%d"),
                    datetime.date.today().strftime("%Y-%m-%d"),
                    raw=True,
                ),
            ).data.decode('utf8'.replace("''", '""')))

    f = csv.writer(open("S&P500 Prices/" + ticker + "_historical_closing_prices.csv", "w", newline=''))
    f.writerow(["timestamp", "close"])

    for i in aggs['results']:
        f.writerow([
            datetime.datetime.fromtimestamp(i['t'] / 1000.0),
            i['c']])
