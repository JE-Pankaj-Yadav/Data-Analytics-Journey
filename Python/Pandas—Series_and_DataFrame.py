"""
===============================================================================
                     PANDAS SERIES AND DATAFRAME EXAMPLES
===============================================================================

Description:
------------
This Python script contains beginner-friendly examples of working with:

1. Pandas Series
2. Pandas DataFrames
3. Arithmetic Operations on DataFrames
4. Insert and Delete Operations
5. loc[] and iloc[] Indexing
6. Reading CSV Files
7. Dropping Rows and Columns

This file is designed as a practice notebook/script where you can uncomment
different sections one by one and learn Pandas concepts.

-------------------------------------------------------------------------------
Prerequisites:
-------------------------------------------------------------------------------
Install Pandas:

    pip install pandas

-------------------------------------------------------------------------------
How to Run:
-------------------------------------------------------------------------------
Open your terminal and run:

    python Pandas_Series_and_DataFrame.py

-------------------------------------------------------------------------------
Required Files:
-------------------------------------------------------------------------------
This script reads:

    Data.csv

Make sure Data.csv exists in the same folder as this Python file.

Folder Structure Example:

Project/
│
├── Pandas_Series_and_DataFrame.py
└── Data.csv

-------------------------------------------------------------------------------
Sample Input:
-------------------------------------------------------------------------------
Data.csv

Customer Name,Gender,Age,Region
Pankaj,Male,25,Gorakhpur
Ayush,Male,24,Lucknow
Anmol,Male,23,Delhi

-------------------------------------------------------------------------------
Expected Output (Current Active Code):
-------------------------------------------------------------------------------
The last line of this script removes the first row (index 0) from Data.csv
and prints the remaining rows.

-------------------------------------------------------------------------------
Code Review:
-------------------------------------------------------------------------------
✓ Reviewed for errors and bad practices.

✓ Improvement Added:
  Added error handling while reading Data.csv because the original code would
  crash if the CSV file was missing.

✓ No changes were made to the learning examples or original intent of the code.

===============================================================================
HOW THIS CODE WORKS
===============================================================================

Step 1:
    Import the pandas library.

Step 2:
    The script contains many examples, but almost all of them are commented.
    Uncomment one section at a time to practice a specific topic.

Step 3:
    The active section reads a CSV file called Data.csv.

Step 4:
    Different examples show how to:
        - Create Series
        - Create DataFrames
        - Perform calculations
        - Insert and delete columns
        - Access rows and columns
        - Remove rows and columns

Step 5:
    The final active code removes the first row from the DataFrame and prints
    the remaining data.

Why are most examples commented?
--------------------------------
This file acts like a personal learning notebook. Keeping examples commented
allows you to practice one concept at a time without executing everything.

===============================================================================
"""

# Import the Pandas library.
# Pandas is used for working with tables (DataFrames) and columns (Series).
import pandas as pd


# =============================================================================
# SERIES
# =============================================================================

# A Series is a one-dimensional data structure in Pandas.
# Think of it as a single column in an Excel sheet.

# Example 1: Create a simple Series.
# x = [2, 3, 4, 5, 6, 7, 8, 9]
# var = pd.Series(x)
# print(var)
# print(type(var))
# print(var[2])

# Example 2: Create a Series with custom indexes.
# x = [2, 3, 4, 5, 6, 7, 8, 9]
# var = pd.Series(
#     x,
#     index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
#     dtype='float',
#     name='Python'
# )
# print(var)
# print(type(var))
# print(var['e'])

# Example 3: Create a Series from a dictionary.
# dic = {
#     'Name': ['Pankaj Yadav', 'Himanshu Yadav',
#              'Anmol Yadav', 'Ayush Yadav'],
#     'Rank': [1, 2, 3, 4],
#     'Position': ['Saram', 'Gorakhpur', 'Gkp', 'Saram']
# }
# print(pd.Series(dic))
# print(type(dic))

# Example 4: Create a Series with one repeated value.
# S = pd.Series(12, index=[1, 2, 3, 4, 5, 6])
# print(S)

