# Learning about lists - they store multiple items in order
# Lists are like containers that can hold many things

# Creating a list
fruits = ["apple", "banana", "orange"]
print(fruits)

# Lists can hold different types of data
mixed_list = ["apple", 42, 3.14, True]
print(mixed_list)

# I can access items in a list by their position (index)
# The first item is at position 0
print(fruits[0])  # This is "apple"
print(fruits[1])  # This is "banana"
print(fruits[2])  # This is "orange"

# I can change items in a list
fruits[0] = "grape"
print(fruits)  # Now it's ["grape", "banana", "orange"]

# I can add items to a list
fruits.append("mango")  # Adds to the end
print(fruits)

# I can insert items at a specific position
fruits.insert(1, "kiwi")  # Inserts "kiwi" at position 1
print(fruits)

# I can remove items
fruits.remove("banana")  # Removes "banana"
print(fruits)

# I can find the length of a list
print("Number of fruits:", len(fruits))

# I can check if something is in a list
print("apple" in fruits)  # True or False

# I can get a range of items (slicing)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])  # Gets items from position 2 to 4 (not including 5)

# I can loop through a list (we'll learn loops next, but here's a preview)
for fruit in fruits:
    print("I like", fruit)

