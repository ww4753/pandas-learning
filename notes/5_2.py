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
# 使用iloc，loc进行索引比[]更好
#避免链式索引

####################################################################5.2.4算术运算和数据对齐
#pandas的自动对齐
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=["a", "c", "d", "e"])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1],
               index=["a", "c", "e", "f", "g"])
print(s1 +s2)

df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list("bcd"),
                   index=["Ohio", "Texas", "Colorado"])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list("bde"),
                   index=["Utah", "Ohio", "Texas", "Oregon"])
print(df1 + df2)

#带有填充值的算术算法
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)),
                   columns=list("abcd"))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)),
                   columns=list("abcde"))
df2.loc[1, "b"] = np.nan
print(df1 + df2)
print(df1.add(df2, fill_value = 0))

#dataframe,series之间的运算
#常规运算
frame = pd.DataFrame(np.arange(12.).reshape((4, 3)),
                     columns=list("bde"),
                     index=["Utah", "Ohio", "Texas", "Oregon"])
series = frame.iloc[0]
print(frame - series)
series2 = pd.Series(np.arange(3), index=["b", "e", "f"])
series2
print(frame + series2)
#列运算
series3 = frame["d"]
print(frame.sub(series3, axis="index"))

##################################################################5.2.5函数应用和映射
frame = pd.DataFrame(np.random.standard_normal((4, 3)),
                     columns=list("bde"),
                     index=["Utah", "Ohio", "Texas", "Oregon"])
print(frame)
print(np.abs(frame))
def f1(x):
    return x.max() - x.min()
print(frame.apply(f1,axis ="index"))
print(frame.apply(f1,axis = "columns"))
#sum,mean本身是dataframe方法，不用apply

#apply不只是标量
def f2(x):
    return pd.Series([x.min(), x.max()], index=["min", "max"])
print(frame.apply(f2))

#元素级的python函数使用
def my_format(x):
    return f"{x:.2f}"
print(frame.applymap(my_format))

################################################################5.2.6排序和排名
#sort_index可以对行或列进行排序，默认行/列升序
#series
obj = pd.Series(np.arange(4), index=["d", "a", "b", "c"])
print(obj)
print(obj.sort_index())
#dataframe
frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
                     index=["three", "one"],
                     columns=["d", "a", "b", "c"])
print(frame)
print(frame.sort_index())
print(frame.sort_index(axis="columns"))
print(frame.sort_index(axis="columns", ascending=False))#ascending可以决定排序方式的升降
print(frame.sort_index(axis="columns", ascending=True))

#sort_values可以按值进行排列，默认值的升序
#series
obj = pd.Series([4, 7, -3, 2])
print(obj.sort_values())
obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])#缺失值默认放到series末尾
print(obj.sort_values())
print(obj.sort_values(na_position="first"))#na_position可以将缺失值放在最前面
#dataframe
frame = pd.DataFrame({"b": [4, 7, -3, 2], "a": [0, 1, 0, 1]})
print(frame)
print(frame.sort_values(["a", "b"]))#sort_values会优先进行第一个排序的对象
print(frame.sort_values(["b", "a"]))

#rank，为各组分配平均排名
obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
print(obj.rank())#value从小到大排列，7有两个，分别是第六大，第七大，（7+7）/2 = 6.5，然后这个值一一对应原来的value

print(obj.rank(method = "first"))#first是按排名顺序

print(obj.rank(ascending = False))#降序

frame = pd.DataFrame({"b": [4.3, 7, -3, 2], "a": [0, 1, 0, 1],
                      "c": [-2, 5, 8, -2.5]})
print(frame.rank(axis="columns"))#对dataframe的columns进行排列，取每一行进行排名
print(frame.rank(axis="index"))#对dataframe的index进行排列，取每一列进行排名
print(frame.rank(axis="index",method="min"))
print(frame.rank(axis="index",method="max"))
print(frame.rank(axis="index",method="dense"))

###############################################5.2.7带有重复标签的轴索引
#没啥东西，就是说可以有重复标签
df = pd.DataFrame(np.random.standard_normal((5, 3)),
                  index=["a", "a", "b", "b", "c"])
print(df.loc["b"])
print(df.loc["c"])
