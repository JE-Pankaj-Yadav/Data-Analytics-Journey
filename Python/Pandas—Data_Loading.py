# ====================================================
# Python Pandas CSV File.
# ====================================================
import pandas as pd
import numpy as np

# dic={'A':[1,2,3,4,5],'B':[6,7,8,9,10]}
# data=pd.DataFrame(dic)
# print(data)

# data.to_csv('Test_data.csv')
# data.to_csv('Test_data1.csv',index=False)
# data.to_csv('Test_data2.csv',index=False, header=['First Row', 'Second Row'])

# data=pd.read_csv('Data.csv')
# print(data)

# data=pd.read_csv('Data.csv', nrows=1)
# print(data)
# print(type(data))

# data=pd.read_csv('Data.csv', usecols=[0,1])
# print(data)
# print(type(data))

# data=pd.read_csv('Data.csv', usecols=['Customer ID','Customer Name'])
# print(data)
# print(type(data))

# data=pd.read_csv('Data.csv', skiprows=[0,1])
# print(data)
# print(type(data))

# data=pd.read_csv('Data.csv', index_col='Customer ID')
# print(data)
# print(type(data))

# data=pd.read_csv('Data.csv',header=5)
# print(data)
# print(type(data))

# data=pd.read_csv('Data.csv',names=['First Row', 'Second Row','Third Row','Fourth Row','Fiveth Row','Sixth Row','Seventh Row','Eight Row'])
# print(data)
# print(type(data))

# data=pd.read_csv('Data.csv',header=None)
# print(data)
# print(type(data))

# data=pd.read_csv('Data.csv',dtype={'Age':'float'})
# print(data)
# print(type(data))

data=pd.read_csv('Data.csv')
# print(data.index)
# print(data.columns)
# print(data.describe())
# print(data.head(7))
# print(data.tail(3))
# print(data[:5])
# print(data[4:15])
# print(data.index.array)
# print(data.to_numpy())
# print(np.asarray(data))
print(data.sort_index(axis=0,ascending=False))