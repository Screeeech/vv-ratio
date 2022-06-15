import pandas as pd
import matplotlib.pyplot as plt
import math

ticker = "AAPL"
df = pd.read_csv(ticker + "_historical_closing_prices.csv", sep="\t", encoding='utf-8')
avg_df = pd.DataFrame(columns=["moving_average"])

period = 20
for i in range(math.floor(df.shape[0]/period)):
    avg = 0
    for j in range(period):
        avg += df["close"][i*period + j]/period

    avg_df.loc[i] = [avg]


slope_period = 1
slope_df = pd.DataFrame(columns=["slope"])
for i in range(1, df.shape[0]-1):
    m = df["close"][i+1] - df["close"][i-1]
    m /= 3
    slope_df.loc[i] = [m]


plt.subplot(3, 1, 1)
plt.scatter(avg_df.index, avg_df["moving_average"])
plt.subplot(3, 1, 2)
plt.scatter(df.index, df["close"])
plt.subplot(3, 1, 3)
plt.scatter(slope_df.index, slope_df["slope"])
plt.show()


