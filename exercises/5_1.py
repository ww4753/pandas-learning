import pandas as pd
import numpy as np
from pandas import Series, DataFrame

prices = pd.Series([10.5, 20.8, 15.2, 30.0],index = ["AAA", "BBB","CCC", "DDD"])
prices.name = "close"
prices.index.name = "stock"
print(prices)
print(prices.values)
print(prices.index)

print(prices.loc["CCC"])#要求按标签取出
print(prices.iloc[2])#要求按位置取出
prices.loc[["DDD", "AAA"]]#标签列表能满足条件
print(prices.iloc[0:2])#标签列表能满足条件
print(prices.loc[prices > 18])#布尔进行筛选

market = pd.DataFrame({
    "close": [10.5, 20.8, 15.2, 30.0],
    "daily_return": [0.02, -0.01, 0.03, -0.04],
    "volume": [1000, 2500, 1800, 3200]
}, index=["AAA", "BBB", "CCC", "DDD"])

market.index.name = "stock"
market.columns.name = "indicator"

print(market)
print(market.loc["BBB"])
print(market.loc["CCC", "volume"])
print(market["daily_return"])
print(market[["daily_return"]])
print(market.iloc[1:4,:])
print(market.iloc[0:3,0:2])

print(market.loc[market["daily_return"] > 0])
print(market.loc[market["close"] > 15])
print(market.loc[(market["daily_return"] > 0) & (market["volume"] > 1500)])#（condition1) & (condition2)重要语法
print(market.loc[(market["daily_return"] > 0) & (market["volume"] > 1500),["close","daily_return"]])
print(market.loc[market["daily_return"] < 0,["daily_return"]])#返回dataframe
print(market.loc[market["daily_return"] < 0,"daily_return"])#返回series

position = pd.Series(
    [100, 200, 300],
    index=["AAA", "BBB", "CCC"],
    name="position"
)

price_change = pd.Series(
    [0.5, -0.2, 1.0],
    index=["BBB", "CCC", "DDD"],
    name="price_change"
)
print(position)
print(price_change)

print(position * price_change)

trades = pd.Series(
    [100, 200, 150],
    index=["AAA", "AAA", "BBB"]
)

print(trades)
print(trades["AAA"])
print(trades[["AAA"]])
print(trades.index.is_unique)

val1 = market.loc[market["daily_return"] > 0]
positive_stocks = pd.DataFrame(val1,columns = ["close", "daily_return", "return_percent"])
positive_stocks.columns.name = "indicator"
val2 = market["daily_return"] * 100
positive_stocks["return_percent"] = val2
print(positive_stocks)#更优写法如下

# positive_stocks = market.loc[market["daily_return"] > 0,
# ["close", "daily_return"]].copy()
# positive_stocks["return_percent"] = (positive_stocks["daily_return"] * 100)
# print(positive_stocks)


stocks = pd.DataFrame(
    {
        "prev_close": [10.0, 20.5, 15.0, 30.0, 8.0],
        "close": [10.5, 20.0, 15.6, 28.8, 8.4],
        "volume": [1200, 3000, 1800, 4500, 900]
    },
    index=["AAA", "BBB", "CCC", "DDD", "EEE"]
)

stocks.index.name = "stock"
stocks.columns.name = "indicator"

stocks["daily_return"] = (stocks["close"] - stocks["prev_close"]) / stocks["prev_close"]
stocks["return_percent"] = stocks["daily_return"] * 100
print(stocks)
#任务二
gainers = stocks.loc[stocks["daily_return"] > 0,["close", "daily_return", "volume"]]
print(gainers)
losers = stocks.loc[stocks["daily_return"] < 0,["close", "daily_return", "volume"]]
print(losers)
active_gainers = stocks.loc[(stocks["daily_return"] > 0) & (stocks["volume"] > 1500),["close", "daily_return", "volume"]]
print(active_gainers)
#任务三
print(stocks.loc[stocks["daily_return"] > 0].index)
print(stocks.loc[stocks["daily_return"] < 0].index)
print(stocks["daily_return"].idxmax())
print(stocks["daily_return"].idxmin())
print(stocks["volume"].idxmax())
print(stocks.loc[(stocks["daily_return"] > 0) & (stocks["volume"] > 1500)].index)
