""" 10-1. Learning Python: Open a blank file in your text editor and write
a few lines summarizing what you've learned about Python so far. Start each
line with the phrase In Python you can.... Save the file as learning_python.txt
in the same directory as your exercises from this chapter. Write a program that
reads the file and prints what you wrote three times. Print the contents once by
reading in the entire file, once by looping over the file object, and once by
storing the lines in a list and then working with them outside the with block. """

filename = "learning_python.txt"

print(f"\nReading \"{filename}\" - 1st time:")
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

print(f"\nReading \"{filename}\" - 2nd time:")
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

print(f"\nReading \"{filename}\" - 3rd time:")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

# Reading "learning_python.txt" - 1st time:
# In Python you can do Data Analytics
# In Python you can program an AI algorithm
# In Python you can create GUI applications
# In Python you can do Data Visualization

# Reading "learning_python.txt" - 2nd time:
# In Python you can do Data Analytics
# In Python you can program an AI algorithm
# In Python you can create GUI applications
# In Python you can do Data Visualization

# Reading "learning_python.txt" - 3rd time:
# In Python you can do Data Analytics
# In Python you can program an AI algorithm
# In Python you can create GUI applications
# In Python you can do Data Visualization
