""" 8-10. Great Magicians: Start with a copy of your program from Exercise
8-9. Write a function called make_great() that modifies the list of magicians
by adding the phrase the Great to each magician's name. Call show_magicians()
to see that the list has actually been modified."""


def show_magicians(magicians_list):
    print("** Magician's names: **")
    for magician in magicians_list:
        print(f"- {magician}")


def make_great(magicians_list):
    great_magicians = []

    while magicians_list:
        magician = magicians_list.pop()
        magician = "The great magician " + magician
        great_magicians.append(magician)

    for great_magician in great_magicians:
        magicians_list.append(great_magician)


magicians = [
    "Harry Potter",
    "Hermione Granger",
    "Ron Weasley",
    "Rubeus Hagrid",
    "Lord Voldemort"
]

make_great(magicians)
show_magicians(magicians)
# ** Magician's names: **
# - The great magician Lord Voldemort
# - The great magician Rubeus Hagrid
# - The great magician Ron Weasley
# - The great magician Hermione Granger
# - The great magician Harry Potter
