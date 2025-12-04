# Learning how to read from and write to files
# Files let me save data and load it back later

# WRITING TO A FILE

# Opening a file for writing ('w' means write mode)
# If the file doesn't exist, it will be created
file = open("my_data.txt", "w")
file.write("Hello, this is my first file!\n")
file.write("I'm learning Python.\n")
file.write("This is line 3.")
file.close()  # Important: always close the file when done

# A better way using 'with' (automatically closes the file)
with open("my_data.txt", "w") as file:
    file.write("Hello, this is my first file!\n")
    file.write("I'm learning Python.\n")
    file.write("This is line 3.")

# READING FROM A FILE

# Reading the entire file
with open("my_data.txt", "r") as file:
    content = file.read()
    print("File contents:")
    print(content)

# Reading line by line
with open("my_data.txt", "r") as file:
    print("\nReading line by line:")
    for line in file:
        print(line.strip())  # strip() removes the newline character

# Reading all lines into a list
with open("my_data.txt", "r") as file:
    lines = file.readlines()
    print("\nAll lines as a list:")
    print(lines)

# APPENDING TO A FILE (adding to the end)

with open("my_data.txt", "a") as file:  # 'a' means append mode
    file.write("\nThis is a new line added later!")

# Reading again to see the new line
with open("my_data.txt", "r") as file:
    print("\nFile after appending:")
    print(file.read())

# File modes:
# 'r' - read (file must exist)
# 'w' - write (creates new file or overwrites existing)
# 'a' - append (adds to end of file)
# 'x' - create (only if file doesn't exist)

# This is useful for saving data, reading data, and working with datasets!

