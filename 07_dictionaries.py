# Learning about dictionaries - they store pairs of keys and values
# Like a real dictionary: you look up a word (key) to find its meaning (value)

# Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
print(student)

# I can access values using keys
print(student["name"])   # This is "Alice"
print(student["age"])    # This is 20

# I can change values
student["age"] = 21
print(student)

# I can add new key-value pairs
student["major"] = "Computer Science"
print(student)

# I can remove key-value pairs
del student["grade"]
print(student)

# I can get all keys
print("Keys:", student.keys())

# I can get all values
print("Values:", student.values())

# I can check if a key exists
print("name" in student)  # True
print("height" in student)  # False

# Dictionaries can store different types of data
person = {
    "name": "Bob",
    "age": 30,
    "hobbies": ["reading", "coding", "gaming"],  # A list as a value!
    "is_student": False
}
print(person)
print(person["hobbies"][0])  # Gets first hobby: "reading"

# I can loop through a dictionary
for key in student:
    print(key, ":", student[key])

# Dictionaries are really useful for organizing data!
# Like storing information about a person, a product, or anything with attributes

