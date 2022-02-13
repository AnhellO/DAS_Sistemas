file = 'learning_python.txt'

with open(file) as file_object:

    lines = file_object.readlines()


for line in lines:
    print(line.replace('Python','C++').rstrip())
    