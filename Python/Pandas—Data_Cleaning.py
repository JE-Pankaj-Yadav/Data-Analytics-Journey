import pandas as pd

data=pd.read_csv("Data.csv")
# print(data)
# ========================================
# Dropna And Fillna
# ========================================
# print(data.dropna())
# print(data.dropna(axis=1))
# print(data.dropna(axis=0))
# print(data.dropna(how='any'))
# print(data.dropna(how='all'))
# print(data.dropna(subset='Job Classification'))
# print(data.dropna(inplace=True))
# print(data.dropna(thresh=1))


# print(data.fillna('Python'))
# print(data.fillna({'Customer Name':'Python','Region':'India'}))
# print(data.fillna(method='ffill'))
# print(data.fillna(method='bfill'))
# print(data.fillna(method='bfill',axis=1))
# print(data.fillna(12,inplace=True))
# print(data.fillna('python', limit=1))



# Replace Function
# Method 1.
# data=data.replace(to_replace='England', value='India')
# Method 2.
# data=data.replace([0.00,00.00,0,0.0,00.0],1)

# Method 3.
# data=data.replace("[A-Za-z]",'Python',regex=True)
# print(data)

# Method 4.
# data=data.replace({"Customer Name":"[A-Za-z]"},'Python',regex=True)
# print(data)

# print(data.replace(77.46, method='ffill'))
# print(data.replace(77.46, method='bfill'))
# print(data.replace(77.46, method='bfill', limit=3))
# print(data.replace(77.46, method='bfill', limit=3, inplace=True))

# print(data.interpolate())
# print(data.interpolate(method='linear'))
# print(data.interpolate(method='linear', axis=0))
# print(data.interpolate(limit=2))
# print(data.interpolate(limit_direction='forward',limit=2))
# print(data.interpolate(limit_direction='backward',limit=2))
# print(data.interpolate(limit_direction='both',limit=2))
# print(data.interpolate(limit_area='inside'))
# print(data.interpolate(limit_area='outside'))
