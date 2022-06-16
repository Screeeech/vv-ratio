import matplotlib.pyplot as plt
import pandas as pd
import moving_lobf_residual as lobfr
import csv
import beta_calculator


def histogram():
    df = pd.read_csv("S&P500_r-squared_list.csv")
    x = []

    for r2 in df["r-squared"]:
        x.append(r2)
    print(min(x))
    plt.hist(x)
    plt.show()


def histogram_moving_lobf():
    df = pd.read_csv("S&P500_r-squared_list.csv", encoding='utf-8')

    x = []

    for ticker in df["ticker"]:
        x.append(lobfr.get_moving_avg_r2(ticker))

    print(min(x))
    print(max(x))
    plt.hist(x)
    plt.show()

    f = csv.writer(open("beta_values.csv", "w", newline=''))
    f.writerow(["ticker", "beta"])

    for ticker in df["ticker"]:

        f.writerow([
            ticker,
            beta_calculator.get_beta(ticker)
        ])


if __name__ == '__main__':
    #histogram()
    histogram_moving_lobf()
