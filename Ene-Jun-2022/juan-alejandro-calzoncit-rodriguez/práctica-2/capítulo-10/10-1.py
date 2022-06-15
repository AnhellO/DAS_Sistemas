file = 'learning_python.txt'

with open(file) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

with open(file) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(file) as file_object:

    lines = file_object.readlines()        

for line in lines:
    print(line.rstrip())