# ============================================================
#                 Chi-Square Test in Python
# ============================================================
#
# Topics Covered:
#
# 1. Chi-Square Goodness of Fit Test
# 2. Chi-Square Test of Independence
# 3. Hypothesis Testing
# 4. Expected Frequency
# 5. Degrees of Freedom
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
# A fair die is rolled 120 times and
# the following results are obtained:
#
# Face 1 -> 22 times
# Face 2 -> 17 times
# Face 3 -> 20 times
# Face 4 -> 26 times
# Face 5 -> 22 times
# Face 6 -> 13 times
#
# Test at 5% significance level whether
# the die is fair.
#
# ============================================================

print("\n========== QUESTION 1 : GOODNESS OF FIT TEST ==========\n")


# ============================================================
#                 OBSERVED FREQUENCIES
# ============================================================

observed_values = np.array([22, 17, 20, 26, 22, 13])

# Expected frequency for fair die
# Total rolls = 120
# 120 / 6 = 20

expected_values = np.array([20, 20, 20, 20, 20, 20])

# Significance level
alpha = 0.05


# ============================================================
#                 HYPOTHESIS FORMULATION
# ============================================================

print("Null Hypothesis (H0):")
print("The die is fair")

print("\nAlternative Hypothesis (Ha):")
print("The die is not fair")


# ============================================================
#                 CHI-SQUARE FORMULA
# ============================================================
#
# Formula:
#
# χ² = Σ (Observed - Expected)² / Expected
#
# ============================================================

chi_calculated = np.sum(
    ((observed_values - expected_values) ** 2)
    /
    expected_values
)

# Degree of freedom
# df = n - 1

degree_of_freedom = len(observed_values) - 1

# Critical chi-square value
chi_critical = st.chi2.ppf(
    1 - alpha,
    degree_of_freedom
)

# P-value
p_value = 1 - st.chi2.cdf(
    chi_calculated,
    degree_of_freedom
)


# ============================================================
#                     PRINT RESULTS
# ============================================================

print("\nObserved Values :", observed_values)
print("Expected Values :", expected_values)

print("\nCalculated Chi-Square :", round(chi_calculated, 4))
print("Critical Chi-Square   :", round(chi_critical, 4))
print("P-Value               :", round(p_value, 6))


# ============================================================
#                     FINAL DECISION
# ============================================================

if chi_calculated > chi_critical:
    print("\nResult: Reject H0")
    print("Conclusion: Die is not fair")
else:
    print("\nResult: Fail to Reject H0")
    print("Conclusion: Die is fair")


# ============================================================
#                VISUALIZATION OF DIE DATA
# ============================================================

faces = ["1", "2", "3", "4", "5", "6"]

plt.figure(figsize=(10, 6))

# Barplot for observed values
plt.bar(
    faces,
    observed_values,
    label="Observed Values"
)

# Plot expected values line
plt.plot(
    faces,
    expected_values,
    marker="o",
    linewidth=2,
    label="Expected Values"
)

# Add title
plt.title("Observed vs Expected Frequencies")

# Labels
plt.xlabel("Dice Faces")
plt.ylabel("Frequency")

# Show legend
plt.legend()

# Show graph
plt.show()


# ============================================================
#                    QUESTION 2
# ============================================================
#
# A study investigates whether there is
# a relationship between:
#
# - Gender
# - Preferred Music Genre
#
# Test at 5% significance level whether
# there is a significant association.
#
# ============================================================

print("\n========== QUESTION 2 : TEST OF INDEPENDENCE ==========\n")


# ============================================================
#                  OBSERVED TABLE
# ============================================================

# Row 1 -> Male
# Row 2 -> Female

row1 = np.array([40, 45, 25, 10])
row2 = np.array([35, 30, 20, 30])

# Observed frequency table
observed_table = np.array([row1, row2])

print("Observed Frequency Table:\n")
print(observed_table)


# ============================================================
#                 HYPOTHESIS FORMULATION
# ============================================================

print("\nNull Hypothesis (H0):")
print("No association exists between gender and music preference")

