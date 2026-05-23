# ============================================================
#                    T-Test in Python
# ============================================================
#
# Topics Covered:
#
# 1. One Sample T-Test
# 2. Independent Two Sample T-Test
# 3. Paired T-Test
# 4. Hypothesis Testing
# 5. P-Value
# 6. Graph Visualization
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
#                    QUESTION 1
# ============================================================
#
# A manufacturer claims that the average weight
# of a bag of potato chips is 150 grams.
#
# A sample of 25 bags is taken.
#
# Sample Mean = 148 grams
# Sample Standard Deviation = 5 grams
#
# Test the claim using a one-tailed t-test
# with significance level 0.05
#
# ============================================================

print("\n========== QUESTION 1 : ONE SAMPLE T-TEST ==========\n")


# ============================================================
#                    GIVEN VALUES
# ============================================================

population_mean = 150
sample_size = 25
sample_mean = 148
sample_std = 5
alpha = 0.05

# Degree of freedom
degree_of_freedom = sample_size - 1


# ============================================================
#                 HYPOTHESIS FORMULATION
# ============================================================

print("Null Hypothesis (H0):")
print("Average weight is equal to 150 grams")

print("\nAlternative Hypothesis (Ha):")
print("Average weight is less than 150 grams")


# ============================================================
#                  CALCULATE T VALUE
# ============================================================

t_calculated = (
    (sample_mean - population_mean)
    /
    (sample_std / np.sqrt(sample_size))
)

# Critical T value for left-tailed test
t_critical = st.t.ppf(alpha, degree_of_freedom)

# P-value
p_value = st.t.cdf(t_calculated, degree_of_freedom)


# ============================================================
#                     PRINT RESULTS
# ============================================================

print("\nCalculated T Value :", round(t_calculated, 4))
print("Critical T Value   :", round(t_critical, 4))
print("P-Value            :", round(p_value, 6))


# ============================================================
#                     FINAL DECISION
# ============================================================

if t_calculated < t_critical:
    print("\nResult: Reject H0")
    print("Conclusion: Manufacturer claim is rejected")
else:
    print("\nResult: Fail to Reject H0")
    print("Conclusion: Manufacturer claim is accepted")


# ============================================================
#               VISUALIZATION OF T-TEST
# ============================================================

# Create x-axis values
x = np.linspace(-4, 4, 1000)

# T distribution curve
y = st.t.pdf(x, degree_of_freedom)

# Create graph
plt.figure(figsize=(10, 6))

# Plot curve
plt.plot(x, y, label="T Distribution")

# Critical T line
plt.axvline(
    t_critical,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Critical T = {round(t_critical, 2)}"
)

# Calculated T line
plt.axvline(
    t_calculated,
    color="green",
    linestyle="--",
    linewidth=2,
    label=f"Calculated T = {round(t_calculated, 2)}"
)

# Fill rejection region
plt.fill_between(
    x,
    y,
    where=(x <= t_critical),
    alpha=0.3
)

# Title
plt.title("One Sample T-Test")

# Labels
plt.xlabel("T Values")
plt.ylabel("Density")

# Legend
plt.legend()

# Show graph
plt.show()


# ============================================================
#                    QUESTION 2
# ============================================================
#
# A company wants to test whether there is
# a difference in productivity between two teams.
#
# Team A:
# Mean = 80
# Standard Deviation = 5
#
# Team B:
# Mean = 75
# Standard Deviation = 6
#
# Sample Size = 20 for both teams
#
# Test at 5% significance level.
#
# ============================================================

print("\n========== QUESTION 2 : TWO SAMPLE T-TEST ==========\n")


# ============================================================
#                    GIVEN VALUES
# ============================================================

sample_size = 20

sample_mean_A = 80
sample_mean_B = 75

std_A = 5
std_B = 6

alpha = 0.05

# Degree of freedom
degree_of_freedom = (sample_size * 2) - 2


# ============================================================
#                 HYPOTHESIS FORMULATION
# ============================================================

print("Null Hypothesis (H0):")
print("No difference in productivity")

print("\nAlternative Hypothesis (Ha):")
print("Difference exists in productivity")


# ============================================================
#                  CALCULATE T VALUE
# ============================================================

t_calculated = (
    (sample_mean_A - sample_mean_B)
    /
    np.sqrt(
        (std_A**2 / sample_size)
        +
        (std_B**2 / sample_size)
    )
)

# Critical T value for two-tailed test
t_critical = st.t.ppf(1 - alpha/2, degree_of_freedom)

# P-value
p_value = (
    2 *
    (1 - st.t.cdf(abs(t_calculated), degree_of_freedom))
)


