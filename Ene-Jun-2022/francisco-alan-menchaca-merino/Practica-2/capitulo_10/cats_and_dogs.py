""" 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least
three names of cats in the first file and three names of dogs in the second file.
Write a program that tries to read these files and print the contents of the file
to the screen. Wrap your code in a try-except block to catch the FileNotFound error, 
and print a friendly message if a file is missing. Move one of the files to a different
location on your system, and make sure the code in the except block executes properly. """

filename = "cats_and_dogs.txt"


def read_file(file_name):
    try:
        print(f"\nReading the file \"{filename}\"")
        with open(file_name) as file_object:
            content = file_object.read()
            print(content)
    except FileNotFoundError:
        print(f"Sorry, the file \"{file_name}\" does not exist.")


filenames = ["dogs.txt", "cats.txt"]
for filename in filenames:
    read_file(filename)
