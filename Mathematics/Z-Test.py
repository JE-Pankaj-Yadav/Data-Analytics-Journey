# ============================================================
#                  Z-Test in Python
# ============================================================
#
# Topics Covered:
#
# 1. Hypothesis Testing
# 2. Null Hypothesis (H0)
# 3. Alternative Hypothesis (Ha)
# 4. Z-Test
# 6. P-Value
# 7. Graph Visualization
#
# Libraries Used:
# - NumPy       -> Mathematical calculations
# - SciPy       -> Statistical functions
# - Matplotlib  -> Data visualization
# - Seaborn     -> Beautiful graphs
#
# ============================================================


# =========================
# Import Required Libraries
# =========================

import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
#                  HYPOTHESIS TESTING
# ============================================================
#
# Hypothesis Testing is used to check whether
# a statement is true or false using sample data.
#
# Main Terms:
#
# H0 (Null Hypothesis)
# -> No significant difference exists
#
# Ha (Alternative Hypothesis)
# -> Significant difference exists
#
# Alpha (α)
# -> Significance level
# -> Common value = 0.05
#
# ============================================================


# ============================================================
#                         Z-TEST
# ============================================================
#
# Z-Test is used when:
#
# 1. Population standard deviation is known
# 2. Sample size is large (n >= 30)
#
# Formula:
#
# Z = (Sample Mean - Population Mean)
#     --------------------------------
#      Population Std / sqrt(n)
#
# ============================================================


# ============================================================
#                  QUESTION 1 : SIMPLE Z-TEST
# ============================================================
#
# Question:
#
# A teacher claims that the mean score of students
# in his class is greater than 82 with a standard
# deviation of 20.
#
# A sample of 81 students was selected and the
# sample mean score was 90.
#
# Check whether the teacher's claim is correct.
#
# ============================================================

print("\n========== QUESTION 1 : SIMPLE Z-TEST ==========\n")


# ============================================================
#                    GIVEN VALUES
# ============================================================

# Population Mean
population_mean = 82

# Population Standard Deviation
population_std = 20

# Sample Size
sample_size = 81

# Sample Mean
sample_mean = 90

# Significance Level
alpha = 0.05


# ============================================================
#                 HYPOTHESIS FORMULATION
# ============================================================

print("Null Hypothesis (H0): Mean <= 82")
print("Alternative Hypothesis (Ha): Mean > 82")


# ============================================================
#                  CALCULATE Z VALUE
# ============================================================

z_calculated = (
    (sample_mean - population_mean)
    /
    (population_std / np.sqrt(sample_size))
)

# Critical Z value for one-tailed test
z_critical = st.norm.ppf(1 - alpha)

# P-value calculation
p_value = 1 - st.norm.cdf(z_calculated)


# ============================================================
#                     PRINT RESULTS
# ============================================================

print("\nSample Mean        :", sample_mean)
print("Population Mean    :", population_mean)

print("\nCalculated Z Value :", round(z_calculated, 4))
print("Critical Z Value   :", round(z_critical, 4))
print("P-Value            :", round(p_value, 6))


# ============================================================
#                      FINAL DECISION
# ============================================================

if z_calculated > z_critical:
    print("\nResult: Reject H0")
    print("Conclusion: Teacher's claim is correct")
else:
    print("\nResult: Fail to Reject H0")
    print("Conclusion: Teacher's claim is not supported")


# ============================================================
#               VISUALIZATION OF SIMPLE Z-TEST
# ============================================================

# Create x-axis values
x = np.linspace(-4, 5, 1000)

# Normal distribution curve
y = st.norm.pdf(x)

# Create graph size
plt.figure(figsize=(10, 6))

# Plot normal distribution curve
plt.plot(x, y, label="Normal Distribution")

# Critical Z line
plt.axvline(
    z_critical,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Critical Z = {round(z_critical, 2)}"
)

# Calculated Z line
plt.axvline(
    z_calculated,
    color="green",
    linestyle="--",
    linewidth=2,
    label=f"Calculated Z = {round(z_calculated, 2)}"
)

# Shade rejection region
plt.fill_between(
    x,
    y,
    where=(x >= z_critical),
    alpha=0.3
)

# Add title
plt.title("Simple Z-Test")

# Add labels
plt.xlabel("Z Values")
plt.ylabel("Density")

# Show legend
plt.legend()

# Show graph
plt.show()


# ============================================================
#                QUESTION 2 : DESIGN TEST
# ============================================================
#
# Scenario:
#
# An e-commerce company wants to check whether
# a new website design increases the average
# customer purchase amount.
#
# We compare:
# - Old Website Design
# - New Website Design
#
# Goal:
# Check whether the new design performs better.
#
# ============================================================

print("\n========== QUESTION 2 : DESIGN Z-TEST ==========\n")


# ============================================================
#                    GIVEN VALUES
# ============================================================

# Population standard deviation
population_std = 2.5

# Sample size
sample_size = 30


# ============================================================
#                  OLD DESIGN DATA
# ============================================================

old_design_data = np.array([
    45.2, 42.8, 38.9, 43.5, 41.0,
    44.6, 40.5, 42.7, 39.8, 41.4,
    44.3, 39.7, 42.1, 40.6, 43.0,
    42.2, 41.5, 39.6, 44.0, 43.1,
    38.7, 43.9, 42.0, 41.9, 42.8,
    43.7, 41.3, 40.9, 42.5, 41.6
])


