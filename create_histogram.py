import matplotlib.pyplot as plt
import pandas as pd


def histogram():
    df = pd.read_csv("S&P500_r-squared_list.csv")
    x = []

    for r2 in df["r-squared"]:
        x.append(r2)
    print(min(x))
    plt.hist(x)
    plt.show()



if __name__ == '__main__':
    histogram()
