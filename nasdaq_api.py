# input ticker and read json form api to output price history and analyze in moving_average.py


import pandas as pd
from polygon import RESTClient
from typing import cast
from urllib3 import HTTPResponse
import datetime
import json
import ast





def getHistoricalData(ticker):
    client = RESTClient("9P7ogpJgyLF1lauT17eqrTAL7YiKriH0") # api_key is used

    year_ago = datetime.date.today() - datetime.timedelta(days=365)
    aggs = cast(
        HTTPResponse,
        client.get_aggs(
            ticker,
            1,
            "day",
            year_ago.strftime("%Y-%m-%d"),
            datetime.date.today().strftime("%Y-%m-%d"),
            raw=True,
        ),
    )

    data = pd.DataFrame(aggs)



    return aggs.data




if __name__ == '__main__':
    print(getHistoricalData("AAPL"))





