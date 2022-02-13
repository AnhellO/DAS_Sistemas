filename = 'Learning Python.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip()
    print(line.replace('Python', 'C'))