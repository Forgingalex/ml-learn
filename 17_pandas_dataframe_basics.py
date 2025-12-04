# Learning more about Pandas DataFrames - the basics
import pandas as pd

# Creating a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age": [25, 30, 35, 28, 32],
    "Salary": [50000, 60000, 70000, 55000, 65000],
    "Department": ["IT", "HR", "IT", "Finance", "IT"]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Viewing the data
print("\nFirst 3 rows:")
print(df.head(3))

print("\nLast 2 rows:")
print(df.tail(2))

# Getting basic statistics
print("\nBasic statistics:")
print(df.describe())  # Shows count, mean, std, min, max for numeric columns

# Selecting specific columns
print("\nName and Age columns:")
print(df[["Name", "Age"]])

# Filtering rows (like SQL WHERE clause)
print("\nPeople older than 30:")
print(df[df["Age"] > 30])

print("\nPeople in IT department:")
print(df[df["Department"] == "IT"])

# Adding a new column
df["Bonus"] = df["Salary"] * 0.1  # 10% bonus
print("\nDataFrame with Bonus column:")
print(df)

# Sorting
print("\nSorted by Age:")
print(df.sort_values("Age"))

print("\nSorted by Salary (descending):")
print(df.sort_values("Salary", ascending=False))

# Grouping data
print("\nAverage salary by department:")
print(df.groupby("Department")["Salary"].mean())

# Counting
print("\nNumber of people in each department:")
print(df["Department"].value_counts())

# These operations are super useful for exploring and understanding data!

