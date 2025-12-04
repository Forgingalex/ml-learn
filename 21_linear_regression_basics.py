# Learning about Linear Regression
# Linear Regression is one of the simplest and most useful ML algorithms

import numpy as np

# What is Linear Regression?
# It finds a straight line that best fits the data
# The line equation: y = mx + b
# - m = slope (how steep the line is)
# - b = intercept (where the line crosses the y-axis)

# Simple example with manual calculation (to understand the concept)

# Sample data: house sizes and prices
X = np.array([50, 60, 70, 80, 90, 100])  # House sizes (features)
y = np.array([100, 120, 140, 160, 180, 200])  # House prices in thousands (target)

print("House sizes (X):", X)
print("House prices (y):", y)

# The goal: find a line y = mx + b that best fits these points
# In real ML, we use algorithms to find m and b automatically
# But let me understand what we're trying to do:

# If I manually estimate:
# When size = 50, price = 100
# When size = 100, price = 200
# So the line goes through (50, 100) and (100, 200)

# Slope (m) = (y2 - y1) / (x2 - x1) = (200 - 100) / (100 - 50) = 100 / 50 = 2
# This means: for every 1 unit increase in size, price increases by 2 (thousand)

# Intercept (b): Using y = mx + b and point (50, 100)
# 100 = 2 * 50 + b
# 100 = 100 + b
# b = 0

# So the line is: y = 2x + 0

# Let's verify with a prediction
size_to_predict = 75
predicted_price = 2 * size_to_predict + 0
print(f"\nFor a house of size {size_to_predict}, predicted price: {predicted_price} thousand")

# In real ML, we use scikit-learn which finds the best m and b automatically
# The algorithm tries different values and picks the ones that minimize error

print("\nKey concepts:")
print("- Linear Regression finds a line that best fits the data")
print("- The line equation: y = mx + b")
print("- We use it to predict continuous values (like prices)")
print("- Next, I'll use scikit-learn to do this automatically!")