# ============================================================
#                     PRINT RESULTS
# ============================================================

print("\nCalculated T Value :", round(t_calculated, 4))
print("Critical T Value   :", round(t_critical, 4))
print("P-Value            :", round(p_value, 6))


# ============================================================
#                     FINAL DECISION
# ============================================================

if abs(t_calculated) > t_critical:
    print("\nResult: Reject H0")
    print("Conclusion: Productivity difference exists")
else:
    print("\nResult: Fail to Reject H0")
    print("Conclusion: No significant difference found")


# ============================================================
#             VISUALIZATION OF TWO SAMPLE T-TEST
# ============================================================

# Create x-axis values
x = np.linspace(-5, 5, 1000)

# T distribution curve
y = st.t.pdf(x, degree_of_freedom)

# Create graph
plt.figure(figsize=(10, 6))

# Plot curve
plt.plot(x, y)

# Positive critical value
plt.axvline(
    t_critical,
    color="red",
    linestyle="--",
    label=f"+ Critical T = {round(t_critical, 2)}"
)

# Negative critical value
plt.axvline(
    -t_critical,
    color="red",
    linestyle="--",
    label=f"- Critical T = {round(-t_critical, 2)}"
)

# Calculated T line
plt.axvline(
    t_calculated,
    color="green",
    linestyle="--",
    label=f"Calculated T = {round(t_calculated, 2)}"
)

# Title
plt.title("Two Sample T-Test")

# Labels
plt.xlabel("T Values")
plt.ylabel("Density")

# Legend
plt.legend()

# Show graph
plt.show()


# ============================================================
#                    QUESTION 3
# ============================================================
#
# A company wants to check whether a new
# training program improves typing speed.
#
# Typing speed was recorded:
# - Before training
# - After training
#
# Test at 5% significance level.
#
# ============================================================

print("\n========== QUESTION 3 : PAIRED T-TEST ==========\n")


# ============================================================
#                    GIVEN DATA
# ============================================================

after_training = np.array([
    60, 70, 55, 75, 65,
    80, 50, 85, 90, 70,
    75, 65, 55, 60, 50,
    80, 65, 55, 70, 75
])

before_training = np.array([
    50, 60, 45, 65, 55,
    70, 40, 75, 80, 65,
    70, 60, 50, 55, 45,
    75, 60, 50, 65, 70
])

alpha = 0.05


# ============================================================
#                 HYPOTHESIS FORMULATION
# ============================================================

print("Null Hypothesis (H0):")
print("Training program has no effect")

print("\nAlternative Hypothesis (Ha):")
print("Training program improves typing speed")


# ============================================================
#                   PAIRED T-TEST
# ============================================================

t_statistic, p_value = st.ttest_rel(
    after_training,
    before_training
)


# ============================================================
#                    PRINT RESULTS
# ============================================================

print("\nT Statistic :", round(t_statistic, 4))
print("P-Value     :", round(p_value, 6))


# ============================================================
#                     FINAL DECISION
# ============================================================

if p_value < alpha:
    print("\nResult: Reject H0")
    print("Conclusion: Training program improves typing speed")
else:
    print("\nResult: Fail to Reject H0")
    print("Conclusion: No significant improvement found")


# ============================================================
#               VISUALIZATION OF PAIRED T-TEST
# ============================================================

plt.figure(figsize=(10, 6))

# Histogram before training
sns.histplot(
    before_training,
    kde=True,
    label="Before Training"
)

# Histogram after training
sns.histplot(
    after_training,
    kde=True,
    label="After Training"
)

# Title
plt.title("Before vs After Training")

# Labels
plt.xlabel("Typing Speed")
plt.ylabel("Frequency")

# Legend
plt.legend()

# Show graph
plt.show()


# ============================================================
#                  IMPORTANT POINTS
# ============================================================

"""
1. One Sample T-Test
---------------------
- Compares sample mean with population mean

2. Two Sample T-Test
---------------------
- Compares means of two independent groups

3. Paired T-Test
-----------------
- Compares before and after data

4. P-Value
------------
- If P-Value < 0.05
  -> Reject H0

- If P-Value >= 0.05
  -> Fail to Reject H0

5. T-Test
-----------
- Used when population standard deviation
  is unknown
"""


# ============================================================
#                        CONCLUSION
# ============================================================

print("\n========== CONCLUSION ==========\n")

print("""
T-Tests are important statistical methods
used for hypothesis testing.

Types Covered:
- One Sample T-Test
- Two Sample T-Test
- Paired T-Test

These tests help us:
- Compare means
- Check significant differences
- Make data-driven decisions

These concepts are useful in:
- Data Science
- Machine Learning
- Business Analytics
- Research Analysis
""")