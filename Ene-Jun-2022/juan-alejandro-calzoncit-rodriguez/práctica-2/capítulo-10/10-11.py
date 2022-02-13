import json

num = input("What is your favorite number? ")
filename = 'fav_number.json'

with open(filename, 'w') as f_obj:
    json.dump(num, f_obj)    