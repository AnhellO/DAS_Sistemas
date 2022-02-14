""" 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail 
silently if either file is missing. """

filename = "cats_and_dogs.txt"


def read_file(file_name):
    try:
        with open(file_name) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(f"\nReading the file \"{filename}\"")
        print(content)


filenames = ["dogs.txt", "cats.txt"]
for filename in filenames:
    read_file(filename)
