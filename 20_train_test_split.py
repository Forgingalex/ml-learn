# Learning about Train-Test Split
# This is a crucial concept in machine learning!

import numpy as np
from sklearn.model_selection import train_test_split

# Why split data?
# - Training set: Used to teach the model
# - Test set: Used to evaluate how well the model works on new, unseen data
# - We don't want to test on the same data we trained on (that would be cheating!)

# Creating some sample data
# Let's say I have house sizes and prices
house_sizes = np.array([50, 60, 70, 80, 90, 100, 110, 120, 130, 140])
house_prices = np.array([100000, 120000, 140000, 160000, 180000, 200000, 220000, 240000, 260000, 280000])

print("Original data:")
print("Sizes:", house_sizes)
print("Prices:", house_prices)
print("Total samples:", len(house_sizes))

# Splitting the data
# test_size=0.2 means 20% goes to test, 80% goes to train
# random_state=42 makes the split reproducible (same every time)
X_train, X_test, y_train, y_test = train_test_split(
    house_sizes, house_prices, test_size=0.2, random_state=42
)

print("\nAfter splitting:")
print("Training set size:", len(X_train))
print("Training sizes:", X_train)
print("Training prices:", y_train)

print("\nTest set size:", len(X_test))
print("Test sizes:", X_test)
print("Test prices:", y_test)

# Why is this important?
# - I train the model on X_train and y_train
# - I test the model on X_test and y_test
# - This tells me if the model can predict well on NEW data it hasn't seen before

# Common split ratios:
# - 80/20 (80% train, 20% test) - common
# - 70/30 (70% train, 30% test) - also common
# - Depends on how much data you have

print("\nKey takeaway:")
print("Always split your data before training!")
print("This prevents overfitting and gives honest performance estimates.")

