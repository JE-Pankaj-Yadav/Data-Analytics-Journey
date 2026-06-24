# ============================================================
#                    NUMPY COMPLETE PRACTICE
# ============================================================
#
# Topics Covered:
#
# 1. Arrays
# 2. Shape, Size, ndim
# 3. Indexing
# 4. Slicing
# 5. Boolean Filtering
# 6. Broadcasting
# 7. Vectorization
# 8. Mathematical Functions
# 9. Statistical Functions
# 10. Reshape
# 11. NaN Handling
# 12. Random Numbers
# 13. Transpose
# 14. Axis Operations
# 15. Sorting
# 16. Unique Values
# 17. Where Function
# 18. Array Manipulation
# 19. Stacking and Splitting
#
# ============================================================
#
# What is NumPy?
#
# NumPy is a Python library used for:
# - Fast mathematical calculations
# - Working with arrays
# - Data Science
# - Machine Learning
# - Data Analysis
#
# Main Advantage:
# NumPy is faster than Python lists.
#
# ============================================================


# =========================
# Import NumPy Library
# =========================

import numpy as np


# ============================================================
#                        ARRAYS
# ============================================================
#
# Array:
# A collection of multiple values stored together.
#
# NumPy arrays are:
# - Faster
# - Memory efficient
# - Easy for calculations
#
# ============================================================

print("\n========== ARRAYS ==========\n")

arr = np.array([10, 20, 30, 40, 50])

print(arr)


# ============================================================
#                ARRAY WITH DEFAULT VALUES
# ============================================================

print("\n========== ZEROS ARRAY ==========\n")

# Create array with all zeros
zeros_array = np.zeros(5)

print(zeros_array)


# ============================================================
#                     ONES ARRAY
# ============================================================

print("\n========== ONES ARRAY ==========\n")

# Create array with all ones
ones_array = np.ones((2, 3))

print(ones_array)


# ============================================================
#                     FULL ARRAY
# ============================================================

print("\n========== FULL ARRAY ==========\n")

# Create array with same values
full_array = np.full((2, 3), 7)

print(full_array)


# ============================================================
#                     ARANGE FUNCTION
# ============================================================
#
# arange(start, stop, step)
#
# Used to create sequence of numbers
#
# ============================================================

print("\n========== ARANGE FUNCTION ==========\n")

sequence_array = np.arange(1, 10, 2)

print(sequence_array)


# ============================================================
#                  IDENTITY MATRIX
# ============================================================
#
# Identity Matrix:
# Diagonal values are 1
# Remaining values are 0
#
# ============================================================

print("\n========== IDENTITY MATRIX ==========\n")

identity_matrix = np.eye(4)

print(identity_matrix)


# ============================================================
#                      SHAPE
# ============================================================
#
# Shape:
# Shows rows and columns
#
# ============================================================

print("\n========== ARRAY SHAPE ==========\n")

arr = np.array([
    [4, 2, 3, 8],
    [4, 5, 6, 9]
])

print(arr.shape)


# ============================================================
#                        SIZE
# ============================================================
#
# Size:
# Total number of elements
#
# ============================================================

print("\n========== ARRAY SIZE ==========\n")

arr = np.array([
    [10, 20, 30],
    [45, 69, 74]
])

print(arr.size)


# ============================================================
#                        NDIM
# ============================================================
#
# ndim:
# Number of dimensions
#
# 1D -> One dimension
# 2D -> Two dimension
# 3D -> Three dimension
#
# ============================================================

print("\n========== ARRAY DIMENSIONS ==========\n")

arr1 = np.array([2, 5, 8, 7])

arr2 = np.array([
    [4, 2, 3, 8],
    [4, 5, 6, 9]
])

arr3 = np.array([
    [
        [10, 20, 30],
        [45, 69, 74],
        [5, 6, 7]
    ]
])

print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)


# ============================================================
#                      DATA TYPE
# ============================================================
#
# dtype:
# Shows data type of array
#
# ============================================================

print("\n========== ARRAY DATA TYPE ==========\n")

arr = np.array([10, 2.5, 3, 10])

print(arr.dtype)


# ============================================================
#                   TYPE CONVERSION
# ============================================================

