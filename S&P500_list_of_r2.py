import pandas as pd
import csv
import moving_average as ma


def create_r_squared_list():
    df = pd.read_csv("constituents.csv")
    f = csv.writer(open("S&P500_r-squared_list.csv", "w", newline=''))
    f.writerow(["ticker", "r-squared"])

    for symbol in df["Symbol"]:
        f.writerow([
            symbol,
            ma.get_moving_avg_r2(symbol)])


