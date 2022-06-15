import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import math


def get_moving_avg_r2(ticker):
    df = pd.read_csv("S&P500 Prices/" + ticker + "_historical_closing_prices.csv", sep="\t", encoding='utf-8')
    avg_df = pd.DataFrame(columns=["moving_average"])

    period = 20
    for i in range(math.floor(df.shape[0] / period)):
        avg = 0
        for j in range(period):
            avg += df["close"][i * period + j] / period

        avg_df.loc[i] = [avg]

    """
    slope_df = pd.DataFrame(columns=["slope"])
    for i in range(1, df.shape[0] - 1):
        m = df["close"][i + 1] - df["close"][i - 1]
        m /= 3
        slope_df.loc[i] = [m]
    """

    # slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(slope_df.index, slope_df["slope"])
    slope_a, intercept_a, r_value_a, p_value_a, std_err_a = scipy.stats.linregress(avg_df.index,
                                                                                   avg_df["moving_average"])

    """
    def best_fit(x):
        return x * slope + intercept
    """

    def best_fit_a(x):
        return x * slope_a + intercept_a

    def graph(formula, x_range):
        x = np.array(x_range)
        y = formula(x)
        plt.plot(x, y, color="orange")

    plt.subplot(3, 1, 1)
    plt.scatter(avg_df.index, avg_df["moving_average"])
    graph(lambda x: best_fit_a(x), range(0, avg_df.shape[0]))

    plt.subplot(3, 1, 2)
    plt.scatter(df.index, df["close"])

    """
    plt.subplot(3, 1, 3)
    plt.scatter(slope_df.index, slope_df["slope"])
    graph(lambda x: best_fit(x), range(0, df.shape[0]))
    plt.show()

    print(r_value_a ** 2)
    print(r_value ** 2)"""

    return r_value_a**2
