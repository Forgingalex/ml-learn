# Learning about conditionals - making decisions in code
# Using if, elif, and else to check conditions

# Basic if statement
age = 18
if age >= 18:
    print("You are an adult")

# If-else statement
age = 15
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# If-elif-else (multiple conditions)
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Comparison operators
x = 10
y = 5

print(x > y)   # Greater than - True
print(x < y)   # Less than - False
print(x >= y)  # Greater than or equal - True
print(x <= y)  # Less than or equal - False
print(x == y)  # Equal to - False
print(x != y)  # Not equal to - True

# Logical operators: and, or, not
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive")

if age < 18 or not has_license:
    print("You cannot drive")

# Checking if something is in a list
fruits = ["apple", "banana", "orange"]
if "apple" in fruits:
    print("Apple is in the list")

# Nested conditionals (if inside if)
temperature = 25
is_sunny = True

if temperature > 20:
    if is_sunny:
        print("Perfect day for a picnic!")
    else:
        print("Warm but cloudy")
else:
    print("It's too cold")

