import scipy.stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def roi_from_index(values, start, end):
    return (values[end] - values[start]) / values[start]


def roi_from_start(values):
    return (values - values[0]) / values[0]


def get_beta_and_alpha(ticker):
    ticker_df = pd.read_csv("S&P500 Prices/" + ticker + "_historical_closing_prices.csv", sep="\t", encoding="utf-8", index_col=0)
    sp500_df = pd.read_csv("S&P500-index.csv", encoding="utf-8")

    ticker_df["roi"] = roi_from_start(ticker_df["close"])
    sp500_df["roi"] = roi_from_start(sp500_df["close"])

    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(sp500_df["roi"][0:ticker_df.shape[0]],
                                                                         ticker_df["roi"])

    """
    plt.scatter(sp500_df["roi"], ticker_df["roi"])
    x = np.linspace(0, max(sp500_df["roi"]), 100)
    y = slope*x + intercept
    plt.plot(x, y, "r")
    plt.show()
    """

    return (slope, intercept, r_value**2)




