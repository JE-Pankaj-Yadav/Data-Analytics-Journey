"""
===============================================================================
                         PANDAS DATA LOADING EXAMPLES
===============================================================================

Description:
------------
This file contains beginner-friendly examples of how to load, save, and inspect
CSV files using the Pandas library.

Topics Covered:
1. Creating a DataFrame
2. Saving DataFrame to CSV
3. Reading CSV files
4. Reading specific rows and columns
5. Skipping rows
6. Setting index columns
7. Changing headers
8. Assigning custom column names
9. Changing data types
10. Exploring and inspecting data
11. Converting DataFrame to NumPy arrays
12. Sorting rows and columns

This file acts as a practice notebook. Most examples are commented so that
you can uncomment and run one concept at a time.

===============================================================================
Prerequisites
===============================================================================

Install required libraries:

pip install pandas
pip install numpy

Or install both together:

pip install pandas numpy

===============================================================================
How to Run
===============================================================================

Open terminal and run:

python Pandas_Data_Loading.py

===============================================================================
Required Files
===============================================================================

This script uses:

Data.csv

Place Data.csv in the same folder as this Python file.

Example:

Project Folder
│
├── Pandas_Data_Loading.py
└── Data.csv

===============================================================================
Sample Input (Data.csv)
===============================================================================

Customer ID,Customer Name,Age,City
1,Pankaj,25,Gorakhpur
2,Ayush,24,Lucknow
3,Anmol,23,Delhi

===============================================================================
Expected Output (Current Active Code)
===============================================================================

The current active code sorts the DataFrame by row index in descending order.

Example Output:

   Customer ID Customer Name  Age       City
2            3         Anmol   23      Delhi
1            2         Ayush   24    Lucknow
0            1        Pankaj   25  Gorakhpur

===============================================================================
Code Review
===============================================================================

✓ Reviewed for errors and bad practices.

✓ Improvement Added:
  Added error handling while reading Data.csv.

✓ Improvement Added:
  Added comments explaining why each operation is used.

✓ Core logic and original learning examples remain unchanged.

===============================================================================
HOW THIS CODE WORKS
===============================================================================

Step 1:
    Import the required libraries:
        - pandas
        - numpy

Step 2:
    Create a DataFrame (optional examples).

Step 3:
    Save the DataFrame into CSV files (optional examples).

Step 4:
    Read data from Data.csv.

Step 5:
    Explore the dataset using functions like:
        - head()
        - tail()
        - describe()
        - columns
        - index

Step 6:
    Convert DataFrame into NumPy arrays if needed.

Step 7:
    Sort the data and print the final result.

Why are most examples commented?
--------------------------------
This file is designed as a learning notebook. Uncomment only the section you
want to practice so the output remains clean and easy to understand.

===============================================================================
"""

# =============================================================================
# IMPORT LIBRARIES
# =============================================================================

# Pandas is used for data analysis and handling tables.
import pandas as pd

# NumPy is used for numerical operations and arrays.
import numpy as np


# =============================================================================
# CREATE DATAFRAME
# =============================================================================

# Create a simple DataFrame from a dictionary.
#
# dic = {
#     'A': [1, 2, 3, 4, 5],
#     'B': [6, 7, 8, 9, 10]
# }
#
# data = pd.DataFrame(dic)
# print(data)


# =============================================================================
# SAVE DATAFRAME TO CSV FILE
# =============================================================================

# Save DataFrame with default index.
# data.to_csv('Test_data.csv')

# Save DataFrame without index.
# index=False prevents Pandas from writing row numbers into the CSV file.
# data.to_csv('Test_data1.csv', index=False)

# Save DataFrame with custom column names.
# data.to_csv(
#     'Test_data2.csv',
#     index=False,
#     header=['First Row', 'Second Row']
# )


# =============================================================================
# READ CSV FILE
# =============================================================================

# Read the entire CSV file.
# data = pd.read_csv('Data.csv')
# print(data)


