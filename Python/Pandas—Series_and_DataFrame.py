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

# --------------------------------------------
# Airthmetic Operations
# --------------------------------------------

# var=pd.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,10]})
# var['C']=var['A']+var['B']
# print(var)

# sub=pd.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,10]})
# sub['C']=sub['A']-sub['B']
# print(sub)


# mul=pd.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,10]})
# mul['C']=mul['A']*mul['B']
# print(mul)

# div=pd.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,10]})
# div['C']=div['A']/div['B']
# print(div)

# num=pd.DataFrame({'A':[11,12,13,14,15],'B':[16,17,18,19,110]})
# num['Data_A']=num['A']<=14
# num['Data_B']=num['B']>=18
# print(num)

# --------------------------------------------------------------
# Insert And Delete Data in Pandas
# --------------------------------------------------------------

# Var=pd.DataFrame({'A':[11,12,13,14,15],'B':[16,17,18,19,110]})
# Var.insert(1,'B1',Var['A']+2)
# print(Var)

# Var=pd.DataFrame({'A':[11,12,13,14,15],'B':[16,17,18,19,110]})
# Var.insert(1,'B1',[1,2,3,4,5])
# print(Var)

# Var=pd.DataFrame({'A':[11,12,13,14,15],'B':[16,17,18,19,110]})
# Var.insert(2,'Python',Var['A'][:3])
# print(Var)

# Var=pd.DataFrame({'A':[11,12,13,14,15],'B':[16,17,18,19,110],'C':[11,22,33,44,55]})
# Var1=Var.pop('B')
# print(Var1)
# print(Var)

# Var=pd.DataFrame({'A':[11,12,13,14,15],'B':[16,17,18,19,110],'C':[11,22,33,44,55]})
# del Var['C']
# print(Var)

# ===================================
# loc vs iloc
# ===================================
data=pd.read_csv('Data.csv')
# data.loc[0,'Region']='India'
# print(data)


# print(data.loc[[2,3],['Customer Name','Gender']])
# print(data.loc[:,['Customer Name','Gender']])
# print(data.loc[[2,3],:])

# print(data.iloc[2,3])

# print(data.drop('Age',axis=1))
print(data.drop(0,axis=0))