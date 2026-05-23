# ============================================================
#                 Measures of Shape in Python
# ============================================================
#
# Topics Covered:
#
# 1. Skewness
# 2. Distribution Shape
# 3. Relationship between:
#    - Mean
#    - Median
#    - Mode
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

dataset = pd.read_csv("Data.csv")

# Display first 5 rows
print("\n========== FIRST 5 ROWS OF DATASET ==========\n")
print(dataset.head())


# ============================================================
#                  MEASURES OF SHAPE
# ============================================================
#
# Measures of Shape help us understand:
# - Shape of data distribution
# - Symmetry of data
# - Direction of data spread
#
# Main Topics:
# 1. Skewness
# 2. Symmetrical Distribution
# 3. Positive Skewness
# 4. Negative Skewness
#
# ============================================================


# ============================================================
#            MEAN, MEDIAN AND MODE OF AGE
# ============================================================

print("\n========== AGE COLUMN ANALYSIS ==========\n")

# Calculate Mean
mean_age = dataset["Age"].mean()

# Calculate Median
median_age = dataset["Age"].median()

# Calculate Mode
mode_age = dataset["Age"].mode()[0]

# Print Results
print("Mean   :", mean_age)
print("Median :", median_age)
print("Mode   :", mode_age)

# Explanation:
# These values help us understand
# the center of the data.


# ============================================================
#                 HISTOGRAM OF AGE
# ============================================================

plt.figure(figsize=(10, 6))

# Create histogram
sns.histplot(
    x="Age",
    data=dataset,
    kde=True
)

# Add Mean Line
plt.axvline(
    mean_age,
    color="red",
    linestyle="--",
    linewidth=2,
    label="Mean"
)

# Add Median Line
plt.axvline(
    median_age,
    color="green",
    linestyle="--",
    linewidth=2,
    label="Median"
)

# Add Mode Line
plt.axvline(
    mode_age,
    color="blue",
    linestyle="--",
    linewidth=2,
    label="Mode"
)

# Add title
plt.title("Distribution of Age")

# Axis labels
plt.xlabel("Age")
plt.ylabel("Frequency")

# Show legend
plt.legend()

# Show graph
plt.show()


# ============================================================
#                RANDOM NORMAL DISTRIBUTION
# ============================================================

print("\n========== RANDOM DATA ANALYSIS ==========\n")

# Generate random normal data
# Mean = 0
# Standard Deviation = 100
# Total Values = 100

data = np.random.normal(0, 100, 100)

# Convert into DataFrame
df = pd.DataFrame({"x": data})

# Display first 5 rows
print(df.head())


# ============================================================
#                     SKEWNESS
# ============================================================

print("\n========== SKEWNESS ==========\n")

# Calculate skewness
skewness_value = df["x"].skew()

print("Skewness :", skewness_value)

# Explanation:
#
# If Skewness = 0
# -> Data is Symmetrical
#
# If Skewness > 0
# -> Positive Skewed Data
# -> Tail goes to right side
#
# If Skewness < 0
# -> Negative Skewed Data
# -> Tail goes to left side


# ============================================================
#         MEAN, MEDIAN AND MODE OF RANDOM DATA
# ============================================================

print("\n========== CENTRAL TENDENCY OF RANDOM DATA ==========\n")

# Calculate Mean
mean_x = df["x"].mean()

# Calculate Median
median_x = df["x"].median()

# Calculate Mode
mode_x = df["x"].mode()[0]

# Print Results
print("Mean   :", mean_x)
print("Median :", median_x)
print("Mode   :", mode_x)

# Explanation:
#
# Relationship between Mean, Median and Mode:
#
# 1. Symmetrical Distribution
#    Mean ≈ Median ≈ Mode
#
# 2. Positive Skewed Distribution
#    Mean > Median > Mode
#
# 3. Negative Skewed Distribution
#    Mean < Median < Mode


# ============================================================
#            HISTOGRAM OF RANDOM DATA
# ============================================================

plt.figure(figsize=(10, 6))

# Create histogram
sns.histplot(
    x="x",
    data=df,
    kde=True
)

# Add Mean Line
plt.axvline(
    mean_x,
    color="red",
    linestyle="--",
    linewidth=2,
    label="Mean"
)

# Add Median Line
plt.axvline(
    median_x,
    color="green",
    linestyle="--",
    linewidth=2,
    label="Median"
)

# Add Mode Line
plt.axvline(
    mode_x,
    color="blue",
    linestyle="--",
    linewidth=2,
    label="Mode"
)

# Add title
plt.title("Random Normal Distribution")

# Axis labels
plt.xlabel("Values")
plt.ylabel("Frequency")

# Show legend
plt.legend()

# Show graph
plt.show()


# ============================================================
#                 TYPES OF SKEWNESS
# ============================================================

"""
1. Symmetrical Distribution
----------------------------
- Mean ≈ Median ≈ Mode
- Data is equally distributed

2. Positive Skewness
---------------------
- Tail goes towards right side
- Mean > Median > Mode

3. Negative Skewness
---------------------
- Tail goes towards left side
- Mean < Median < Mode
"""


# ============================================================
#                 IMPORTANT POINTS
# ============================================================

"""
1. Skewness measures the shape of data.

2. Skewness tells whether data is:
   - Symmetrical
   - Positively skewed
   - Negatively skewed

3. Histogram helps visualize data distribution.

4. KDE Curve:
   KDE stands for Kernel Density Estimation.
   It gives a smooth curve of distribution.

5. Mean, Median and Mode help identify skewness.
"""


# ============================================================
#                        CONCLUSION
# ============================================================

print("\n========== CONCLUSION ==========\n")

print("""
Measures of Shape help us understand
the distribution pattern of data.

Important concepts:
- Skewness
- Symmetrical Distribution
- Positive Skewness
- Negative Skewness

These concepts are very important in:
- Data Science
- Data Analytics
- Machine Learning
- Statistical Analysis
""")