import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import math


def roi_from_start(values, start=0):
    return (values - values[start]) / values[start]


def get_moving_avg_r2(ticker):
    df = pd.read_csv("S&P500 Prices/" + ticker + "_historical_closing_prices.csv", sep="\t", encoding='utf-8')
    # plt.scatter(df.index, df["close"])

    period = 20
    avg_r2 = 0
    avg_slope = 0
    avg_vv = 0
    df["ROI"] = roi_from_start(df["close"])

    for i in range(math.floor(df.shape[0] / period)):
        slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(df.index[i * period:(i + 1) * period],
                                                                             df["ROI"][i * period:(i + 1) * period])

        """
        x = np.linspace(i * period, (i + 1)*period, 100)
        y = slope * x + intercept
        plt.plot(x, y, "r")
        """
        avg_vv += (slope / (r_value ** 2)) / (math.floor(df.shape[0] / period))
        avg_slope += slope / (math.floor(df.shape[0] / period))
        avg_r2 += (r_value ** 2) / (math.floor(df.shape[0] / period))

    # plt.show()

    return avg_vv, avg_slope, avg_r2


# get_moving_avg_r2("AAPL")

if __name__ == '__main__':
    get_moving_avg_r2("PFG")
