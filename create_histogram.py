import matplotlib.pyplot as plt
import pandas as pd


def histogram():
    df = pd.read_csv("S&P500 ratios.csv")

    # print(min(df["r-squared"]))
    plt.subplot(4, 1, 1)
    plt.hist(df["avg r2"])

    plt.subplot(4, 1, 2)
    plt.hist(df["beta"])

    plt.subplot(4, 1, 3)
    plt.hist(df["alpha"])

    plt.subplot(4, 1, 4)
    plt.hist(df.drop([433, 103, 19, 466, 375, 423, 316, 55, 434, 35])["avg vv-ratio"])

    plt.show()


if __name__ == '__main__':
    histogram()

    """
    df = pd.read_csv("S&P500 ratios.csv")
    plt.subplot(2, 1, 1)
    plt.scatter(abs(df["beta"]), df["avg r2"])
    plt.subplot(2, 1, 2)
    plt.scatter(df.drop(433)["beta"], df.drop(433)["avg vv-ratio"])
    plt.show()
    """
