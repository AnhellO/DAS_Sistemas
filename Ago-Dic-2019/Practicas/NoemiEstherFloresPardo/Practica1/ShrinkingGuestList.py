"""3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
• Print a message to each of the two people still on your list, letting them
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program."""

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


print("\nLo siento, solo podemos invitar a dos personas a cenar")

name = invitados.pop()
print("Lo siento, " + name.title() + " no puedo invitarte a cenar")

name = invitados.pop()
print("Lo siento, " + name.title() + " no puedo invitarte a cenar.")

name = invitados.pop()
print("Lo siento, " + name.title() + " no puedo invitarte a cenar.")

name = invitados.pop()
print("Lo siento, " + name.title() + " no puedo invitarte a cenar.")

# Los que iran a cenar
name = invitados[0].title()
print(name + ", te invito a cenar unos ricos taquitos!")

name = invitados[1].title()
print(name + ", te invito a cenar unos ricos taquitos!")

# Eliminar
del(invitados[0])
del(invitados[0])

# Mostrando la lista vacia
print(invitados)