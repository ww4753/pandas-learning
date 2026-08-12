import pandas as pd
import numpy as np
from pandas import Series, DataFrame

df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
                   [np.nan, np.nan], [0.75, -1.3]],
                  index=["a", "b", "c", "d"],
                  columns=["one", "two"])
print(df)

print(df.sum)
print(df.sum(axis = "columns"))
print(df.sum(axis = "index",skipna = False))#skipna一般默认为True，其作用是跳过NaN值
print(df.mean(axis = "columns"))#mean的使用要求至少包含一个非NaN值

print(df.idxmax())#间接统计，找到最大值的索引，同理idxmin
print(df.idxmax(axis = "columns"))

print(df.cumsum())#累计

print(df.describe())#对于数值型能一次性生成多个汇总统计

obj = pd.Series(["a", "a", "b", "c"] * 4)
print(obj)
print(obj.describe())#对于非数值有另外一种汇总统计

##############################################################################5.3.1相关系数与协方差
price = pd.read_pickle(
    r"D:\量化学习\books\pydata-book-3rd-edition\examples\yahoo_price.pkl"
)

volume = pd.read_pickle(
    r"D:\量化学习\books\pydata-book-3rd-edition\examples\yahoo_volume.pkl"
)
print(price)
print(volume)

returns = price.pct_change()
print(returns.tail())
#corr计算相关系数
print(returns.corr())
print(returns["MSFT"].corr(returns["IBM"]))

#cov计算协方差
print(returns.cov())
print(returns["MSFT"].cov(returns["IBM"]))

#corrwith可以计算一个dataframe中的行或列与另一个series或dataframe之间的相关系数
print(returns.corrwith(returns["IBM"]))
print(returns.corrwith(volume))

####################################################################5.3.2唯一值，计数以及成员属性
#unique可以去掉重复的
obj = pd.Series(["c", "a", "d", "a", "a", "b", "b", "c", "c"])
print(obj.unique())

#value_counts计算数值出现频次
print(obj.value_counts())#默认是按频次从高到低排序即sort = True
print(pd.value_counts(obj.to_numpy(),sort = False))#先将obj转换为numpy形态；sort = False表示不规律排序

#isin可以执行向量化的成员检查，用于dataframe，series中一列的形式，将数据集过滤为子集
print(obj)
mask = obj.isin(["b", "c"])
print(mask)
print(obj[mask])

#Index.get_indexer
to_match = pd.Series(["c", "a", "b", "b", "c", "a"])
unique_values = to_match.unique()
print(unique_values)
indices = pd.Index(unique_values).get_indexer(to_match)
print(indices)

#
data = pd.DataFrame({"Qu1": [1, 3, 4, 3, 4],
                     "Qu2": [2, 3, 1, 2, 3],
                     "Qu3": [1, 5, 2, 4, 4]})
print(data)
print(data["Qu1"].value_counts().sort_index())
print(data.value_counts())#以每一行作为一个元组，看起出现的次数，（1，2，1），（3，3，5）...都是只出现过一次，所以均为一
print(data.apply(pd.value_counts).fillna(0))#apply(pd.value_counts)就是统计每一列出现的某个值的次数；fillna()是将空值填为括号里的值
