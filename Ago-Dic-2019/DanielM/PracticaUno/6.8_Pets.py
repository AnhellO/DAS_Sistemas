# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the name of a pet.
# In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list and as you do print
# everything you know about each pet.

pets = []

pet = {
    'animal type': 'dog',
    'name': 'Skiry',
    'owner': 'Daniel',
    'weight': 8,
    'eats': 'meat and vegetables',
}
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'Rayas',
    'owner': 'Carlos',
    'weight': 5,
    'eats': 'meat',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'Max',
    'owner': 'Luis',
    'weight': 13,
    'eats': 'All',
}
pets.append(pet)

for pet in pets:
    print("\nCheck this info about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))