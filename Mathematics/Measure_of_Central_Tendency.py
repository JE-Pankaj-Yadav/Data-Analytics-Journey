# ============================================================
#            Measures of Central Tendency in Python
# ============================================================
# Topics Covered:
# 1. Mean
# 2. Median
# 3. Mode
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

# Show first 5 rows of dataset
print("\nFirst 5 Rows of Dataset:\n")
print(dataset.head())


# ============================================================
#              MEASURES OF CENTRAL TENDENCY
# ============================================================
#
# Central Tendency means:
# "The center or average value of data"
#
# There are 3 main types:
#
# 1. Mean   -> Average value
# 2. Median -> Middle value
# 3. Mode   -> Most repeated value
#
# ============================================================


# ============================================================
#                         1. MEAN
# ============================================================

print("\n================ MEAN =================")

# Mean Formula:
# Sum of all values / Total number of values

# Calculate Mean of Age column
mean_age = dataset["Age"].mean()

# Another method using NumPy
mean_age_numpy = np.mean(dataset["Age"])

print("Mean using Pandas :", mean_age)
print("Mean using NumPy  :", mean_age_numpy)

# Explanation:
# Mean gives the average value of the data.


# ============================================================
#                        2. MEDIAN
# ============================================================

print("\n================ MEDIAN =================")

# Median means middle value after sorting the data.

# Calculate Median of Balance column
median_balance = dataset["Balance"].median()

# Another method using NumPy
median_balance_numpy = np.median(dataset["Balance"])

print("Median using Pandas :", median_balance)
print("Median using NumPy  :", median_balance_numpy)

# Explanation:
# Median is useful when data contains outliers.
# Example:
# Salary data, bank balance, etc.


# ============================================================
#                         3. MODE
# ============================================================

print("\n================ MODE =================")

# Mode means the most frequently repeated value.

# Calculate Mode of Region column
mode_region = dataset["Region"].mode()[0]

print("Mode of Region :", mode_region)

# Count frequency of each value
print("\nValue Counts:\n")
print(dataset["Region"].value_counts())

# Explanation:
# Mode is mostly used for categorical data.
# Example:
# City names, product category, gender, etc.


# ============================================================
#               COMPARISON OF MEAN, MEDIAN, MODE
# ============================================================

print("\n========== COMPARISON ==========")

print(f"Mean   of Age     : {mean_age}")
print(f"Median of Balance : {median_balance}")
print(f"Mode   of Region  : {mode_region}")


# ============================================================
#               VISUALIZATION OF MEAN, MEDIAN, MODE
# ============================================================

# ------------------------------------------------------------
# Histogram for Age Column
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

# Create histogram
sns.histplot(
    x="Age",
    data=dataset,
    bins=10,
    kde=True
)

# Draw Mean Line
plt.axvline(
    mean_age,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Mean = {round(mean_age, 2)}"
)

# Draw Median Line
median_age = dataset["Age"].median()

plt.axvline(
    median_age,
    color="green",
    linestyle="--",
    linewidth=2,
    label=f"Median = {round(median_age, 2)}"
)

# Draw Mode Line
mode_age = dataset["Age"].mode()[0]

plt.axvline(
    mode_age,
    color="blue",
    linestyle="--",
    linewidth=2,
    label=f"Mode = {mode_age}"
)

# Graph Title
plt.title("Mean, Median and Mode of Age")

# X-axis label
plt.xlabel("Age")

# Y-axis label
plt.ylabel("Frequency")

# Show legend
plt.legend()

# Show graph
plt.show()


# ============================================================
#                 MODE VISUALIZATION (Count Plot)
# ============================================================

plt.figure(figsize=(10, 6))

# Count plot for Region column
sns.countplot(x="Region", data=dataset)

# Position of Mode
mode_position = dataset["Region"].value_counts().index.get_loc(mode_region)

# Draw vertical line
plt.axvline(
    x=mode_position,
    color="blue",
    linestyle="--",
    linewidth=2,
    label=f"Mode = {mode_region}"
)

# Title
plt.title("Mode of Region")

# Labels
plt.xlabel("Region")
plt.ylabel("Count")

# Legend
plt.legend()

# Show graph
plt.show()


# ============================================================
#                   IMPORTANT POINTS
# ============================================================

"""
1. Mean
---------
- Uses all values in the dataset
- Sensitive to outliers
- Best for normally distributed data

2. Median
-----------
- Middle value of sorted data
- Not affected much by outliers
- Best for skewed data

3. Mode
---------
- Most repeated value
- Can be used for categorical data
- A dataset can have:
    - One mode  -> Unimodal
    - Two modes -> Bimodal
    - Many modes -> Multimodal

"""


# ============================================================
#                        CONCLUSION
# ============================================================

print("\n================ CONCLUSION =================")

print("""
Mean, Median, and Mode are called
Measures of Central Tendency.

They help us understand the center point
or typical value of the data.

- Mean   -> Average value
- Median -> Middle value
- Mode   -> Most repeated value
""")