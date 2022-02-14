""" 8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the 
function make_great() with a copy of the list of magicians' names. Because the 
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original
names and one list with the Great added to each magician's name. """


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

    return great_magicians


magicians = [
    "Harry Potter",
    "Hermione Granger",
    "Ron Weasley",
    "Rubeus Hagrid",
    "Lord Voldemort"
]

great_magicians = make_great(magicians[:])

print("Original magicians list:")
show_magicians(magicians)

print("\nMagicians list with \"The great magician\" added:")
show_magicians(great_magicians)
# Original magicians list:
# ** Magician's names: **
# - Harry Potter
# - Hermione Granger
# - Ron Weasley
# - Rubeus Hagrid
# - Lord Voldemort

# Magicians list with "The great magician" added:
# ** Magician's names: **
# - The great magician Lord Voldemort
# - The great magician Rubeus Hagrid
# - The great magician Ron Weasley
# - The great magician Hermione Granger
# - The great magician Harry Potter
