# Learning about data cleaning with Pandas
# Real data is often messy - missing values, duplicates, wrong formats
import pandas as pd
import numpy as np

# Creating a DataFrame with some messy data
data = {
    "Name": ["Alice", "Bob", "Charlie", None, "Eve", "Bob"],
    "Age": [25, 30, None, 28, 32, 30],
    "Salary": [50000, 60000, 70000, None, 65000, 60000],
    "Email": ["alice@email.com", "bob@email.com", "charlie@email.com", "diana@email.com", "eve@email.com", "bob@email.com"]
}

df = pd.DataFrame(data)
print("Messy DataFrame:")
print(df)

# Checking for missing values
print("\nMissing values:")
print(df.isnull())  # Shows True where values are missing

print("\nCount of missing values per column:")
print(df.isnull().sum())

# Handling missing values

# Option 1: Drop rows with any missing values
df_dropped = df.dropna()
print("\nAfter dropping rows with missing values:")
print(df_dropped)

# Option 2: Fill missing values
df_filled = df.copy()
df_filled["Age"].fillna(df_filled["Age"].mean(), inplace=True)  # Fill with mean
df_filled["Salary"].fillna(df_filled["Salary"].mean(), inplace=True)
print("\nAfter filling missing values:")
print(df_filled)

# Finding and removing duplicates
print("\nDuplicate rows:")
print(df.duplicated())

df_no_duplicates = df.drop_duplicates()
print("\nAfter removing duplicates:")
print(df_no_duplicates)

# Checking data types
print("\nData types:")
print(df.dtypes)

# Converting data types if needed
df["Age"] = df["Age"].astype(float)  # Convert to float
print("\nAge column type:", df["Age"].dtype)

# Renaming columns
df_renamed = df.rename(columns={"Name": "Full_Name", "Age": "Years_Old"})
print("\nAfter renaming columns:")
print(df_renamed.columns.tolist())

# Data cleaning is an important step before doing machine learning!
# Clean data = better models

