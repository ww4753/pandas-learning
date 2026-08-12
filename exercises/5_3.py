import pandas as pd
import numpy as np

returns = pd.DataFrame(
    {
        "AAA": [0.02, -0.01, 0.03, 0.00, 0.01],
        "BBB": [0.01,  0.02, -0.01, 0.04, 0.00],
        "CCC": [-0.02, 0.01, 0.02, 0.01, 0.03],
    },
    index=["Mon", "Tue", "Wed", "Thu", "Fri"]
)
print(returns)
#1
print(returns.mean())
print(returns.std())
print(returns.max())
print(returns.min())
#2
print(returns["AAA"].idxmax())
print(returns["BBB"].idxmax())
print(returns["CCC"].idxmax())
print(returns.idxmax())
#3
print(returns.mean(axis = "columns"))
#4
print(returns.cumsum())
print(returns.sum())
print("nihao")
print(returns.cumsum().iloc[-1])
#5
print(returns.corr())
#6 
signals = pd.DataFrame({
    "AAA": ["buy", "hold", "buy", "sell", "buy"],
    "BBB": ["hold", "buy", "buy", "hold", "sell"],
    "CCC": ["sell", "hold", "buy", "buy", "buy"]
})
print(signals)
print(signals.apply(pd.value_counts))
#7 错题
signals_bool = signals["AAA"].isin(["buy","sell"]) 
print(signals_bool)
signals.index = returns.index
buy_bool = signals["AAA"].isin(["buy"])
print(returns.loc[buy_bool, "AAA"])

#8
print(returns.describe())

best_day = returns.mean(axis=1).idxmax()
print(best_day)