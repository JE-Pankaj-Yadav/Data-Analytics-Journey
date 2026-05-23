# 📊 Statistics in Python — Complete Guide

A simple and easy collection of Python programs that teach **Statistics** step by step.
These programs are perfect for beginners in **Data Science**, **Machine Learning**, and **Data Analytics**.

---

## 📁 Files in This Project

| File Name | Topic |
|---|---|
| `Measure_of_Central_Tendency.py` | Mean, Median, Mode |
| `Measures_of_Variability.py` | Range, MAD, Variance, Std Dev |
| `Measures_Of_Shape.py` | Skewness, Distribution Shape |
| `Percentiles_And_Quartiles.py` | Percentiles, Quartiles, IQR |
| `Covariance_and_Correlation.py` | Covariance, Correlation, Heatmap |
| `Central_Limit_Theorem.PY` | CLT, Sample Means, Normal Distribution |
| `Z-Test.py` | Z-Test, Hypothesis Testing |
| `T-Test.py` | One Sample, Two Sample, Paired T-Test |
| `Chi_square_Test.py` | Goodness of Fit, Test of Independence |

---

## 📚 Libraries Used

Make sure these libraries are installed before running any file:

```bash
pip install numpy pandas matplotlib seaborn scipy
```

| Library | Use |
|---|---|
| `NumPy` | Mathematical calculations |
| `Pandas` | Data handling and CSV reading |
| `Matplotlib` | Graphs and charts |
| `Seaborn` | Beautiful visualizations |
| `SciPy` | Statistical functions |

---

## 📄 Dataset Requirement

Some files need a **Data.csv** file.
Make sure `Data.csv` is in the **same folder** as the Python files.

Files that need `Data.csv`:
- `Measure_of_Central_Tendency.py`
- `Measures_of_Variability.py`
- `Measures_Of_Shape.py`
- `Percentiles_And_Quartiles.py`
- `Covariance_and_Correlation.py`

---

## 📘 File Details

---

### 1️⃣ Measure_of_Central_Tendency.py

**Topic:** Mean, Median, and Mode

**What it does:**
- Calculates the **Mean** (average value) of the Age column
- Calculates the **Median** (middle value) of the Balance column
- Calculates the **Mode** (most repeated value) of the Region column
- Shows a **Histogram** with Mean, Median, and Mode lines
- Shows a **Count Plot** for the Mode of Region

**Simple explanation:**
> These 3 values help us find the "center" of our data.

```
Mean   → Average of all values
Median → Middle value when data is sorted
Mode   → Value that appears most often
```

---

### 2️⃣ Measures_of_Variability.py

**Topic:** Range, MAD, Variance, Standard Deviation

**What it does:**
- Calculates **Range** = Max value − Min value
- Calculates **Mean Absolute Deviation (MAD)** for two datasets A and B
- Calculates **Variance** for datasets A and B
- Calculates **Standard Deviation** for datasets A and B
- Shows a **Scatter Plot** comparing two datasets
- Shows a **Histogram** of the Age column
- Prints full dataset summary using `describe()`

**Simple explanation:**
> These values tell us how "spread out" the data is.

```
Range  → Difference between largest and smallest value
MAD    → Average distance of values from the mean
Variance       → Measures how far values are from the mean (squared)
Std Deviation  → Square root of variance (most commonly used)
```

---

### 3️⃣ Measures_Of_Shape.py

**Topic:** Skewness and Distribution Shape

**What it does:**
- Loads dataset and calculates Mean, Median, Mode of Age
- Generates random normal data and calculates its **Skewness**
- Shows **Histogram** with Mean, Median, Mode lines for both datasets
- Explains the relationship between Mean, Median, and Mode

**Simple explanation:**
> Skewness tells us if data is leaning to one side.

```
Skewness = 0   → Data is Symmetrical (balanced)
Skewness > 0   → Positive Skew (tail on right side)
Skewness < 0   → Negative Skew (tail on left side)

Symmetrical:        Mean ≈ Median ≈ Mode
Positive Skewed:    Mean > Median > Mode
Negative Skewed:    Mean < Median < Mode
```

---

### 4️⃣ Percentiles_And_Quartiles.py

**Topic:** Percentiles, Quartiles, IQR, Boxen Plot

**What it does:**
- Checks for **missing values** in the dataset
- Calculates **Percentiles** (1st, 25th, 50th, 75th, 100th) of Age
- Calculates **Quartiles** Q1, Q2, Q3 of Age
- Calculates **IQR** (Interquartile Range)
- Shows **Boxen Plots** for Age and Balance columns
- Prints full dataset summary using `describe()`

**Simple explanation:**
> Percentiles and Quartiles tell us how data is divided into parts.

```
Percentile → Value below which a % of data falls
Q1 (25%)   → 25% of data is below this value
Q2 (50%)   → Middle value (same as Median)
Q3 (75%)   → 75% of data is below this value
IQR        → Q3 − Q1 (spread of middle 50% data)
```

---

### 5️⃣ Covariance_and_Correlation.py

**Topic:** Covariance, Correlation, Heatmaps

**What it does:**
- Loads dataset and selects only **numerical columns**
- Calculates and prints the **Correlation Matrix**
- Shows a **Correlation Heatmap** using `coolwarm` colors
- Calculates and prints the **Covariance Matrix**
- Shows a **Covariance Heatmap** using `viridis` colors

**Simple explanation:**
> These values tell us how two variables are related to each other.

