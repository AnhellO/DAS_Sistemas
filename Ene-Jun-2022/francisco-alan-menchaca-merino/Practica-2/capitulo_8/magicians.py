""" 8-9. Magicians: Make a list of magician's names. Pass the list to a function 
called show_magicians(), which prints the name of each magician in the list. """


def show_magicians(magicians_list):
    print("** Magician's names: **")
    for magician in magicians_list:
        print(f"- {magician}")


magicians = [
    "Harry Potter",
    "Hermione Granger",
    "Ron Weasley",
    "Rubeus Hagrid",
    "Lord Voldemort"
]

show_magicians(magicians)
# ** Magician's names: **
# - Harry Potter
# - Hermione Granger
# - Ron Weasley
# - Rubeus Hagrid
# - Lord Voldemort
