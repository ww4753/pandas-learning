import pandas as pd
import numpy as np
from pandas import Series, DataFrame

############################################################5.2.1重建索引

#reindex可以创建一个按新索引重新排列的对象,一定注意是返回新对象，无论是series还是dataframe
obj = pd.Series([4.5, 7.2, -5.3, 3.6],index = ["d", "b", "a", "c"])
print(obj)
obj2 = obj.reindex(["a", "b", "c", "d", "e"])
print(obj2)

#dataframe格式的修改inedx和columns
frame = pd.DataFrame(np.arange(9).reshape((3, 3)),index = ["a", "c", "d"],columns =["Ohio", "Texas", "Califorina"])
print(frame)
frame5 = frame.loc[["a", "d", "c"],["Califorina", "Texas"]]#这个方法只适用于改变index，，columns的位置或删除，不能新增index，columns
print(frame5)
#index
frame2 = frame.reindex(["a", "b", "c", "d"])
print(frame2)
#columns
#1
states = ["Texas", "Utah", "California"]
frame3 = frame.reindex(columns=states)
print(frame3)
#2
frame4 = frame.reindex(states,axis = "columns")
print(frame4)

##################################################################5.2.2删除指定轴上的项
#drop能删除东西并返回新对象
obj = pd.Series(np.arange(5.), index=["a", "b", "c", "d", "e"])
print(obj)
new_obj = obj.drop("c")
print(new_obj)
new__obj = obj.drop(["d", "c"])
print(new__obj)
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=["Ohio", "Colorado", "Utah", "New York"],
                    columns=["one", "two", "three", "four"])
print(data)
data1 = data.drop(index = ["Colorado", "Ohio"])
print(data1)
data2 = data.drop(columns = ["two"])
print(data2)

######################################################################5.2.3索引、选取和过滤
