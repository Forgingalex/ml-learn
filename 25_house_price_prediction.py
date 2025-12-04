# My first complete Machine Learning project!
# Using the Boston Housing dataset to predict house prices
# This brings together everything I've learned!

import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Note: load_boston is deprecated in newer sklearn versions
# But I'll use it for this learning project
# In real projects, I'd use a different dataset or load from a file

print("=" * 60)
print("HOUSE PRICE PREDICTION PROJECT")
print("=" * 60)

# Loading the Boston Housing dataset
# This dataset has information about houses in Boston and their prices
try:
    boston = load_boston()
    print("\nDataset loaded successfully!")
except:
    print("\nNote: load_boston is deprecated in newer sklearn versions.")
    print("For this learning project, I'll create a simple dataset instead.")
    # Creating a simple dataset for demonstration
    np.random.seed(42)
    n_samples = 200
    X = np.random.rand(n_samples, 1) * 100 + 50  # House sizes between 50-150
    y = X.flatten() * 2 + np.random.randn(n_samples) * 10  # Prices with some noise
    boston = type('obj', (object,), {'data': X, 'target': y, 'feature_names': ['size']})

# Converting to DataFrame for easier viewing
df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['PRICE'] = boston.target

print(f"\nDataset shape: {df.shape}")
print(f"Number of features: {len(boston.feature_names)}")
print(f"Number of samples: {len(df)}")

# Looking at the data
print("\nFirst few rows of the dataset:")
print(df.head())

print("\nBasic statistics:")
print(df.describe())

# Preparing the data
# X = features (what we use to predict)
# y = target (what we want to predict - house prices)
X = boston.data
y = boston.target

print(f"\nFeatures shape: {X.shape}")
print(f"Target shape: {y.shape}")

# Splitting into training and test sets
# 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nTraining set: {X_train.shape[0]} samples")
print(f"Test set: {X_test.shape[0]} samples")

# Creating and training the model
print("\nTraining the Linear Regression model...")
model = LinearRegression()
model.fit(X_train, y_train)
print("Model trained!")

# Making predictions
print("\nMaking predictions on test set...")
y_pred = model.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\n" + "=" * 60)
print("MODEL EVALUATION RESULTS")
print("=" * 60)
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared (R²) Score: {r2:.4f}")

# Showing some example predictions
print("\n" + "=" * 60)
print("EXAMPLE PREDICTIONS")
print("=" * 60)
print("Actual Price | Predicted Price | Error")
print("-" * 50)
for i in range(min(10, len(y_test))):
    actual = y_test[i]
    predicted = y_pred[i]
    error = abs(actual - predicted)
    print(f"${actual:8.2f}   | ${predicted:8.2f}   | ${error:6.2f}")

# Making a prediction for a new house
print("\n" + "=" * 60)
print("PREDICTING PRICE FOR A NEW HOUSE")
print("=" * 60)
# Using the mean values of all features as an example
new_house = X_test[0:1]  # Taking first test house as example
predicted_price = model.predict(new_house)[0]
print(f"Predicted price: ${predicted_price:.2f}")

print("\n" + "=" * 60)
print("PROJECT COMPLETE!")
print("=" * 60)
print("I've successfully:")
print("1. Loaded a real dataset")
print("2. Prepared the data")
print("3. Split it into train/test sets")
print("4. Trained a Linear Regression model")
print("5. Made predictions")
print("6. Evaluated the model using MSE and R²")
print("\nThis is my first complete machine learning project!")

