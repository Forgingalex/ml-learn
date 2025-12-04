# Learning about modules - using code that other people wrote
# Python comes with many built-in modules I can use

# Importing a module
import math

# Using functions from the math module
print("Square root of 16:", math.sqrt(16))
print("Pi:", math.pi)
print("2 to the power of 3:", math.pow(2, 3))

# Importing specific functions
from random import randint, choice

# randint gives a random integer between two numbers
random_number = randint(1, 10)
print("Random number between 1 and 10:", random_number)

# choice picks a random item from a list
fruits = ["apple", "banana", "orange"]
random_fruit = choice(fruits)
print("Random fruit:", random_fruit)

# Importing with an alias (shorter name)
import datetime as dt

# Getting current date and time
now = dt.datetime.now()
print("Current date and time:", now)

# Importing everything from a module (not always recommended, but it works)
from math import *

# Now I can use sqrt without math. prefix
print("Square root of 25:", sqrt(25))

# Some useful built-in modules:
# - math: mathematical functions
# - random: random numbers
# - datetime: dates and times
# - os: operating system functions
# - sys: system-specific functions

# Later I'll learn to import external libraries like NumPy and Pandas
# But for now, I'm using what comes with Python!

