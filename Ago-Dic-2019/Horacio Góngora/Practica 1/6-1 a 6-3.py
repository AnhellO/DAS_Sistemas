'''Try It Yourself'''
'''6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.'''
person = {'nombre': 'Pablo', 'apellido': 'Rojas', 'edad': 22, 'ciudad': 'zacatecas'}
print(person['nombre'].title())
print(person['apellido'].title())
print(person['edad'])
print(person['ciudad'].title())

'''6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.'''
favorite_number = {'Luis': 14, 'Alex': 25, 'Jhona': 7, 'Pablo': 13, 'Vela': 4}
print(f"Luis tu numero favorito es: {favorite_number['Luis']}")
print(f"Alex tu numero favorito es: {favorite_number['Alex']}")
print(f"Jhona tu numero favorito es: {favorite_number['Jhona']}")
print(f"Pablo tu numero favorito es: {favorite_number['Pablo']}")
print(f"Vela tu numero favorito es: {favorite_number['Vela']}")

'''6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.'''
words = {'if': 'Sirve para hacer una condicion simple', 'else': 'Sirve para dar resultado a una condicion if que no se cumple', 'elif': 'Sirve para agregar otra condicon si la condicion inicial if no es correcta y se agrega entre un if y else', 'upper': 'Es un metodo de las listas con el cual podemos hacer que todas las letras mayusculas', 'lower': 'Es un metodo de las listas con el cual podemos hacer que todas las letras sean minusculas'}
print("El significado de if es:" + f"\n{words['if'].title()}")
print("El significado de else es:" + f"\n{words['else'].title()}")
print("El significado de elif es:" + f"\n{words['elif'].title()}")
print("El significado de upper() es:" + f"\n{words['upper'].title()}")
print("El significado de lower() es:" + f"\n{words['lower'].title()}")