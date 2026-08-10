import pandas as pd
import numpy as np
from pandas import Series, DataFrame

#2
stocks = pd.DataFrame(
    {
        "price": [100, 80, 120, 95],
        "return": [0.03, -0.01, 0.05, 0.02],
        "volume": [1000, 1500, 800, 1200]
    },
    index=["AAA", "BBB", "CCC", "DDD"]
)

benchmark = pd.Series(
    {
        "AAA": 0.01,
        "BBB": 0.00,
        "CCC": 0.02,
        "DDD": 0.01
    }
)

print(stocks)
print(benchmark)

#2.1
print(stocks["return"].sub(benchmark))

#2.2
value1 = stocks["return"].sub(benchmark)
stocks["excess_return"] = value1
print(stocks)

#2.3
print(stocks.sort_values(["excess_return"],ascending = False))

#2.4
value2 = stocks["return"].rank(method = "first",ascending = False)
print(value2)
stocks["return_rank"] = value2
print(stocks)

#2.5
print(stocks.loc[stocks["return_rank"] <= 2.0])

#2.6
def spread(x):
    return x.max() - x.min()
print(stocks.apply(spread,axis = "index"))


