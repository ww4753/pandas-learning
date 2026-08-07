import pandas as pd
import numpy as np
from pandas import Series, DataFrame

obj3 = pd.Series(["blue", "purple", "yellow"], index=[0, 2, 4])
print(obj3)
print(obj3.reindex(np.arange(6), method="bfill"))
print(obj3.reindex(np.arange(6), method="ffill"))