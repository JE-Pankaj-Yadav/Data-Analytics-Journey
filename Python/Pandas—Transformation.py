import pandas as pd

# ===============================================
# Merge
# ===============================================

# var1=pd.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,10]})
# var2=pd.DataFrame({'A':[1,2,3,4,5],'C':[16,17,18,19,20]})
# print(pd.merge(var1,var2,on='A'))

# var1=pd.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,10]})
# var2=pd.DataFrame({'A':[1,2,3,4,6],'C':[16,17,18,19,20]})
# print(pd.merge(var1,var2,on='A'))

# var1=pd.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,10]})
# var2=pd.DataFrame({'A':[1,2,3,4,6],'C':[16,17,18,19,20]})
# print(pd.merge(var1,var2,how='inner'))

# var1=pd.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,10]})
# var2=pd.DataFrame({'A':[1,2,3,4,6],'C':[16,17,18,19,20]})
# print(pd.merge(var1,var2,how='left'))

# var1=pd.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,10]})
# var2=pd.DataFrame({'A':[1,2,3,4,6],'C':[16,17,18,19,20]})
# print(pd.merge(var1,var2,how='right'))

# var1=pd.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,10]})
# var2=pd.DataFrame({'A':[1,2,3,4,6],'C':[16,17,18,19,20]})
# print(pd.merge(var1,var2,how='outer'))

# var1=pd.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,10]})
# var2=pd.DataFrame({'A':[1,2,3,4,6],'C':[16,17,18,19,20]})
# print(pd.merge(var1,var2,how='outer', indicator=True))

# var1=pd.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,10]})
# var2=pd.DataFrame({'A':[1,2,3,4,6],'C':[16,17,18,19,20]})
# print(pd.merge(var1,var2,left_index=True, right_index=True))

# var1=pd.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,10]})
# var2=pd.DataFrame({'A':[1,2,3,4,6],'C':[16,17,18,19,20]})
# print(pd.merge(var1,var2,left_index=True, right_index=True, suffixes=('Name','Id')))

# ========================================================
# Concat
# ========================================================
# sr1=pd.Series([1,2,3,4,5,6,7,8,9,10])
# sr2=pd.Series([11,12,13,14,15,16,17,18,19])
# print(pd.concat([sr1,sr2]))


# sr1=pd.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,10]})
# sr2=pd.DataFrame({'A':[1,2,3,4,5],'B':[16,17,18,19,20]})
# print(pd.concat([sr1,sr2]))

# sr1=pd.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,10]})
# sr2=pd.DataFrame({'A':[1,2,3],'B':[16,17,18]})
# print(pd.concat([sr1,sr2],axis=1, join='inner'))

# sr1=pd.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,10]})
# sr2=pd.DataFrame({'A':[1,2,3],'B':[16,17,18]})
# print(pd.concat([sr1,sr2],axis=1, join='outer'))

# sr1=pd.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,10]})
# sr2=pd.DataFrame({'A':[1,2,3],'B':[16,17,18]})
# print(pd.concat([sr1,sr2],axis=1, keys=['di','d2']))

sr1=pd.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,10]})
sr2=pd.DataFrame({'A':[1,2,3],'B':[16,17,18]})
print(pd.concat([sr1,sr2],axis=0, keys=['di','d2']))