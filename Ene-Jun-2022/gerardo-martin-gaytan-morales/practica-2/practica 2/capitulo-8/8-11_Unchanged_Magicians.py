def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    # Build a new list to hold the great musicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)

    return magicians

magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)

print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print("\nOriginal magicians:")
show_magicians(magicians)
