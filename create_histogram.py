import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats


def histogram():
    df = pd.read_csv("S&P500 ratios.csv")

    # print(min(df["r-squared"]))
    plt.subplot(4, 1, 1)
    plt.hist(df["avg r"])

    plt.subplot(4, 1, 2)
    plt.hist(df["beta"])

    plt.subplot(4, 1, 3)
    plt.hist(df["alpha"])

    drop = []
    for i in range(df.shape[0]):
        if abs(df["avg vv-ratio"][i]) > 0.1:
            drop.append(i)

    plt.subplot(4, 1, 4)
    plt.hist(df.drop(drop)["avg vv-ratio"])

    plt.show()


if __name__ == '__main__':
    df = pd.read_csv("S&P500 ratios.csv")
    # df["avg slope/r2"] = df["avg slope"]/df["avg r2"]
    """
    drop = []
    for i in range(df.shape[0]):
        if abs(df["avg slope/r"][i]-0.019798) > 0.8637015109399775:
            drop.append(i)
    """

    plt.subplot(221)
    plt.hist(df["avg r2"])

    plt.subplot(222)
    plt.hist(df["avg slope/r2"])

    plt.subplot(223)
    plt.hist(df["avg wr2"])

    plt.subplot(224)
    plt.hist(df["avg slope/r2"]/np.abs(df["avg slope"]))
    # print(scipy.stats.describe(df["avg slope/r"]))

    # plt.scatter(df["beta"], df["avg slope/r"])

    plt.show()

