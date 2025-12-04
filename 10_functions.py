# Learning about functions - reusable blocks of code
# Functions help me avoid repeating the same code

# Defining a simple function
def greet():
    print("Hello!")

# Calling (using) the function
greet()
greet()  # I can call it multiple times

# Function with parameters (inputs)
def greet_person(name):
    print("Hello,", name)

greet_person("Alice")
greet_person("Bob")

# Function with multiple parameters
def introduce(name, age):
    print("My name is", name, "and I am", age, "years old")

introduce("Alice", 25)

# Function that returns a value
def add_numbers(a, b):
    result = a + b
    return result

sum_result = add_numbers(5, 3)
print("Sum:", sum_result)

# Function with default parameters
def greet_with_title(name, title="Mr."):
    print("Hello,", title, name)

greet_with_title("Smith")  # Uses default "Mr."
greet_with_title("Johnson", "Dr.")  # Uses "Dr." instead

# Function that calculates something
def calculate_area(length, width):
    area = length * width
    return area

room_area = calculate_area(10, 8)
print("Room area:", room_area, "square feet")

# Function with conditional logic
def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

status = check_age(20)
print("Status:", status)

# Function that works with lists
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

my_numbers = [3, 7, 2, 9, 1]
print("Maximum:", find_max(my_numbers))

# Functions make code organized and reusable!
# Instead of writing the same code many times, I write it once in a function

