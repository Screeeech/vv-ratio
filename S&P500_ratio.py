import pandas as pd
import csv
import moving_lobf_residual as lobf
import beta_calculator as bc


def create_r_squared_list():
    df = pd.read_csv("constituents.csv")
    f = csv.writer(open("S&P500 ratios.csv", "w", newline=''))
    f.writerow(["ticker", "avg vv-ratio", "avg slope", "avg r2", "beta", "alpha", "beta r2", "avg slope/r2", "avg wr2"])

    for ticker in df["Symbol"]:
        x = lobf.get_moving_avg_r2(ticker)
        y = bc.get_beta_and_alpha(ticker)
        f.writerow([
            ticker,
            x[0],
            x[1],
            x[2],
            y[0],
            y[1],
            y[2],
            x[1]/x[2],
            x[3]])


if __name__ == '__main__':
    create_r_squared_list()



