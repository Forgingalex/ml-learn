# Training my first Linear Regression model using scikit-learn!
# This is exciting - I'm actually doing machine learning now!

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# First, I need to install scikit-learn (pip install scikit-learn)
# Then I can import it

# Creating sample data
# Let's say I have data about house sizes and their prices
house_sizes = np.array([50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]).reshape(-1, 1)
house_prices = np.array([100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320])

print("Training data:")
print("House sizes:", house_sizes.flatten())
print("House prices:", house_prices)

# Splitting into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    house_sizes, house_prices, test_size=0.2, random_state=42
)

print(f"\nTraining set: {len(X_train)} samples")
print(f"Test set: {len(X_test)} samples")

# Creating and training the model
# This is the exciting part!
model = LinearRegression()

# Training the model (this is where it learns!)
model.fit(X_train, y_train)

# After training, the model has learned the relationship
# I can see what it learned:
print("\nModel learned:")
print(f"Slope (coefficient): {model.coef_[0]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")

# This means the model's equation is approximately:
# price = (slope) * size + intercept

print("\nModel equation:")
print(f"price = {model.coef_[0]:.2f} * size + {model.intercept_:.2f}")

# The model is now trained and ready to make predictions!
# Next file, I'll use it to make predictions

print("\nSuccess! My first ML model is trained!")
print("The model has learned the relationship between house size and price.")

