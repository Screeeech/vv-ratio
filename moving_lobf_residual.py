import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import math


def roi_from_start(values, start=0):
    return (values - values[start]) / values[start]


def get_moving_avg_r2(ticker):
    df = pd.read_csv("S&P500 Prices/" + ticker + "_historical_closing_prices.csv", sep="\t", encoding='utf-8')
    plt.scatter(df.index, roi_from_start(df["close"]), s=1)

    period = 30
    avg_r2 = 0
    avg_slope = 0
    avg_vv = 0

    weight = 1
    avg_wr2 = 0

    df["ROI"] = roi_from_start(df["close"])

    for i in range(math.floor(df.shape[0] / period)):
        slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(df.index[i * period:(i + 1) * period],
                                                                             df["ROI"][i * period:(i + 1) * period])

        x = np.linspace(i * period, (i + 1)*period, 100)
        y = slope * x + intercept
        plt.plot(x, y, "r")


        avg_vv += (slope / (r_value ** 2)) / (math.floor(df.shape[0] / period))
        avg_slope += slope / (math.floor(df.shape[0] / period))
        avg_r2 += (r_value**2) / (math.floor(df.shape[0] / period))
        avg_wr2 = weight * (r_value**2) / (math.floor(df.shape[0] / period))

        weight += .5/math.floor(df.shape[0] / period)
        # print(r_value**2)


    return avg_vv, avg_slope, avg_r2, avg_wr2


# get_moving_avg_r2("AAPL")

if __name__ == '__main__':
    """
    plt.subplot(421)
    get_moving_avg_r2("DVN")

    plt.subplot(422)
    get_moving_avg_r2("GPS")

    plt.subplot(423)
    get_moving_avg_r2("TDY")

    plt.subplot(424)
    get_moving_avg_r2("PAYC")

    plt.subplot(425)
    get_moving_avg_r2("ICE")

    plt.subplot(426)
    get_moving_avg_r2("BDX")

    plt.subplot(427)
    get_moving_avg_r2("ACN")
    """
    # print(get_moving_avg_r2("TDY")[2])
    print(get_moving_avg_r2("WLTW"))
    plt.show()
