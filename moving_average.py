import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("AAPL_historical_closing_prices.csv", sep="\t", encoding='utf-8')
avg_df = pd.DataFrame(columns=["timestamp", "moving_average"])


t = 20
for count, value in df["close"].iteritems():
    if count == len(df["close"])-t:
        break

    avg = 0
    for i in range(t):
        avg += df["close"][count+i]/t

    avg_df.loc[count] = [df["timestamp"][count], avg]

plt.scatter(avg_df["timestamp"], avg_df["moving_average"])
plt.show()
