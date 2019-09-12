'''Try It Yourself'''
'''3-8. Seeing the World: Think of at least five places in the world you’d like to
visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly,
just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the
actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse alphabetical order without changing
the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse() to change the order of your list. Print the list to show that its
order has changed.
• Use reverse() to change the order of your list again. Print the list to show
it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the
list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse alphabetical order.
Print the list to show that its order has changed.'''

places = ['Disney Land', 'Paris', 'España', 'Noruega']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.reverse()
print(places)

'''3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
through 3-7 (page 46), use len() to print a message indicating the number
of people you are inviting to dinner'''
guest = ['Antonio Banderas', 'Halle Berry']
print(f"Invite a cenar a {len(guest)} personas")

'''3-10. Every Function: Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or anything
else you’d like. Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once.'''

things =['Hawai', 'Rols Roy', 'Lasaña']
things.pop()
things.insert(1, "Lasaña X2")
things.insert(0, "PS4")
things.append("Angelina Jolie")
things.append("Disney Land")
print("Aqui esta la lista de las cosas que deseo:")

for i in things:
   print(i)

print(f"El total es: {len(things)}")
print(f"Pero solo puedo tener 4: asi que dos se iran, pero primero las ordenare")
things.sort()
print("Cosas ordenadas: ")

for i in things:
    print(i)

print("Se van a ir dos, el utlimo de la lista y el #3: ")
ultimo = things.pop()
No3 = 'Hawai'
things.remove(No3)
print(f"{ultimo}" + f"\n{No3}")
print("Las cosas se reducen a 3 :( y se va el ultimo")
del things[3]
print("Ahora los ordenamos al reves")
things.reverse()

for i in things:
    print(i.title())

print("Con eso soy feliz <3")

'''3-11. Intentional Error: If you haven’t received an index error in one of your
programs yet, try to make one happen. Change an index in one of your programs
to produce an index error. Make sure you correct the error before closing
the program.'''

print("Aqui el error intencional es imprimir en things el elemento 5 de la lista")
#print(things[5].title())