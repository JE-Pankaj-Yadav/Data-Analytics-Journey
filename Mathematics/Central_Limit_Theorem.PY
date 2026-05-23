# ============================================================
#              Central Limit Theorem (CLT) in Python
# ============================================================
#
# Topics Covered:
#
# 1. Population Data
# 2. Sample Data
# 3. Sample Mean
# 4. Central Limit Theorem (CLT)
# 5. KDE Plot Visualization
#
# Libraries Used:
# - NumPy      -> Mathematical calculations
# - Pandas     -> Data handling
# - Matplotlib -> Data visualization
# - Seaborn    -> Beautiful graphs
#
# ============================================================


# =========================
# Import Required Libraries
# =========================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
#                 CENTRAL LIMIT THEOREM
# ============================================================
#
# Central Limit Theorem (CLT) says:
#
# "If we take many random samples from a population
# and calculate their means, then the distribution
# of sample means becomes approximately normal."
#
# Even if the original population is not normal.
#
# ============================================================


# ============================================================
#                  CREATE POPULATION DATA
# ============================================================

# Generate random population data
# randint(10, 100) means:
# Random values between 10 and 100

population_data = [
    np.random.randint(10, 100)
    for i in range(10000)
]

# Convert into DataFrame
population_table = pd.DataFrame({
    "Population_Data": population_data
})

# Display first 5 rows
print("\n========== FIRST 5 ROWS OF POPULATION DATA ==========\n")
print(population_table.head())


# ============================================================
#                 POPULATION MEAN
# ============================================================

print("\n========== POPULATION MEAN ==========\n")

# Calculate mean of population
population_mean = np.mean(population_data)

print("Population Mean:", population_mean)

# Explanation:
# Population mean is the average
# of all population values.


# ============================================================
#            VISUALIZATION OF POPULATION DATA
# ============================================================

plt.figure(figsize=(8, 5))

# KDE Plot
sns.kdeplot(
    x="Population_Data",
    data=population_table,
    fill=True
)

# Add title
plt.title("Population Data Distribution")

# Axis labels
plt.xlabel("Population Values")
plt.ylabel("Density")

# Show graph
plt.show()


# ============================================================
#                  CREATE SAMPLE MEANS
# ============================================================

# Empty list to store sample means
sample_means = []

# Total number of samples
number_of_samples = 50

# Sample size
sample_size = 1000


# Loop for creating multiple samples
for sample_number in range(number_of_samples):

    # Empty list for storing sample data
    sample_data = []

    # Generate random sample values
    for value in range(sample_size):

        # Randomly choose value from population
        random_value = np.random.choice(population_data)

        # Add value into sample
        sample_data.append(random_value)

    # Calculate sample mean
    mean_of_sample = np.mean(sample_data)

    # Store sample mean
    sample_means.append(mean_of_sample)


# ============================================================
#                   SAMPLE MEAN RESULT
# ============================================================

print("\n========== SAMPLE MEAN ==========\n")

# Mean of all sample means
final_sample_mean = np.mean(sample_means)

print("Mean of Sample Means:", final_sample_mean)

# Explanation:
# According to CLT:
# Population Mean ≈ Mean of Sample Means


# ============================================================
#             SAMPLE MEANS DATAFRAME
# ============================================================

sample_mean_table = pd.DataFrame({
    "Sample_Mean": sample_means
})

# Display first 5 rows
print("\n========== FIRST 5 SAMPLE MEANS ==========\n")
print(sample_mean_table.head())


# ============================================================
#         VISUALIZATION OF SAMPLE MEAN DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))

# KDE Plot for sample means
sns.kdeplot(
    x="Sample_Mean",
    data=sample_mean_table,
    fill=True
)

# Add title
plt.title("Distribution of Sample Means")

# Axis labels
plt.xlabel("Sample Mean")
plt.ylabel("Density")

# Show graph
plt.show()


# ============================================================
#           COMPARISON OF POPULATION AND SAMPLE
# ============================================================

print("\n========== COMPARISON ==========\n")

print("Population Mean       :", population_mean)
print("Mean of Sample Means  :", final_sample_mean)

# Difference
difference = abs(population_mean - final_sample_mean)

print("Difference            :", difference)

# Explanation:
# Smaller difference means
# Central Limit Theorem works correctly.


# ============================================================
#                 IMPORTANT POINTS
# ============================================================

"""
1. Population
--------------
- Complete collection of data

2. Sample
-----------
- Small part of population

3. Sample Mean
---------------
- Average value of sample data

4. Central Limit Theorem
-------------------------
- Sample means follow normal distribution
- Works even if population is not normal

5. Larger Sample Size
----------------------
- Gives better approximation

6. KDE Plot
-------------
- Shows smooth data distribution
"""


# ============================================================
#              ADVANTAGES OF CLT
# ============================================================

"""
1. Helps in statistical analysis

2. Used in Machine Learning

3. Used in Data Science

4. Helps estimate population behavior

5. Important for hypothesis testing
"""


# ============================================================
#                        CONCLUSION
# ============================================================

print("\n========== CONCLUSION ==========\n")

print("""
Central Limit Theorem is one of the
most important concepts in statistics.

It says that:
The distribution of sample means becomes
approximately normal when sample size
is large enough.

Important concepts:
- Population
- Sample
- Sample Mean
- Normal Distribution

These concepts are very useful in:
- Data Science
- Data Analytics
- Machine Learning
- Statistical Analysis
""")