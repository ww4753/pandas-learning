import pandas as pd
import numpy as np
from pandas import Series, DataFrame

#pandas允许对象不完整，使用NaN表示缺失

#Index不可变，但允许存在重复标签

#Series不是简单的“一列DataFrame”
#Series是一维带标签数据结构
#DataFrame是二维带行列标签的数据结构

#[""]叫标签列表



###############################5.1.1 Series
#obj = pd.Series([    ], index = ['这是索引列表，里面是字符串’'可以通过赋值的方式修改index'])

#字典可以直接传入，pandas会自动把字典的key作为索引，value作为数据
sadata = {"Ohio":35000, "Texas":71000, "Oregon":16000, "Utah":5000}
obj = pd.Series(sadata)
print(obj)
#to_dict可以将Series转换为字典
print(obj.to_dict())

#pandas的isnull和notnull函数可以用于检测数据
print(pd.isna(obj))
print(pd.notna(obj))

###############################5.1.2 DataFrame
#DataFrame可以用字典生成。key作为column，value作为数据
data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)

#head,tail在特别大的DataFrame中可以分别查看前五行和后五行
frame.head()
frame.tail()

#column
#frame = pd.DataFrame(data,columns)是格式
#frame[column]可以用来索引某一列,也是最稳妥的办法。frame.column可以用来索引，但是要求column是合理的python变量名

#loc和iloc
#frame.loc[行标签, 列标签]（行标签和列标签都是字符串）
#frame.iloc[行位置, 列位置]（行位置和列位置都是整数）
#iloc 的切片右侧不包含；loc 的标签切片右侧包含

#DataFramede赋值与删除
frame["eastern"] = frame["state"] == "Ohio"
print(frame)
del frame["eastern"]
print(frame)
#通过索引方式从DataFrame返回的列是底层数据的视图，并不是副本。因此，对返回的Series所作的任何修改全部会反映到DataFrame上。。应当通过Series的copy方法来复制列。

#如果是嵌套字典作为DataFrame的value,外层字典的key为列，内层字典的key为索引
populations = {"Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6},
               "Nevada": {2001: 2.4, 2002: 2.9}}
frame3 = pd.DataFrame(populations)
print(frame3)

#DataFrame的转置，即DataFrame.T，会转换index和columns

#to_numpy()方法可以将DataFrame转换为一个二维数组
print(frame3.to_numpy())

###########################5.1.3索引对象
#index对象不可变
