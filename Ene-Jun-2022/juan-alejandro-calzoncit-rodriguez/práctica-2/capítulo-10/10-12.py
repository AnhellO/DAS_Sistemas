import json

def create_num():

    num = input("What is your favorite number? ")
    filename = 'fav_number2.json'

    with open(filename, 'w') as f_obj:
        json.dump(num, f_obj)    


def num_exists():
    try:

        filename = 'fav_number2.json'
        with open(filename) as f_obj:
            fav_num = json.load(f_obj)
        return fav_num            

    except FileNotFoundError:
        return None


def print_user():

    n = num_exists()

    if n:
        print(f"I know your favorite number! It's {n}.")
    else:
        create_num()

print_user()