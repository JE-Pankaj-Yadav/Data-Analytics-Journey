import pandas as pd

# -----------------------------------------
# Series
# -----------------------------------------

# x=[2,3,4,5,6,7,8,9]
# var=pd.Series(x)
# print(var)
# print(type(var))
# print(var[2])

# x=[2,3,4,5,6,7,8,9]
# var=pd.Series(x, index=['a','b','c','d','e','f','g','h'],dtype='float',name='Python')
# print(var)
# print(type(var))
# print(var['e'])

# dic={'Name':['Pankaj Yadav','Himanshu Yadav','Anmol Yadav','Ayush Yadav'],'Rank':[1,2,3,4],'Postion':['Saram','Gorakhpur','Gkp','Saram']}
# print(pd.Series(dic),type(dic))

# S=pd.Series(12, index=[1,2,3,4,5,6])
# print(S)
# print(type(S))

# S1=pd.Series(12, index=[1,2,3,4,5,6])
# S2=pd.Series(12, index=[1,2,3])
# print(S1+S2)

# -----------------------------------------
# DATAFRAME
# -----------------------------------------
# x=[2,3,4,5,6,7,8,9]
# var=pd.DataFrame(x)
# print(var, type(var))

# dic={'a':[1,2,3,4,5],'b':[1,2,3,4,5],1:[1,2,3,4,5]}
# var=pd.DataFrame(dic)
# print(var)

# dic={'a':[1,2,3,4,5],'b':[1,2,3,4,5],1:[1,2,3,4,5]}
# var=pd.DataFrame(dic,columns=['a',1])
# print(var)

# dic={'a':[1,2,3,4,5],'b':[1,2,3,4,5],1:[1,2,3,4,5]}
# var=pd.DataFrame(dic,columns=['a',1], index=[5,6,7,8,9])
# print(var)

# dic={'a':[1,2,3,4,5],'b':[1,2,3,4,5],1:[1,2,3,4,5]}
# var=pd.DataFrame(dic,columns=['a',1], index=[5,6,7,8,9])
# print(var['a'][7])

# list_1=[[1,2,3,4,5],[6,7,8,9,10]]
# print(pd.DataFrame(list_1))

# sr={'s':pd.Series([1,2,3,4,5]),'a':pd.Series([4,5,6,7,8])}
# print(pd.DataFrame(sr))