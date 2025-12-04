# Introduction to Pandas - a library for working with data tables
# Pandas makes it easy to work with structured data (like Excel spreadsheets)

# First, I need to install Pandas (pip install pandas)
# Then I can import it
import pandas as pd

# Pandas has two main data structures:
# 1. Series - like a single column of data
# 2. DataFrame - like a table with rows and columns

# Creating a Series (one column of data)
ages = pd.Series([25, 30, 35, 40, 45])
print("Ages Series:")
print(ages)
print("\nMean age:", ages.mean())

# Creating a DataFrame (a table)
# Using a dictionary where keys are column names
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [25, 30, 35, 28],
    "City": ["New York", "London", "Tokyo", "Paris"]
}

df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

# Getting basic information about the DataFrame
print("\nDataFrame shape (rows, columns):", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nData types:")
print(df.dtypes)

# Accessing columns
print("\nAge column:")
print(df["Age"])

# Accessing rows
print("\nFirst row:")
print(df.iloc[0])  # iloc uses position

# Pandas makes it really easy to work with data!
# This is what I'll use for real datasets