# Example 5: Add two Series together.
# Pandas automatically matches indexes.
# S1 = pd.Series(12, index=[1, 2, 3, 4, 5, 6])
# S2 = pd.Series(12, index=[1, 2, 3])
# print(S1 + S2)


# =============================================================================
# DATAFRAME
# =============================================================================

# A DataFrame is a two-dimensional table made up of rows and columns.

# Example 1: Create a DataFrame from a list.
# x = [2, 3, 4, 5, 6, 7, 8, 9]
# var = pd.DataFrame(x)
# print(var)
# print(type(var))

# Example 2: Create a DataFrame from a dictionary.
# dic = {
#     'a': [1, 2, 3, 4, 5],
#     'b': [1, 2, 3, 4, 5],
#     1: [1, 2, 3, 4, 5]
# }
# var = pd.DataFrame(dic)
# print(var)

# Example 3: Select only specific columns.
# var = pd.DataFrame(dic, columns=['a', 1])
# print(var)

# Example 4: Use custom indexes.
# var = pd.DataFrame(
#     dic,
#     columns=['a', 1],
#     index=[5, 6, 7, 8, 9]
# )
# print(var)

# Example 5: Access a specific value.
# print(var['a'][7])

# Example 6: Create DataFrame from nested lists.
# list_1 = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10]
# ]
# print(pd.DataFrame(list_1))

# Example 7: Create DataFrame from Series.
# sr = {
#     's': pd.Series([1, 2, 3, 4, 5]),
#     'a': pd.Series([4, 5, 6, 7, 8])
# }
# print(pd.DataFrame(sr))


# =============================================================================
# ARITHMETIC OPERATIONS
# =============================================================================

# Addition
# var = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5],
#     'B': [6, 7, 8, 9, 10]
# })
# var['C'] = var['A'] + var['B']
# print(var)

# Subtraction
# sub['C'] = sub['A'] - sub['B']

# Multiplication
# mul['C'] = mul['A'] * mul['B']

# Division
# div['C'] = div['A'] / div['B']

# Comparison Operations
# num = pd.DataFrame({
#     'A': [11, 12, 13, 14, 15],
#     'B': [16, 17, 18, 19, 110]
# })
#
# num['Data_A'] = num['A'] <= 14
# num['Data_B'] = num['B'] >= 18
# print(num)


# =============================================================================
# INSERT AND DELETE DATA
# =============================================================================

# Insert a new column.
# Var.insert(1, 'B1', Var['A'] + 2)

# Insert a list as a new column.
# Var.insert(1, 'B1', [1, 2, 3, 4, 5])

# Insert partial data.
# Var.insert(2, 'Python', Var['A'][:3])

# Remove a column using pop().
# removed_column = Var.pop('B')

# Remove a column using del.
# del Var['C']


# =============================================================================
# LOC VS ILOC
# =============================================================================

# loc[]
# -----
# Access data using labels (row names and column names).

# iloc[]
# ------
# Access data using integer positions (row number and column number).


# =============================================================================
# READ CSV FILE
# =============================================================================

# Original code:
# data = pd.read_csv('Data.csv')
#
# Problem:
# --------
# If Data.csv does not exist, the program crashes with:
# FileNotFoundError.
#
# Fix:
# ----
# Added try-except so the program shows a friendly message instead
# of crashing.

try:
    data = pd.read_csv('Data.csv')

    # Change a value using loc.
    # data.loc[0, 'Region'] = 'India'

    # Select specific rows and columns.
    # print(data.loc[[2, 3], ['Customer Name', 'Gender']])

    # Select all rows and specific columns.
    # print(data.loc[:, ['Customer Name', 'Gender']])

    # Select specific rows and all columns.
    # print(data.loc[[2, 3], :])

    # Select a value using row and column positions.
    # print(data.iloc[2, 3])

    # Drop a column.
    # axis=1 means columns.
    # print(data.drop('Age', axis=1))

    # Drop a row.
    # axis=0 means rows.
    # This removes the row having index 0.
    print(data.drop(0, axis=0))

except FileNotFoundError:
    print(
        "Error: 'Data.csv' was not found.\n"
        "Please place Data.csv in the same folder as this script."
    )