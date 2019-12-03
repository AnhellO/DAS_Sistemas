"""3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list."""

invitados = ['Teresa', 'Guadalupe', 'Rosendo']

name = invitados[0].title()
print(name + ", te invito a cenar unos ricos taquitos!")

name = invitados[1].title()
print(name + ", te invito a cenar unos ricos taquitos!")

name = invitados[2].title()
print(name + ", te invito a cenar unos ricos taquitos!")

name = invitados[1].title()
print("\nLo siento, " + name + " no puede llegar a cenar.")

# Cuando Guadalupe no puede
del(invitados[1])
invitados.insert(1, 'Samuel')

# Imprimir las invitaciones de nuevo.
name = invitados[0].title()
print("\n" + name + ", te invito a cenar unos ricos taquitos!")

name = invitados[1].title()
print(name + ", te invito a cenar unos ricos taquitos!")

name = invitados[2].title()
print(name + ", te invito a cenar unos ricos taquitos!")

# Agregando mas personas a la lista.
print("\nAgregando mas personas a la lista")
invitados.insert(0, 'Maria')
invitados.insert(2, 'Reynaldo')
invitados.append('José')

name = invitados[0].title()
print(name + ", te invito a cenar unos ricos taquitos!")

name = invitados[1].title()
print(name + ", te invito a cenar unos ricos taquitos!")

name = invitados[2].title()
print(name + ", te invito a cenar unos ricos taquitos!")

name = invitados[3].title()
print(name + ", te invito a cenar unos ricos taquitos!")

name = invitados[4].title()
print(name + ", te invito a cenar unos ricos taquitos!")

name = invitados[5].title()
print(name + ", te invito a cenar unos ricos taquitos!")