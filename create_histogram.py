import matplotlib.pyplot as plt
import pandas as pd


def histogram():
    df = pd.read_csv("S&P500 ratios.csv")

    # print(min(df["r-squared"]))
    plt.subplot(3, 1, 1)
    plt.hist(df["avg r2"], alpha=0.3)

    plt.subplot(3, 1, 2)
    plt.hist(df["beta"], alpha=0.3)

    plt.subplot(3, 1, 3)
    plt.hist(df["alpha"], alpha=0.3)
    plt.show()


if __name__ == '__main__':
    histogram()