print("\nAlternative Hypothesis (Ha):")
print("Association exists between gender and music preference")


# ============================================================
#                 ROW TOTALS
# ============================================================

row_totals = np.sum(observed_table, axis=1)

print("\nRow Totals:")
print(row_totals)


# ============================================================
#                COLUMN TOTALS
# ============================================================

column_totals = np.sum(observed_table, axis=0)

print("\nColumn Totals:")
print(column_totals)


# ============================================================
#                  GRAND TOTAL
# ============================================================

grand_total = np.sum(observed_table)

print("\nGrand Total:")
print(grand_total)


# ============================================================
#              EXPECTED FREQUENCY TABLE
# ============================================================
#
# Formula:
#
# Expected =
# (Row Total × Column Total)
# ---------------------------
#      Grand Total
#
# ============================================================

expected_table = (
    np.outer(row_totals, column_totals)
    /
    grand_total
)

print("\nExpected Frequency Table:\n")
print(expected_table)


# ============================================================
#                CHI-SQUARE CALCULATION
# ============================================================

chi_calculated = np.sum(
    ((observed_table - expected_table) ** 2)
    /
    expected_table
)

# Degree of freedom
# df = (rows - 1) * (columns - 1)

degree_of_freedom = (
    (observed_table.shape[0] - 1)
    *
    (observed_table.shape[1] - 1)
)

# Critical value
chi_critical = st.chi2.ppf(
    1 - alpha,
    degree_of_freedom
)

# P-value
p_value = 1 - st.chi2.cdf(
    chi_calculated,
    degree_of_freedom
)


# ============================================================
#                     PRINT RESULTS
# ============================================================

print("\nCalculated Chi-Square :", round(chi_calculated, 4))
print("Critical Chi-Square   :", round(chi_critical, 4))
print("P-Value               :", round(p_value, 6))


# ============================================================
#                     FINAL DECISION
# ============================================================

if chi_calculated > chi_critical:
    print("\nResult: Reject H0")
    print("Conclusion: Significant association exists")
else:
    print("\nResult: Fail to Reject H0")
    print("Conclusion: No significant association exists")


# ============================================================
#                 HEATMAP VISUALIZATION
# ============================================================

plt.figure(figsize=(8, 5))

# Create heatmap
sns.heatmap(
    observed_table,
    annot=True,
    fmt=".0f"
)

# Add title
plt.title("Observed Frequency Heatmap")

# Axis labels
plt.xlabel("Music Genres")
plt.ylabel("Gender")

# Show graph
plt.show()


# ============================================================
#               EXPECTED FREQUENCY HEATMAP
# ============================================================

plt.figure(figsize=(8, 5))

# Heatmap for expected values
sns.heatmap(
    expected_table,
    annot=True,
    fmt=".2f"
)

# Add title
plt.title("Expected Frequency Heatmap")

# Labels
plt.xlabel("Music Genres")
plt.ylabel("Gender")

# Show graph
plt.show()


# ============================================================
#                  IMPORTANT POINTS
# ============================================================

"""
1. Chi-Square Test
-------------------
- Used for categorical data

2. Goodness of Fit Test
------------------------
- Checks whether observed data
  matches expected data

3. Test of Independence
------------------------
- Checks relationship between
  two categorical variables

4. P-Value
------------
- If P-Value < 0.05
  -> Reject H0

- If P-Value >= 0.05
  -> Fail to Reject H0

5. Degree of Freedom
---------------------
Goodness of Fit:
df = n - 1

Test of Independence:
df = (rows - 1) × (columns - 1)
"""


# ============================================================
#                        CONCLUSION
# ============================================================

print("\n========== CONCLUSION ==========\n")

print("""
Chi-Square Test is an important
statistical hypothesis testing method.

Types Covered:
- Goodness of Fit Test
- Test of Independence

These tests help us:
- Compare observed and expected values
- Find associations between variables
- Make statistical decisions

These concepts are useful in:
- Data Science
- Machine Learning
- Business Analytics
- Research Analysis
""")