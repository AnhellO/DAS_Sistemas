import json

filename = 'fav_number.json'

with open(filename) as f_obj:
    fav_num = json.load(f_obj)
    print(f"I know your favorite number! It's {fav_num}.")