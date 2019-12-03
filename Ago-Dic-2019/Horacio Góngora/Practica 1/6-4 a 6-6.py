'''Try It Yourself'''
'''6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output.'''
words = {'if': 'Sirve para hacer una condicion simple', 'else': 'Sirve para dar resultado a una condicion if que no se cumple', 'elif': 'Sirve para agregar otra condicon si la condicion inicial if no es correcta y se agrega entre un if y else', 'upper': 'Es un metodo de las listas con el cual podemos hacer que todas las letras mayusculas', 'lower': 'Es un metodo de las listas con el cual podemos hacer que todas las letras sean minusculas', 'for': 'Sirve para hacer un ciclo y funciona recorriendo palabras, listas, diccionarios, tuplas, etc...', 'for each': 'sirve para crear listas de comprencion', '.split': 'Sirve para crear una lista apartir de un string', '.keys': 'Sirve para utilizar la llave identificadora en un diccionario', '.values': 'Sirve para regresarnos el valor de una llave'}
for word, definition in words.items():
    print(f"El significado de {word.title()} es :"+f"\n{definition.title()}")

'''6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.'''
rivers = {'Nilo': 'Egipto', 'Rio Bravo': 'Mexico', 'Crystal Lake': 'USA'}
for word, definition in rivers.items():
    if word.title() == 'Nilo' in rivers.keys():
        print(f'La Emperatriz del {word.title()} es Cleopatra y ambos son de {definition.title()}')
    if word.title() == 'Rio Bravo' in rivers.keys():
        print(f'Los indocumentados de America Latina pasan por el  {word.title()} que esta en {definition.title()}')
    if word.title() == 'Crystal Lake' in rivers.keys():
        print(f'En el {word.title()} murio y nacio Jason Voorhees y este locochon es de {definition.title()}')

for word in rivers.keys():
    print(f"Los rios son: {word}")

for definition in rivers.values():
    print(f"Los rios estan en estos paises: {definition}")

'''6-6. Polling: Use the code in favorite_languages.py (page 104).
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.'''
favorite_languages = {'Luis': 'si', 'Jose': 'si', 'Pablo': 'si', 'Vela': 'no', 'Juan': 'no', 'Dany': 'no'}
for name, YoN in favorite_languages.items():
    if YoN == 'si':
        print(f'Gracias por hacer la entrevista {name.title()}')
    else:
        print(f'Deberias hacer la encuesta {name.title()}')