print("\n========== TYPE CONVERSION ==========\n")

arr = np.array([5.2, 6.5, 4, 5.5, 8.1])

print("Before Conversion:")
print(arr.dtype)

# Convert float into integer
int_arr = arr.astype(int)

print("\nAfter Conversion:")
print(int_arr.dtype)

print(int_arr)


# ============================================================
#                MATHEMATICAL OPERATIONS
# ============================================================
#
# NumPy performs calculations very fast.
#
# ============================================================

print("\n========== MATHEMATICAL OPERATIONS ==========\n")

arr = np.array([10, 20, 30, 40, 50])

print("Addition:")
print(arr + 2)

print("\nMultiplication:")
print(arr * 2)

print("\nPower:")
print(arr ** 2)

print("\nSquare Root:")
print(np.sqrt(arr))


# ============================================================
#                STATISTICAL FUNCTIONS
# ============================================================

print("\n========== STATISTICAL FUNCTIONS ==========\n")

arr = np.array([10, 20, 30, 40, 50])

print("Sum:", np.sum(arr))

print("Maximum:", np.max(arr))

print("Minimum:", np.min(arr))

print("Mean:", np.mean(arr))

print("Median:", np.median(arr))

print("Standard Deviation:", np.std(arr))

print("Variance:", np.var(arr))


# ============================================================
#                       INDEXING
# ============================================================
#
# Indexing:
# Access single values
#
# ============================================================

print("\n========== INDEXING ==========\n")

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[0])

print(arr[2])

print(arr[-1])


# ============================================================
#                        SLICING
# ============================================================
#
# Slicing:
# Access multiple values
#
# ============================================================

print("\n========== SLICING ==========\n")

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[1:5])

print(arr[:4])

print(arr[2:])

print(arr[::2])

print(arr[:-1])

print(arr[::-1])


# ============================================================
#                    FANCY INDEXING
# ============================================================

print("\n========== FANCY INDEXING ==========\n")

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[[0, 2, 4]])


# ============================================================
#                  BOOLEAN FILTERING
# ============================================================
#
# Used to filter values using conditions
#
# ============================================================

print("\n========== BOOLEAN FILTERING ==========\n")

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[arr < 25])

print(arr[arr > 30])


# ============================================================
#                       RESHAPE
# ============================================================
#
# reshape():
# Changes array shape
#
# ============================================================

print("\n========== RESHAPE ==========\n")

arr = np.array([10, 20, 30, 40, 50, 60])

reshaped_array = arr.reshape(2, 3)

print(reshaped_array)


# ============================================================
#                     TRANSPOSE
# ============================================================
#
# Transpose:
# Converts rows into columns
#
# ============================================================

print("\n========== TRANSPOSE ==========\n")

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr.T)


# ============================================================
#                RAVEL AND FLATTEN
# ============================================================
#
# Convert multi-dimensional array
# into 1D array
#
# ============================================================

print("\n========== RAVEL AND FLATTEN ==========\n")

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Ravel:")
print(arr.ravel())

print("\nFlatten:")
print(arr.flatten())


# ============================================================
#                 ARRAY MODIFICATION
# ============================================================

print("\n========== INSERT FUNCTION ==========\n")

arr = np.array([10, 20, 30, 40, 50])

new_arr = np.insert(arr, 2, 100)

print(new_arr)


# ============================================================
#                     APPEND
# ============================================================

print("\n========== APPEND FUNCTION ==========\n")

arr = np.array([10, 20, 30])

new_arr = np.append(arr, [40, 50])

print(new_arr)


# ============================================================
#                  CONCATENATE
# ============================================================

print("\n========== CONCATENATE FUNCTION ==========\n")

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

print(np.concatenate((arr1, arr2)))


# ============================================================
#                       DELETE
# ============================================================

print("\n========== DELETE FUNCTION ==========\n")

arr = np.array([10, 20, 30, 40, 50])

print(np.delete(arr, 0))


# ============================================================
#                      STACKING
# ============================================================

print("\n========== STACKING ==========\n")

arr1 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Vertical Stack:")
print(np.vstack((arr1, arr2)))

print("\nHorizontal Stack:")
print(np.hstack((arr1, arr2)))


