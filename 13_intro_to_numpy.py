# Introduction to NumPy - a library for working with numbers and arrays
# NumPy is the foundation for data science and machine learning in Python

# First, I need to install NumPy (pip install numpy)
# Then I can import it
import numpy as np

# NumPy is great for working with arrays (like lists but faster and more powerful)
# Let me start with simple arrays

# Creating an array from a list
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print("Array from list:", my_array)
print("Type:", type(my_array))

# NumPy arrays can do math operations easily
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Addition:", arr1 + arr2)  # Adds element by element!
print("Multiplication:", arr1 * 2)  # Multiplies each element by 2

# NumPy has useful functions
numbers = np.array([1, 2, 3, 4, 5])
print("Sum:", np.sum(numbers))
print("Mean (average):", np.mean(numbers))
print("Max:", np.max(numbers))
print("Min:", np.min(numbers))

# NumPy is much faster than regular Python lists for large datasets
# This is why it's used in data science and machine learning!

