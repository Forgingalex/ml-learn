# Learning NumPy operations - doing math and calculations with arrays
import numpy as np

# Creating some arrays to work with
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print("Array 1:", arr1)
print("Array 2:", arr2)

# Element-wise operations (operations on each element)
print("Addition:", arr1 + arr2)
print("Subtraction:", arr2 - arr1)
print("Multiplication:", arr1 * arr2)
print("Division:", arr2 / arr1)

# Statistical operations
data = np.array([23, 45, 67, 89, 12, 34, 56, 78])
print("\nData:", data)
print("Sum:", np.sum(data))
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard deviation:", np.std(data))
print("Min:", np.min(data))
print("Max:", np.max(data))

# Working with 2D arrays
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nMatrix:")
print(matrix)

# Sum along different axes
print("Sum of all elements:", np.sum(matrix))
print("Sum of each row:", np.sum(matrix, axis=1))  # Sum across columns
print("Sum of each column:", np.sum(matrix, axis=0))  # Sum across rows

# Mean along axes
print("Mean of each row:", np.mean(matrix, axis=1))
print("Mean of each column:", np.mean(matrix, axis=0))

# Finding indices
data = np.array([10, 20, 30, 40, 50])
print("\nData:", data)
print("Index of maximum value:", np.argmax(data))
print("Index of minimum value:", np.argmin(data))

# Sorting
unsorted = np.array([5, 2, 8, 1, 9])
print("\nUnsorted:", unsorted)
print("Sorted:", np.sort(unsorted))

# These operations are super fast even with huge amounts of data!
# That's why NumPy is essential for data science

