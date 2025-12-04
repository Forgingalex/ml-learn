# Learning about loops - repeating code multiple times
# Two types: for loops and while loops

# FOR LOOP - when I know how many times to repeat

# Looping through a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print("I like", fruit)

# Looping through numbers using range()
# range(5) gives numbers 0, 1, 2, 3, 4
for i in range(5):
    print("Number:", i)

# range(1, 6) gives numbers 1, 2, 3, 4, 5 (starts at 1, stops before 6)
for i in range(1, 6):
    print("Count:", i)

# range(0, 10, 2) gives 0, 2, 4, 6, 8 (starts at 0, stops before 10, steps by 2)
for i in range(0, 10, 2):
    print("Even:", i)

# Looping through a string
word = "Python"
for letter in word:
    print(letter)

# Looping through a dictionary
student = {"name": "Alice", "age": 20, "grade": "A"}
for key, value in student.items():
    print(key, ":", value)

# WHILE LOOP - repeats while a condition is true

# Counting up
count = 0
while count < 5:
    print("Count is:", count)
    count = count + 1  # Important: change the variable or loop never ends!

# Breaking out of a loop early
for i in range(10):
    if i == 5:
        break  # Stops the loop completely
    print(i)

# Skipping to next iteration
for i in range(10):
    if i == 5:
        continue  # Skips the rest and goes to next iteration
    print(i)

# Practical example: summing numbers
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total = total + num
print("Sum:", total)

