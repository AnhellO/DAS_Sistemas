# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so each person can have
# more than one favorite number. Then print each person’s name along with their favorite numbers.

fav_numbers = {
    'Yanily': [9, 5],
    'Maria': [57, 16],
    'Carlos': [73, 18],
    'Luis': [72, 9],
    'Daniel': [11, 3],
    }

for name, numbers in fav_numbers.items():
    print("\n" + name.title() + " likes these numbers:")
    for number in numbers:
        print("  " + str(number))