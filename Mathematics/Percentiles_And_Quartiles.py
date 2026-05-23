# ============================================================
#          Percentiles and Quartiles in Python
# ============================================================
#
# Topics Covered:
#
# 1. Percentiles
# 2. Quartiles
# 3. Boxen Plot Visualization
# 4. Dataset Summary using describe()
#
# Libraries Used:
# - NumPy      -> Mathematical calculations
# - Pandas     -> Data handling
# - Matplotlib -> Data visualization
# - Seaborn    -> Beautiful graphs
#
# Dataset File:
# Make sure "Data.csv" is in the same folder
# as this Python file.
#
# ============================================================


# =========================
# Import Required Libraries
# =========================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# =========================
# Load Dataset
# =========================

# Read CSV file
dataset = pd.read_csv("Data.csv")

# Display first 5 rows
print("\n========== FIRST 5 ROWS OF DATASET ==========\n")
print(dataset.head())


# ============================================================
#                 CHECK MISSING VALUES
# ============================================================

print("\n========== MISSING VALUES ==========\n")

# Check null values in each column
print(dataset.isnull().sum())

# Explanation:
# Missing values can affect calculations.
# So, checking null values is important.


# ============================================================
#                     PERCENTILES
# ============================================================
#
# Percentile means:
# The value below which a percentage of data falls.
#
# Example:
# 50th percentile = Median
#
# ============================================================

print("\n========== PERCENTILES ==========\n")

# 100th Percentile -> Maximum Value
percentile_100 = np.percentile(dataset["Age"], 100)

# 50th Percentile -> Median
percentile_50 = np.percentile(dataset["Age"], 50)

# 1st Percentile
percentile_1 = np.percentile(dataset["Age"], 1)

# 25th Percentile -> First Quartile (Q1)
percentile_25 = np.percentile(dataset["Age"], 25)

# 75th Percentile -> Third Quartile (Q3)
percentile_75 = np.percentile(dataset["Age"], 75)

# Print Results
print("100th Percentile :", percentile_100)
print("50th Percentile  :", percentile_50)
print("1st Percentile   :", percentile_1)
print("25th Percentile  :", percentile_25)
print("75th Percentile  :", percentile_75)


# ============================================================
#                     QUARTILES
# ============================================================
#
# Quartiles divide data into 4 equal parts.
#
# Q1 -> 25%
# Q2 -> 50% (Median)
# Q3 -> 75%
#
# ============================================================

print("\n========== QUARTILES ==========\n")

# Calculate Quartiles
Q1 = dataset["Age"].quantile(0.25)
Q2 = dataset["Age"].quantile(0.50)
Q3 = dataset["Age"].quantile(0.75)

# Interquartile Range (IQR)
IQR = Q3 - Q1

# Print Quartiles
print("First Quartile (Q1)  :", Q1)
print("Second Quartile (Q2) :", Q2)
print("Third Quartile (Q3)  :", Q3)

print("\nInterquartile Range (IQR):", IQR)

# Explanation:
# IQR measures the spread of middle 50% data.


# ============================================================
#                 MINIMUM AND MAXIMUM VALUES
# ============================================================

print("\n========== MINIMUM AND MAXIMUM ==========\n")

# Minimum Age
minimum_age = dataset["Age"].min()

# Maximum Age
maximum_age = dataset["Age"].max()

# Median Age
median_age = dataset["Age"].median()

# Print Results
print("Minimum Age :", minimum_age)
print("Median Age  :", median_age)
print("Maximum Age :", maximum_age)


# ============================================================
#                  DATASET SUMMARY
# ============================================================

print("\n========== DATASET SUMMARY ==========\n")

# describe() gives:
# count, mean, std, min, max,
# quartiles and other statistics

print(dataset.describe())


# ============================================================
#                BOXEN PLOT FOR AGE
# ============================================================

# Create graph size
plt.figure(figsize=(10, 6))

# Create boxen plot
sns.boxenplot(
    x="Age",
    data=dataset
)

# Add title
plt.title("Boxen Plot of Age")

# Add label
plt.xlabel("Age")

# Show graph
plt.show()

# Explanation:
# Boxen plot helps us identify:
# - Distribution of data
# - Spread of data
# - Outliers


# ============================================================
#               BOXEN PLOT FOR BALANCE
# ============================================================

# Create graph size
plt.figure(figsize=(10, 6))

# Create boxen plot
sns.boxenplot(
    x="Balance",
    data=dataset
)

# Add title
plt.title("Boxen Plot of Balance")

# Add label
plt.xlabel("Balance")

# Show graph
plt.show()


# ============================================================
#                 IMPORTANT POINTS
# ============================================================

"""
1. Percentile
--------------
- Shows position of data
- 50th percentile is Median

2. Quartiles
--------------
- Divide data into 4 equal parts
- Q1 = 25%
- Q2 = 50%
- Q3 = 75%

3. Interquartile Range (IQR)
-----------------------------
- IQR = Q3 - Q1
- Measures middle 50% spread

4. Boxen Plot
--------------
- Used for data distribution
- Helps detect outliers
- Useful in Data Analysis
"""


# ============================================================
#                        CONCLUSION
# ============================================================

print("\n========== CONCLUSION ==========\n")

print("""
Percentiles and Quartiles help us
understand the distribution of data.

Important concepts:
- Percentiles
- Quartiles
- IQR
- Boxen Plot

These concepts are very useful in:
- Data Science
- Data Analytics
- Machine Learning
- Statistical Analysis
""")