import sys
vowels = "aeiouy"
try:
    with open("SPECS.md","r") as in_file:
        txt = in_file.read()
        count = {x:sum([1 for char in txt if char==x])for x in 'aeiouy'}
        print(count)
except FileNotFoundError:
        print("The text file is not found")
        sys.exit(1)