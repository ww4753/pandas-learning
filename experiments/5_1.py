import pandas as pd
import numpy as np
from pandas import Series, DataFrame

#非字典创建的series能不能用to_dict转换为字典
obj = pd.Series([4,7,5,-3])
obj1 = obj.to_dict()
print(obj1)

#Series的赋值，不匹配与匹配的情况
data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame2 = pd.DataFrame(data, columns=["year", "state", "pop", "debt"])
frame2["debt"] = np.arange(6)
print(frame2)
val = pd.Series([-1.2, -1.5, -1.7], index=[2, 4, 5])
frame2["debt"] = val
print(frame2)
val1 = pd.Series([-1.2, -1.5, -1.7, 1.6, 1.9, 2.0], index=[0, 1, 2, 3, 4, 5])
frame2["debt"] = val1
print(frame2)