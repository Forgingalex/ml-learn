# Learning more about NumPy arrays - creating different types of arrays
import numpy as np

# Creating arrays with different methods

# Array of zeros
zeros = np.zeros(5)
print("Array of zeros:", zeros)

# Array of ones
ones = np.ones(5)
print("Array of ones:", ones)

# Array with a range of numbers
range_array = np.arange(0, 10, 2)  # Start, stop, step
print("Range array:", range_array)

# Array with evenly spaced numbers
linspace_array = np.linspace(0, 1, 5)  # Start, end, number of points
print("Linspace array:", linspace_array)

# Creating 2D arrays (like a table with rows and columns)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D array (matrix):")
print(matrix)

# Getting the shape (dimensions) of an array
print("Shape of matrix:", matrix.shape)  # (3, 3) means 3 rows, 3 columns

# Creating arrays with specific shape
zeros_2d = np.zeros((3, 4))  # 3 rows, 4 columns
print("2D zeros array:")
print(zeros_2d)

# Reshaping an array
arr = np.arange(12)
print("Original array:", arr)
reshaped = arr.reshape(3, 4)  # Reshape to 3 rows, 4 columns
print("Reshaped array:")
print(reshaped)

# Accessing elements in 2D arrays
print("Element at row 0, column 1:", matrix[0, 1])
print("First row:", matrix[0, :])  # All columns in row 0
print("First column:", matrix[:, 0])  # All rows in column 0

# Arrays are really powerful for organizing data!

