'''Try these short programs to get some firsthand experience with Python’s lists.
    You might want to create a new folder for each chapter’s exercises to keep
    them organized.'''

'''3-1. Names: Store the names of a few of your friends in a list called names. Print
each person’s name by accessing each element in the list, one at a time.'''

names = ['Luis', 'Alejandro', 'Pablo', 'Jared', 'Fernando', 'Jhonatan']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])

'''3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
printing each person’s name, print a message to them. The text of each message
should be the same, but each message should be personalized with the
person’s name.'''

for i in names:
    print(f"Como estas {i} chiquilla chiflada")

'''3-3. Your Own List: Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle.”'''

transport = ['carro', 'camioneta', 'tren', 'avion', 'barco', 'bicicleta']
message1 = (f"Me gustaria tener un {transport[3].title()} para ir a Disney Land")
message2 = (f"Me gustaria tener un {transport[4].title()} para salir con unas nenas")
message3 = (f"Me gustaria tener un {transport[2].title()} para viajar como los vaqueros")

print(message1)
print(message2)
print(message3)