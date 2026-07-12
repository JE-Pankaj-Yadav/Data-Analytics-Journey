"""
===============================================================================
                         PANDAS TRANSFORMATION EXAMPLES
===============================================================================

Description:
------------
This file contains beginner-friendly examples of different Pandas DataFrame
operations such as:

1. Merge
2. Concat
3. GroupBy
4. Join
5. Melt
6. Pivot / Pivot Table
7. Stack / Unstack
8. Apply
9. Map
10. DataFrame.map (Replacement for applymap)

The purpose of this file is to practice and understand how data transformation
works in Pandas.

Prerequisites:
--------------
Install Pandas using:

pip install pandas

How to Run:
-----------
Open terminal and run:

python Pandas_Transformation.py

No API keys, environment variables, or additional setup are required.

Sample Input:
-------------
No user input is required because the examples use hardcoded sample data.

Expected Output:
----------------
The final active example doubles every value in the DataFrame:

   Day      St_Name           eng  Math
0    2  PankajPankaj            24    28
1    4  HimanshuHimanshu        20    30
2    6  HimanshuHimanshu        26    32
3    8  AyushAyush            30    34
4   10  AyushAyush            32    38
5   12  PankajPankaj          28    36

Code Review:
------------
✓ The code was reviewed.
✓ One issue was found and fixed:
  - DataFrame.applymap() is deprecated in newer versions of Pandas.
  - Replaced it with DataFrame.map(), which performs the same task.

===============================================================================
HOW THIS CODE WORKS
===============================================================================

Step 1:
    Import the pandas library.

Step 2:
    Create sample DataFrames and Series.

Step 3:
    Uncomment any section you want to practice
    (Merge, Concat, GroupBy, etc.).

Step 4:
    The final active section demonstrates how to apply a function to every
    element of a DataFrame.

Step 5:
    The program prints the transformed DataFrame.

Note:
-----
Almost all examples are intentionally kept as comments so that you can
uncomment one section at a time and learn each concept separately.
===============================================================================
"""

import pandas as pd

# =============================================================================
# MERGE
# =============================================================================

# Merge combines two DataFrames based on one or more common columns.

# var1 = pd.DataFrame({'A': [1, 2, 3, 4, 5],
#                      'B': [6, 7, 8, 9, 10]})
#
# var2 = pd.DataFrame({'A': [1, 2, 3, 4, 5],
#                      'C': [16, 17, 18, 19, 20]})
#
# print(pd.merge(var1, var2, on='A'))

# Inner Merge (returns only matching rows)
# print(pd.merge(var1, var2, how='inner'))

# Left Merge (keeps all rows from left DataFrame)
# print(pd.merge(var1, var2, how='left'))

# Right Merge (keeps all rows from right DataFrame)
# print(pd.merge(var1, var2, how='right'))

# Outer Merge (keeps all rows from both DataFrames)
# print(pd.merge(var1, var2, how='outer'))

# Indicator shows where each row came from.
# print(pd.merge(var1, var2, how='outer', indicator=True))

# Merge using index instead of columns.
# print(pd.merge(var1, var2, left_index=True, right_index=True))

# Add suffixes when both DataFrames have same column names.
# print(pd.merge(var1, var2,
#                left_index=True,
#                right_index=True,
#                suffixes=('Name', 'Id')))


# =============================================================================
# CONCAT
# =============================================================================

# Concatenate Series vertically.
# sr1 = pd.Series([1, 2, 3, 4, 5])
# sr2 = pd.Series([6, 7, 8, 9, 10])
# print(pd.concat([sr1, sr2]))

# Concatenate DataFrames vertically.
# print(pd.concat([df1, df2]))

# Concatenate horizontally.
# print(pd.concat([df1, df2], axis=1))

# Inner Join during concatenation.
# print(pd.concat([df1, df2], axis=1, join='inner'))

# Add keys to create MultiIndex.
# print(pd.concat([df1, df2], keys=['d1', 'd2']))


