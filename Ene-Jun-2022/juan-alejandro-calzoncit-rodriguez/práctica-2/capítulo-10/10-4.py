file_name = 'guest_book.txt'

def greeting(nm):
    return f"It's nice to meet you {nm}"

x = 0
while x < 5:
    name = input('Hi!, please type your name : ')
    print(greeting(name))

    with open(file_name, 'a') as file_object:
        file_object.write(name + '\n')

    x += 1