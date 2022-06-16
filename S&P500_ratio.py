import pandas as pd
import csv
import moving_lobf_residual as lobf
import beta_calculator as bc


def create_r_squared_list():
    df = pd.read_csv("constituents.csv")
    f = csv.writer(open("S&P500 ratios", "w", newline=''))
    f.writerow(["ticker", "avg vv-ratio", "avg slope", "avg r2", "beta", "alpha"])

    for ticker in df["Symbol"]:
        f.writerow([
            ticker,
            lobf.get_moving_avg_r2(ticker)[0],
            lobf.get_moving_avg_r2(ticker)[1],
            lobf.get_moving_avg_r2(ticker)[2],
            bc.get_beta_and_alpha(ticker)[0],
            bc.get_beta_and_alpha(ticker)[1]])


if __name__ == '__main__':
    create_r_squared_list()



