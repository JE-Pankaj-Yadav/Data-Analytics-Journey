import pandas as pd

data=pd.read_csv("Data.csv")
print(data)

# Replace Function
# Method 1.
data=data.replace(to_replace='England', value='India')
# Method 2.
data=data.replace([0.00,00.00,0,0.0,00.0],1)

# Method 3.
# data=data.replace("[A-Za-z]",'Python',regex=True)
print(data)

