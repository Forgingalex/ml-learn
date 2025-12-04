# Learning about tuples - like lists but they can't be changed
# Tuples use parentheses instead of square brackets

# Creating a tuple
coordinates = (3, 5)
print(coordinates)

# Tuples can hold multiple items
person = ("Alice", 25, "Engineer")
print(person)

# I can access items in a tuple (same as lists)
print(person[0])  # This is "Alice"
print(person[1])  # This is 25

# The difference: I CANNOT change a tuple after creating it
# This would cause an error:
# coordinates[0] = 10  # This doesn't work!

# But I can create a new tuple
new_coordinates = (10, 20)
print(new_coordinates)

# Why use tuples? They're useful when I want to make sure data doesn't change
# For example, storing a date that shouldn't be modified
birth_date = (1990, 5, 15)
print("Birth date:", birth_date)

# I can convert a list to a tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)

# I can convert a tuple to a list
my_list_again = list(my_tuple)
print(my_list_again)

# I can find the length of a tuple
print("Length of tuple:", len(person))

# I can check if something is in a tuple
print("Alice" in person)  # True

