try:
    file = 'cats.txt'
    with open(file) as file_object:
        print(file_object.read())

    print()

    file = 'dogs.txt'
    with open(file) as file_object:
        print(file_object.read())

except FileNotFoundError:
    pass