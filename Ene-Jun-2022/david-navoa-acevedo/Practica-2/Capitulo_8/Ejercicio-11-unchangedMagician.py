magicians_name = ['pedro', 'roberto', 'batman']
the_greath_magicians_name = []

def show_magicians(magicians):
    for magician in magicians:
        print("congats to the magician " + magician)


def make_greath():
    word = 'The greath '
    while magicians_name:
        magician_name_modified = word + magicians_name.pop()
        the_greath_magicians_name.append(magician_name_modified)

    return the_greath_magicians_name

show_magicians(magicians_name)
magicians_name_copy = make_greath()
show_magicians(magicians_name_copy)