```
Correlation:
+1  → Perfect Positive Relationship
 0  → No Relationship
-1  → Perfect Negative Relationship

Covariance:
Positive → Both variables increase together
Negative → One increases, other decreases
```

> **Key difference:** Correlation is easier to understand because its value is always between -1 and +1. Covariance can be any number.

---

### 6️⃣ Central_Limit_Theorem.PY

**Topic:** Central Limit Theorem (CLT)

**What it does:**
- Creates **Population Data** of 10,000 random values
- Shows **KDE Plot** of population data
- Takes **50 random samples**, each of size 1000
- Calculates **mean of each sample**
- Shows **KDE Plot** of sample means
- Compares **Population Mean** vs **Mean of Sample Means**

**Simple explanation:**
> CLT says: If we take many samples and calculate their average, those averages will follow a Normal Distribution — even if the original data is not normal.

```
Population Mean ≈ Mean of Sample Means

Larger sample size → Better approximation
```

---

### 7️⃣ Z-Test.py

**Topic:** Z-Test and Hypothesis Testing

**What it does:**

**Question 1 — Simple Z-Test:**
- Tests if student mean score is greater than 82
- Calculates Z value, Critical Z value, and P-value
- Shows visualization of Z distribution

**Question 2 — Design Z-Test:**
- Compares old website vs new website purchase amounts
- Performs both **Z-Test** and **T-Test**
- Shows histogram comparison of both designs

**Simple explanation:**

```
Z-Test is used when:
✔ Population standard deviation is KNOWN
✔ Sample size is large (n ≥ 30)

Formula:
Z = (Sample Mean − Population Mean) / (Std / √n)

Decision Rule:
If Z calculated > Z critical → Reject H0
If P-Value < 0.05           → Reject H0
```

---

### 8️⃣ T-Test.py

**Topic:** One Sample, Two Sample, and Paired T-Test

**What it does:**

**Question 1 — One Sample T-Test:**
- Tests if average bag weight is less than 150 grams
- Shows T distribution with critical and calculated T values

**Question 2 — Two Sample T-Test:**
- Compares productivity of Team A and Team B
- Two-tailed test with α = 0.05

**Question 3 — Paired T-Test:**
- Compares typing speed before and after training
- Uses `scipy.stats.ttest_rel()`
- Shows histogram of before vs after data

**Simple explanation:**

```
T-Test is used when:
✔ Population standard deviation is NOT known
✔ Sample size is small

One Sample T-Test  → Compare sample mean with population mean
Two Sample T-Test  → Compare means of two different groups
Paired T-Test      → Compare same group before and after

Decision Rule:
If P-Value < 0.05 → Reject H0 (significant difference found)
```

---

### 9️⃣ Chi_square_Test.py

**Topic:** Chi-Square Test

**What it does:**

**Question 1 — Goodness of Fit Test:**
- Tests if a die is fair using 120 rolls
- Compares observed vs expected frequencies
- Shows Bar chart with expected value line

**Question 2 — Test of Independence:**
- Tests if gender and music preference are related
- Calculates expected frequency table
- Shows **Heatmaps** for observed and expected frequencies

**Simple explanation:**

```
Chi-Square Test is used for CATEGORICAL data

Goodness of Fit Test:
→ Checks if observed data matches expected data
→ df = n − 1

Test of Independence:
→ Checks if two variables are related
→ df = (rows − 1) × (columns − 1)

Formula:
χ² = Σ (Observed − Expected)² / Expected

Decision Rule:
If χ² calculated > χ² critical → Reject H0
If P-Value < 0.05              → Reject H0
```

---

## 🧪 How to Run Any File

**Step 1:** Open terminal or VS Code

**Step 2:** Go to the folder where files are saved

```bash
cd your-folder-name
```

**Step 3:** Run any file

```bash
python Measure_of_Central_Tendency.py
python Measures_of_Variability.py
python Measures_Of_Shape.py
python Percentiles_And_Quartiles.py
python Covariance_and_Correlation.py
python Central_Limit_Theorem.PY
python Z-Test.py
python T-Test.py
python Chi_square_Test.py
```

---

## 🧠 Key Concepts Summary

| Concept | Simple Meaning |
|---|---|
| Mean | Average of all values |
| Median | Middle value |
| Mode | Most repeated value |
| Range | Max − Min |
| Variance | How spread data is (squared) |
| Std Deviation | Square root of variance |
| Skewness | How tilted the data distribution is |
| Percentile | Value below which % of data falls |
| IQR | Spread of middle 50% data |
| Correlation | Strength of relationship between variables |
| Covariance | Direction of relationship between variables |
| CLT | Sample means follow normal distribution |
| Z-Test | Hypothesis test when population std is known |
| T-Test | Hypothesis test when population std is unknown |
| Chi-Square | Hypothesis test for categorical data |

---

## ✅ Hypothesis Testing — Quick Reference

```
H0  → Null Hypothesis      (No difference exists)
Ha  → Alternative Hypothesis (Difference exists)
α   → Significance Level   (Usually 0.05)

If P-Value < 0.05  → Reject H0  ✅
If P-Value ≥ 0.05  → Fail to Reject H0 ❌
```

---

## 👨‍💻 Useful For

- 📊 Data Science
- 🤖 Machine Learning
- 📈 Data Analytics
- 🔬 Research and Analysis
- 🏢 Business Analytics

---

> Made with ❤️ for Statistics learners
