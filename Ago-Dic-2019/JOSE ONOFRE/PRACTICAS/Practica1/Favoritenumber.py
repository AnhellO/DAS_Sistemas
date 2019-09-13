favorite_numbers = {
    'Eduardo': [5, 7,19],
    'Miguel': [18, 3, 6],
    'Luis': [7, 11,45],
    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " Le gusta los numeros:")
    for number in numbers:
        print("  " + str(number))