# Learning about strings (text) and what I can do with them
# Strings have built-in methods (functions) that do useful things

# Creating strings
first_name = "John"
last_name = "Doe"

# Combining strings (concatenation)
full_name = first_name + " " + last_name
print(full_name)

# I can make strings uppercase
text = "hello world"
print(text.upper())  # Makes everything uppercase

# I can make strings lowercase
text = "HELLO WORLD"
print(text.lower())  # Makes everything lowercase

# I can capitalize the first letter
text = "hello world"
print(text.capitalize())  # Makes first letter uppercase

# I can find the length of a string
text = "Python"
print("Length of 'Python':", len(text))  # This is 6

# I can check if something is in a string
text = "I love Python"
print("Python" in text)  # This is True
print("Java" in text)     # This is False

# I can replace parts of a string
text = "I love Java"
new_text = text.replace("Java", "Python")
print(new_text)

# I can split a string into parts
text = "apple,banana,orange"
fruits = text.split(",")  # Splits at commas
print(fruits)  # This creates a list: ['apple', 'banana', 'orange']

# I can access individual characters
text = "Hello"
print(text[0])  # This is 'H' (first character, counting starts at 0)
print(text[1])  # This is 'e'

