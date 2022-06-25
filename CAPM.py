import pandas as pd
import csv
import beta_calculator as bc
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import math


def sml_attributes(marketpercent):
    sml = csv.writer(open("SML-" + str(marketpercent) + ".csv", "w", newline=''))
    sml.writerow(["ticker", "beta", "E(Ra)"])

    df = pd.read_csv("constituents.csv")

    for ticker in df["Symbol"]:
        y = bc.get_beta_and_alpha(ticker)
        sml.writerow([
            ticker,
            y[0],
            y[0] * marketpercent + y[1],
        ])

    sml_df = pd.read_csv("SML-" + str(marketpercent) + ".csv")

    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(sml_df["beta"],
                                                                         sml_df["E(Ra)"])

    plt.scatter(sml_df["beta"], sml_df["E(Ra)"], marker='o', s=1, color='b')
    x = np.linspace(min(sml_df["beta"]), max(sml_df["beta"]), 100)
    y = slope * x + intercept
    plt.plot(x, y, "r")
    for i,ticker in enumerate(sml_df["ticker"]):
        plt.annotate(ticker, (sml_df["beta"][i], sml_df["E(Ra)"][i]))
    plt.show()


if __name__ == '__main__':
    sml_attributes(0)