# =============================================================================
# READ SPECIFIC NUMBER OF ROWS
# =============================================================================

# Read only the first row.
# nrows=1 means load only one row from the file.
# data = pd.read_csv('Data.csv', nrows=1)
# print(data)
# print(type(data))


# =============================================================================
# READ SPECIFIC COLUMNS USING COLUMN POSITION
# =============================================================================

# usecols=[0,1] means load only the first and second columns.
# data = pd.read_csv('Data.csv', usecols=[0, 1])
# print(data)


# =============================================================================
# READ SPECIFIC COLUMNS USING COLUMN NAMES
# =============================================================================

# data = pd.read_csv(
#     'Data.csv',
#     usecols=['Customer ID', 'Customer Name']
# )
# print(data)


# =============================================================================
# SKIP SPECIFIC ROWS
# =============================================================================

# skiprows=[0,1] skips row number 0 and row number 1.
# data = pd.read_csv('Data.csv', skiprows=[0, 1])
# print(data)


# =============================================================================
# SET A COLUMN AS INDEX
# =============================================================================

# The index is the row label in a DataFrame.
# data = pd.read_csv('Data.csv', index_col='Customer ID')
# print(data)


# =============================================================================
# CHANGE HEADER ROW
# =============================================================================

# header=5 means row number 5 will become column names.
# data = pd.read_csv('Data.csv', header=5)
# print(data)


# =============================================================================
# ASSIGN CUSTOM COLUMN NAMES
# =============================================================================

# names creates completely new column names.
#
# data = pd.read_csv(
#     'Data.csv',
#     names=[
#         'First Row',
#         'Second Row',
#         'Third Row',
#         'Fourth Row',
#         'Fifth Row',
#         'Sixth Row',
#         'Seventh Row',
#         'Eighth Row'
#     ]
# )
#
# print(data)


# =============================================================================
# REMOVE HEADER COMPLETELY
# =============================================================================

# header=None tells Pandas that the file does not contain column names.
# data = pd.read_csv('Data.csv', header=None)
# print(data)


# =============================================================================
# CHANGE DATA TYPES
# =============================================================================

# Convert Age column into float data type.
#
# data = pd.read_csv(
#     'Data.csv',
#     dtype={'Age': 'float'}
# )
#
# print(data)


# =============================================================================
# READ DATA FOR EXPLORATION
# =============================================================================

# Original code:
#
# data = pd.read_csv('Data.csv')
#
# Problem:
# --------
# If Data.csv is missing, the script crashes with FileNotFoundError.
#
# Fix:
# ----
# Added try-except block to show a beginner-friendly error message instead of
# stopping the program unexpectedly.

try:
    data = pd.read_csv('Data.csv')

    # =========================================================================
    # DATA INSPECTION EXAMPLES
    # =========================================================================

    # Print row indexes.
    # print(data.index)

    # Print column names.
    # print(data.columns)

    # Show statistical summary of numeric columns.
    # print(data.describe())

    # Show first 7 rows.
    # print(data.head(7))

    # Show last 3 rows.
    # print(data.tail(3))

    # Slice first 5 rows.
    # print(data[:5])

    # Slice rows from index 4 to 14.
    # print(data[4:15])

    # Return indexes as an array.
    # print(data.index.array)

    # Convert DataFrame to NumPy array.
    # print(data.to_numpy())

    # Another way to convert DataFrame into NumPy array.
    # print(np.asarray(data))

    # =========================================================================
    # SORTING DATA
    # =========================================================================

    # sort_index()
    # ------------
    # Sorts rows or columns using index labels.
    #
    # axis=0 -> Sort rows.
    # axis=1 -> Sort columns.
    #
    # ascending=False means descending order.
    print(data.sort_index(axis=0, ascending=False))

except FileNotFoundError:
    print(
        "Error: 'Data.csv' was not found.\n"
        "Please place Data.csv in the same folder as this script."
    )