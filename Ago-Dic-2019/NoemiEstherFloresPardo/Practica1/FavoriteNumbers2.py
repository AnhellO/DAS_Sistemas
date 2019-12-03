"""6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers."""

favorite_numbers = {
    'Lupita': [10,17],
    'Reynaldo': [24,42],
    'Samuel': [7,14],
    'Teresa': [21,26],
    'Rosendo': [12,24]
    }

for name, numbers in favorite_numbers.items():
    print("\nA " + name.title() + " le gustan los siguientes numeros:")
    for number in numbers:
        print("  " + str(number))