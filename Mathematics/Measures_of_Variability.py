# ============================================================
#               Statistics in Python using Pandas
# ============================================================
#
# Topics Covered:
#
# 1. Range
# 2. Mean Absolute Deviation (MAD)
# 3. Variance
# 4. Standard Deviation
# 5. Dataset Summary using describe()
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
#               MEASURES OF DISPERSION
# ============================================================
#
# Dispersion means:
# How much the data values are spread out.
#
# Main Topics:
# 1. Range
# 2. Mean Absolute Deviation
# 3. Variance
# 4. Standard Deviation
#
# ============================================================


# ============================================================
#                          1. RANGE
# ============================================================

print("\n========== RANGE ==========\n")

# Range Formula:
# Range = Maximum Value - Minimum Value

# Find minimum and maximum age
min_age = dataset["Age"].min()
max_age = dataset["Age"].max()

# Calculate range
range_age = max_age - min_age

# Print results
print("Minimum Age :", min_age)
print("Maximum Age :", max_age)
print("Range of Age:", range_age)


# ============================================================
#               RANGE OF BALANCE COLUMN
# ============================================================

min_balance = dataset["Balance"].min()
max_balance = dataset["Balance"].max()

range_balance = max_balance - min_balance

print("\nMinimum Balance :", min_balance)
print("Maximum Balance :", max_balance)
print("Range of Balance:", range_balance)

# Explanation:
# Range shows the difference between
# the smallest and largest value.


# ============================================================
#              2. MEAN ABSOLUTE DEVIATION (MAD)
# ============================================================

print("\n========== MEAN ABSOLUTE DEVIATION ==========\n")

# Create Sample Data
A = np.array([75, 65, 63, 68, 72, 76])
B = np.array([90, 47, 43, 96, 93, 51])

# Calculate Mean
mean_A = np.mean(A)
mean_B = np.mean(B)

print("Mean of A:", mean_A)
print("Mean of B:", mean_B)

# MAD Formula:
# Sum of absolute differences from mean / Total values

mad_A = np.sum(np.abs(A - mean_A)) / len(A)
mad_B = np.sum(np.abs(B - mean_B)) / len(B)

print("\nMAD of A:", mad_A)
print("MAD of B:", mad_B)

# Explanation:
# Lower MAD means data is close to mean.
# Higher MAD means data is more spread out.


# ============================================================
#              VISUALIZATION OF MAD
# ============================================================

# Create position values
numbers = np.array([1, 2, 3, 4, 5, 6])

# Create graph size
plt.figure(figsize=(10, 7))

# Scatter plot for dataset A
plt.scatter(
    A,
    numbers,
    label="Dataset A"
)

# Scatter plot for dataset B
plt.scatter(
    B,
    numbers,
    label="Dataset B",
    color="red"
)

# Draw mean line for A
plt.plot(
    [mean_A] * len(numbers),
    numbers,
    color="blue",
    label="Mean of A"
)

# Draw mean line for B
plt.plot(
    [mean_B] * len(numbers),
    numbers,
    color="green",
    label="Mean of B"
)

# Graph title
plt.title("Mean Absolute Deviation")

# Axis labels
plt.xlabel("Values")
plt.ylabel("Position")

# Show legend
plt.legend()

# Show graph
plt.show()


# ============================================================
#                         3. VARIANCE
# ============================================================

print("\n========== VARIANCE ==========\n")

# Variance measures how far data points
# are spread from the mean.

variance_A = np.var(A)
variance_B = np.var(B)

print("Variance of A:", variance_A)
print("Variance of B:", variance_B)

# Explanation:
# Larger variance means greater spread in data.


# ============================================================
#                  4. STANDARD DEVIATION
# ============================================================

print("\n========== STANDARD DEVIATION ==========\n")

# Standard deviation is the square root of variance.

std_A = np.std(A)
std_B = np.std(B)

print("Standard Deviation of A:", std_A)
print("Standard Deviation of B:", std_B)

# Explanation:
# It shows how much data values
# move away from the mean.


# ============================================================
#           HISTOGRAM OF AGE COLUMN
# ============================================================

plt.figure(figsize=(10, 6))

# Create histogram
sns.histplot(
    x="Age",
    data=dataset,
    kde=True
)

# Add title
plt.title("Distribution of Age")

# Add labels
plt.xlabel("Age")
plt.ylabel("Frequency")

# Show graph
plt.show()


# ============================================================
#                  DATASET SUMMARY
# ============================================================

print("\n========== DATASET SUMMARY ==========\n")

# describe() gives:
# count, mean, std, min, max, quartiles, etc.

print(dataset.describe())


# ============================================================
#                 IMPORTANT POINTS
# ============================================================

"""
1. Range
---------
- Difference between maximum and minimum value
- Easy to calculate
- Affected by outliers

2. Mean Absolute Deviation (MAD)
--------------------------------
- Average distance from mean
- Helps understand spread of data

3. Variance
------------
- Measures spread of data
- Uses squared differences

4. Standard Deviation
----------------------
- Square root of variance
- Most commonly used measure
- Lower value means data is close to mean

5. describe() Function
-----------------------
- Gives statistical summary of dataset
- Very useful in Data Analysis
"""


# ============================================================
#                        CONCLUSION
# ============================================================

print("\n========== CONCLUSION ==========\n")

print("""
Measures of Dispersion help us understand
how much data is spread out.

Important concepts:
- Range
- Mean Absolute Deviation
- Variance
- Standard Deviation

These concepts are very useful in:
- Data Science
- Data Analytics
- Machine Learning
- Business Analysis
""")