# ============================================================
#                  NEW DESIGN DATA
# ============================================================

new_design_data = np.array([
    48.5, 49.1, 50.2, 47.8, 48.7,
    49.9, 48.0, 50.5, 49.8, 49.6,
    48.2, 48.9, 49.7, 50.3, 49.4,
    50.1, 48.6, 48.3, 49.0, 50.0,
    48.4, 49.3, 49.5, 48.8, 50.6,
    50.4, 48.1, 49.2, 50.7, 50.8
])


# ============================================================
#                 HYPOTHESIS FORMULATION
# ============================================================

print("Null Hypothesis (H0):")
print("New website design does NOT improve purchases")

print("\nAlternative Hypothesis (Ha):")
print("New website design improves purchases")


# ============================================================
#                    CALCULATE MEANS
# ============================================================

old_mean = np.mean(old_design_data)
new_mean = np.mean(new_design_data)

print("\nOld Design Mean :", round(old_mean, 2))
print("New Design Mean :", round(new_mean, 2))


# ============================================================
#                  CALCULATE Z VALUE
# ============================================================

z_calculated = (
    (new_mean - old_mean)
    /
    (population_std / np.sqrt(sample_size))
)

# Critical Z value
z_critical = st.norm.ppf(1 - alpha)

# P-value
p_value = 1 - st.norm.cdf(z_calculated)


# ============================================================
#                     PRINT RESULTS
# ============================================================

print("\nCalculated Z Value :", round(z_calculated, 4))
print("Critical Z Value   :", round(z_critical, 4))
print("P-Value            :", round(p_value, 10))


# ============================================================
#                      FINAL DECISION
# ============================================================

if z_calculated > z_critical:
    print("\nResult: Reject H0")
    print("Conclusion: New design performs significantly better")
else:
    print("\nResult: Fail to Reject H0")
    print("Conclusion: No significant improvement found")


# ============================================================
#                  VISUALIZATION OF Z-TEST
# ============================================================

# Create x-axis values
x = np.linspace(-4, 8, 1000)

# Normal distribution curve
y = st.norm.pdf(x)

# Create graph size
plt.figure(figsize=(10, 6))

# Plot curve
plt.plot(x, y, label="Normal Distribution")

# Critical Z line
plt.axvline(
    z_critical,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Critical Z = {round(z_critical, 2)}"
)

# Calculated Z line
plt.axvline(
    z_calculated,
    color="green",
    linestyle="--",
    linewidth=2,
    label=f"Calculated Z = {round(z_calculated, 2)}"
)

# Shade rejection region
plt.fill_between(
    x,
    y,
    where=(x >= z_critical),
    alpha=0.3
)

# Add title
plt.title("Z-Test for Old vs New Website Design")

# Add labels
plt.xlabel("Z Values")
plt.ylabel("Density")

# Show legend
plt.legend()

# Show graph
plt.show()


# ============================================================
#                          T-TEST
# ============================================================
#
# T-Test is used when:
#
# 1. Population standard deviation is NOT known
# 2. Sample size is small
#
# Here we perform Independent T-Test
# because both groups are independent.
#
# ============================================================

print("\n========== T-TEST ==========\n")


# ============================================================
#                   PERFORM T-TEST
# ============================================================

t_statistic, t_p_value = st.ttest_ind(
    new_design_data,
    old_design_data
)


# ============================================================
#                    PRINT RESULTS
# ============================================================

print("T Statistic :", round(t_statistic, 4))
print("P-Value     :", round(t_p_value, 10))


# ============================================================
#                     FINAL DECISION
# ============================================================

if t_p_value < alpha:
    print("\nResult: Reject H0")
    print("Conclusion: Significant difference exists")
else:
    print("\nResult: Fail to Reject H0")
    print("Conclusion: No significant difference exists")


# ============================================================
#                HISTOGRAM COMPARISON
# ============================================================

plt.figure(figsize=(10, 6))

# Histogram for old design
sns.histplot(
    old_design_data,
    kde=True,
    label="Old Design"
)

# Histogram for new design
sns.histplot(
    new_design_data,
    kde=True,
    label="New Design"
)

# Add title
plt.title("Old Design vs New Design")

# Axis labels
plt.xlabel("Purchase Amount")
plt.ylabel("Frequency")

# Show legend
plt.legend()

# Show graph
plt.show()


# ============================================================
#                  IMPORTANT POINTS
# ============================================================

"""
1. Z-Test
-----------
- Used for large sample sizes
- Population standard deviation is known

2. T-Test
-----------
- Used for small sample sizes
- Population standard deviation is unknown

3. P-Value
------------
- If P-Value < 0.05
  -> Reject H0

- If P-Value >= 0.05
  -> Fail to Reject H0

4. One-Tailed Test
-------------------
- Checks only one direction
- Example:
  Mean is greater than a value

5. Hypothesis Testing
----------------------
- Helps in decision making
- Used in research and business analysis
"""


# ============================================================
#                        CONCLUSION
# ============================================================

print("\n========== CONCLUSION ==========\n")

print("""
Z-Test and T-Test are important
hypothesis testing techniques.

They help us:
- Compare groups
- Find significant differences
- Make data-driven decisions

Important concepts:
- Null Hypothesis (H0)
- Alternative Hypothesis (Ha)
- Z-Test
- T-Test
- P-Value

These concepts are widely used in:
- Data Science
- Machine Learning
- Research Analysis
- Business Analytics
""")