# ============================================================
#                       SPLIT
# ============================================================

print("\n========== SPLIT FUNCTION ==========\n")

arr = np.array([10, 20, 30, 40, 50, 60])

print(np.split(arr, 3))


# ============================================================
#                    BROADCASTING
# ============================================================
#
# Broadcasting:
# NumPy automatically adjusts shapes
# during calculations.
#
# ============================================================

print("\n========== BROADCASTING ==========\n")

price = np.array([100, 200, 150, 300])

discount = 10

final_price = price - (price * discount / 100)

print(final_price)


# ============================================================
#                    VECTORIZATION
# ============================================================
#
# Vectorization:
# Perform operations without loops.
#
# Faster than Python loops.
#
# ============================================================

print("\n========== VECTORIZATION ==========\n")

arr1 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Addition:")
print(arr1 + arr2)

print("\nMultiplication:")
print(arr1 * arr2)


# ============================================================
#                     AXIS OPERATIONS
# ============================================================
#
# axis = 0 -> Column operation
# axis = 1 -> Row operation
#
# ============================================================

print("\n========== AXIS OPERATIONS ==========\n")

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Column Sum:")
print(np.sum(arr, axis=0))

print("\nRow Sum:")
print(np.sum(arr, axis=1))


# ============================================================
#                    RANDOM NUMBERS
# ============================================================
#
# Random numbers are used in:
# - Machine Learning
# - Data Science
# - Simulations
#
# ============================================================

print("\n========== RANDOM NUMBERS ==========\n")

print("Random Integer:")
print(np.random.randint(1, 100, 5))

print("\nRandom Float:")
print(np.random.rand(5))


# ============================================================
#                         SORTING
# ============================================================

print("\n========== SORTING ==========\n")

arr = np.array([50, 10, 30, 20, 40])

print(np.sort(arr))


# ============================================================
#                    UNIQUE VALUES
# ============================================================

print("\n========== UNIQUE VALUES ==========\n")

arr = np.array([10, 20, 20, 30, 30, 40])

print(np.unique(arr))


# ============================================================
#                    WHERE FUNCTION
# ============================================================
#
# where():
# Used for condition checking
#
# ============================================================

print("\n========== WHERE FUNCTION ==========\n")

arr = np.array([10, 20, 30, 40, 50])

print(np.where(arr > 25))


# ============================================================
#                      NaN HANDLING
# ============================================================
#
# NaN:
# Missing values
#
# ============================================================

print("\n========== NaN HANDLING ==========\n")

arr = np.array([10, 20, np.nan, 30, np.nan])

print("Check NaN:")
print(np.isnan(arr))

print("\nReplace NaN with 0:")
print(np.nan_to_num(arr))

print("\nReplace NaN with 100:")
print(np.nan_to_num(arr, nan=100))


# ============================================================
#                  INFINITE VALUES
# ============================================================

print("\n========== INFINITE VALUES ==========\n")

arr = np.array([10, 20, np.inf, -np.inf, 40])

print(np.isinf(arr))

print(
    np.nan_to_num(
        arr,
        posinf=100,
        neginf=-100
    )
)


# ============================================================
#                IMPORTANT NUMPY TOPICS
# ============================================================
#
# These topics are very important for:
# - Data Science
# - Machine Learning
# - Deep Learning
#
# Important Topics:
#
# 1. Broadcasting
# 2. Vectorization
# 3. Indexing and Slicing
# 4. Boolean Filtering
# 5. Reshape
# 6. Axis Operations
# 7. Random Numbers
# 8. NaN Handling
#
# ============================================================


# ============================================================
#                        CONCLUSION
# ============================================================

print("\n========== CONCLUSION ==========\n")

print("""
NumPy is one of the most important
libraries in Python for Data Science.

It helps in:
- Fast calculations
- Array operations
- Mathematical analysis
- Data preprocessing

Important concepts learned:
- Arrays
- Broadcasting
- Vectorization
- Indexing
- Slicing
- Reshape
- Filtering
- Mathematical Functions
- Statistical Functions

NumPy is widely used in:
- Data Science
- Machine Learning
- Artificial Intelligence
- Deep Learning
""")