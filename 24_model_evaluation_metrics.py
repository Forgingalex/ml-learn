# Learning how to evaluate my model - is it making good predictions?
# I need metrics to measure how well my model performs

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Creating and training a model
house_sizes = np.array([50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]).reshape(-1, 1)
house_prices = np.array([100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320])

X_train, X_test, y_train, y_test = train_test_split(
    house_sizes, house_prices, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

print("Actual prices:", y_test)
print("Predicted prices:", y_pred)

# EVALUATION METRICS

# 1. MEAN SQUARED ERROR (MSE)
# - Measures the average squared difference between actual and predicted values
# - Lower is better (closer to 0 is best)
# - Units are squared (so if prices are in thousands, MSE is in thousands squared)
mse = mean_squared_error(y_test, y_pred)
print(f"\nMean Squared Error (MSE): {mse:.2f}")

# 2. ROOT MEAN SQUARED ERROR (RMSE)
# - Square root of MSE
# - Same units as the target variable (easier to interpret)
# - Lower is better
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")

# 3. R-SQUARED (R²) SCORE
# - Measures how well the model explains the variance in the data
# - Range: 0 to 1 (or can be negative for bad models)
# - 1.0 = perfect predictions
# - 0.0 = model is as good as just predicting the mean
# - Higher is better
r2 = r2_score(y_test, y_pred)
print(f"R-squared (R²) Score: {r2:.4f}")

# What do these mean?
print("\nInterpretation:")
print(f"- RMSE of {rmse:.2f} means on average, predictions are off by {rmse:.2f} thousand")
print(f"- R² of {r2:.4f} means the model explains {r2*100:.2f}% of the variance")

# Comparing predictions visually
print("\nComparison:")
for actual, predicted in zip(y_test, y_pred):
    error = abs(actual - predicted)
    print(f"Actual: {actual:.2f}, Predicted: {predicted:.2f}, Error: {error:.2f}")

# These metrics help me understand if my model is good enough!
# For a real project, I'd want:
# - Low MSE/RMSE (small errors)
# - High R² (close to 1.0)

print("\nKey metrics:")
print("- MSE: Lower is better")
print("- RMSE: Lower is better (easier to interpret)")
print("- R²: Higher is better (closer to 1.0)")

