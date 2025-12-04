# Using my trained model to make predictions!
# This is where the magic happens - the model predicts on new data

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Creating and training a model (same as before)
house_sizes = np.array([50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]).reshape(-1, 1)
house_prices = np.array([100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320])

# Splitting the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    house_sizes, house_prices, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

print("Model trained!")
print(f"Slope: {model.coef_[0]:.2f}, Intercept: {model.intercept_:.2f}\n")

# MAKING PREDICTIONS

# Predicting on the test set (data the model hasn't seen during training)
predictions = model.predict(X_test)

print("Predictions on test set:")
print("Actual sizes:", X_test.flatten())
print("Actual prices:", y_test)
print("Predicted prices:", predictions)

# Predicting on a single new house
new_house_size = np.array([[85]])  # A house of size 85
predicted_price = model.predict(new_house_size)
print(f"\nFor a new house of size {new_house_size[0][0]}:")
print(f"Predicted price: {predicted_price[0]:.2f} thousand")

# Predicting on multiple new houses
new_house_sizes = np.array([[55], [95], [125], [155]])
predicted_prices = model.predict(new_house_sizes)

print("\nPredictions for multiple houses:")
for size, price in zip(new_house_sizes.flatten(), predicted_prices):
    print(f"Size {size}: Predicted price {price:.2f} thousand")

# This is amazing! The model can predict prices for houses it has never seen before!
# But how good are these predictions? That's what I'll learn next - evaluation metrics

print("\nKey takeaway:")
print("After training, I can use model.predict() to make predictions on new data!")

