filename = "learning_python.txt"

print(f"\nReading \"{filename}\" - 1st time")
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

print(f"\nReading \"{filename}\" - 2nd time")
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

print(f"\nReading \"{filename}\" - 3rd time")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

# Reading "learning_python.txt" - 1st time
# In Python you can make lists
# In Python you can make dictionaries
# In Python you can program

# Reading "learning_python.txt" - 2nd time
# In Python you can make lists
# In Python you can make dictionaries
# In Python you can program

# Reading "learning_python.txt" - 3rd time
# In Python you can make lists
# In Python you can make dictionaries
# In Python you can program