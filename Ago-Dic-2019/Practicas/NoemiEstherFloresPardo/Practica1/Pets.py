"""6-8. Pets: Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your list
and as you do print everything you know about each pet."""

# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'dog',
    'name': 'Sorullo',
    'owner': 'Noemi',
    'weight': 8.3,
    'eats': 'meat',
}
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'Silvestre',
    'owner': 'Lupe',
    'weight': 3.2,
    'eats': 'meat',
}
pets.append(pet)

pet = {
    'animal type': 'fish',
    'name': 'nemo',
    'owner': 'Erick',
    'weight': .3,
    'eats': 'sea wrack',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
