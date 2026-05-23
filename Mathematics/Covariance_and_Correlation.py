# ============================================================
#           Covariance and Correlation in Python
# ============================================================
#
# Topics Covered:
#
# 1. Covariance
# 2. Correlation
# 3. Heatmap Visualization
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
#                    DATASET INFORMATION
# ============================================================

print("\n========== DATASET INFO ==========\n")

# info() gives:
# - Column names
# - Data types
# - Non-null values

print(dataset.info())


# ============================================================
#              SELECT NUMERICAL COLUMNS
# ============================================================

# Select only numerical columns
# int64  -> Integer values
# float64 -> Decimal values

numeric_data = dataset.select_dtypes(
    include=["int64", "float64"]
)

print("\n========== NUMERICAL COLUMNS ==========\n")
print(numeric_data.head())


# ============================================================
#                     CORRELATION
# ============================================================
#
# Correlation measures:
# Relationship between two variables.
#
# Correlation Value Range:
#
# +1  -> Perfect Positive Correlation
#  0  -> No Correlation
# -1  -> Perfect Negative Correlation
#
# ============================================================

print("\n========== CORRELATION MATRIX ==========\n")

# Calculate correlation matrix
data_corr = numeric_data.corr()

# Print correlation matrix
print(data_corr)

# Explanation:
#
# Positive Correlation:
# If one variable increases,
# the other also increases.
#
# Negative Correlation:
# If one variable increases,
# the other decreases.
#
# No Correlation:
# No relationship between variables.


# ============================================================
#                  CORRELATION HEATMAP
# ============================================================

plt.figure(figsize=(10, 6))

# Create heatmap
sns.heatmap(
    data_corr,
    annot=True,
    cmap="coolwarm"
)

# Add title
plt.title("Correlation Heatmap")

# Show graph
plt.show()


# ============================================================
#                      COVARIANCE
# ============================================================
#
# Covariance measures:
# Direction of relationship between variables.
#
# Positive Covariance:
# Variables move in same direction.
#
# Negative Covariance:
# Variables move in opposite direction.
#
# ============================================================

print("\n========== COVARIANCE MATRIX ==========\n")

# Calculate covariance matrix
data_cov = numeric_data.cov()

# Print covariance matrix
print(data_cov)

# Explanation:
#
# Large positive value:
# Strong positive relationship
#
# Large negative value:
# Strong negative relationship
#
# Near zero:
# Weak relationship


# ============================================================
#                   COVARIANCE HEATMAP
# ============================================================

plt.figure(figsize=(10, 6))

# Create heatmap
sns.heatmap(
    data_cov,
    annot=True,
    cmap="viridis"
)

# Add title
plt.title("Covariance Heatmap")

# Show graph
plt.show()


# ============================================================
#          DIFFERENCE BETWEEN CORRELATION AND COVARIANCE
# ============================================================

"""
1. Correlation
---------------
- Measures both strength and direction
- Value always between -1 and +1
- Easy to understand
- Standardized value

2. Covariance
---------------
- Measures only direction
- Value can be any number
- Harder to compare
- Not standardized
"""


# ============================================================
#                 IMPORTANT POINTS
# ============================================================

"""
1. Correlation helps find relationships between variables.

2. Correlation is widely used in:
   - Data Science
   - Machine Learning
   - Business Analytics

3. Heatmaps help visualize relationships easily.

4. Covariance shows whether variables move
   together or opposite.

5. Correlation is more useful than covariance
   for comparing relationships.
"""


# ============================================================
#                        CONCLUSION
# ============================================================

print("\n========== CONCLUSION ==========\n")

print("""
Covariance and Correlation help us
understand relationships between variables.

Important concepts:
- Positive Relationship
- Negative Relationship
- Strength of Relationship
- Heatmap Visualization

These concepts are very important in:
- Data Science
- Data Analytics
- Machine Learning
- Statistical Analysis
""")