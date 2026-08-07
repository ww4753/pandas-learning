import pandas as pd
import numpy as np
from pandas import Series, DataFrame

returns = pd.DataFrame(
    {
        "AAPL": [0.012, -0.008, 0.021, -0.004, 0.015],
        "MSFT": [0.006, 0.011, -0.005, 0.018, 0.009],
        "NVDA": [0.025, -0.020, 0.031, 0.008, -0.012],
    },
    index=["Mon", "Tue", "Wed", "Thu", "Fri"]
)
print(returns)

returns1 = returns.drop(columns = ["MSFT"])
print(returns1)

print(returns.loc[returns["AAPL"] > 0.01])

print(returns.loc[returns["NVDA"] < 0,["AAPL", "NVDA"]])

clean_returns = returns.drop(columns = ["MSFT"],index = ["Fri"])

a = returns.reindex(["Mon", "Wed", "Fri1"])
print(a)
b = returns.loc[["Mon", "Wed", "Fri1"]]
print(b)