# =============================================================================
# GROUPBY
# =============================================================================

# GroupBy is used to split data into groups and perform calculations.

# var = pd.DataFrame({
#     'Name': ['Pankaj', 'Anmol', 'Ayush', 'Anmol',
#              'Pankaj', 'Himanshu', 'Ayush', 'Himanshu'],
#     'Marks1': [25, 36, 45, 36, 95, 15, 25, 85],
#     'Marks2': [45, 65, 96, 36, 15, 45, 36, 25]
# })
#
# grouped = var.groupby('Name')
# print(grouped.mean())
# print(grouped.max())
# print(grouped.min())
# print(grouped.median())


# =============================================================================
# JOIN
# =============================================================================

# Join combines DataFrames using their indexes.

# var1 = pd.DataFrame(
#     {'A': [1, 2, 3], 'B': [4, 5, 6]},
#     index=['a', 'b', 'c']
# )
#
# var2 = pd.DataFrame(
#     {'C': [7, 8, 9], 'D': [10, 11, 12]},
#     index=['a', 'b', 'c']
# )
#
# print(var1.join(var2))


# =============================================================================
# MELT
# =============================================================================

# Melt converts wide-format data into long-format data.

# var1 = pd.DataFrame({
#     'Day': [1, 2, 3],
#     'Eng': [12, 15, 18],
#     'Math': [20, 25, 30]
# })
#
# print(pd.melt(var1))
# print(pd.melt(var1, id_vars=['Day']))
# print(pd.melt(var1,
#               id_vars=['Day'],
#               var_name='Subject',
#               value_name='Marks'))


# =============================================================================
# PIVOT
# =============================================================================

# Pivot converts long-format data back into wide-format.

# var1 = pd.DataFrame({
#     'Day': [1, 2, 3],
#     'Student': ['Pankaj', 'Ayush', 'Pankaj'],
#     'Marks': [90, 80, 95]
# })
#
# print(var1.pivot(index='Day',
#                  columns='Student',
#                  values='Marks'))


# =============================================================================
# STACK / UNSTACK
# =============================================================================

# Stack converts columns into rows.
# Unstack converts rows into columns.

# data = pd.read_csv('Data.csv', header=[0, 1], index_col=[0])
# print(data.stack())
# print(data.unstack())


# =============================================================================
# APPLY
# =============================================================================

# Apply is generally used on rows or columns.

# var1['Total'] = var1[['Eng', 'Math']].apply(sum, axis=1)
# print(var1[['Eng', 'Math']].apply(lambda x: x + 5))
# print(var1['Student'].apply(str.upper))


# =============================================================================
# MAP
# =============================================================================

# map() is generally used on a Series (single column).

var1 = pd.DataFrame({
    'Day': [1, 2, 3, 4, 5, 6],
    'St_Name': [
        'Pankaj',
        'Himanshu',
        'Himanshu',
        'Ayush',
        'Ayush',
        'Pankaj'
    ],
    'eng': [12, 10, 13, 15, 16, 14],
    'Math': [14, 15, 16, 17, 19, 18]
})

# Convert names to uppercase.
# print(var1['St_Name'].map(str.upper))

# Add bonus marks.
# var1['Bonus'] = var1['eng'].map(lambda x: x + 5)

# Pass or Fail example.
# print(var1['eng'].map(lambda x: 'Pass' if x >= 13 else 'Fail'))


# =============================================================================
# DATAFRAME.MAP (Replacement for applymap)
# =============================================================================

# Previous code:
# print(var1.applymap(lambda x: x * 2))
#
# Problem:
# --------
# DataFrame.applymap() is deprecated in newer versions of Pandas and may
# show a FutureWarning.
#
# Fix:
# ----
# Replaced applymap() with DataFrame.map(), which performs element-wise
# operations on every value in the DataFrame.

# Multiply every element by 2.
# Numbers become doubled and strings are repeated twice.

print(var1.map(lambda x: x * 2))