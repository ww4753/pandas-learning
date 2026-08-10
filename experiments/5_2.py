import pandas as pd
import numpy as np
from pandas import Series, DataFrame

#dfill,ffill
obj3 = pd.Series(["blue", "purple", "yellow"], index=[0, 2, 4])
print(obj3)
print(obj3.reindex(np.arange(6), method="bfill"))
print(obj3.reindex(np.arange(6), method="ffill"))

#sort_values怎么进行多列的排序
frame = pd.DataFrame({"b":[1, -3, 1, 1], "a":[1, 1, -2, 1]})
print(frame)
print(frame.sort_values(["b", "a"]))