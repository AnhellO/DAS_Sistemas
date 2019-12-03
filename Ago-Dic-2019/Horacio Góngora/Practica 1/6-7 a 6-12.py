'''Try It Yourself'''
'''6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.'''
person1 = {'nombre': 'Pablo', 'apellido': 'Rojas', 'edad': 22, 'ciudad': 'zacatecas'}
person2 = {'nombre': 'Luis', 'apellido': 'Caseres', 'edad': 24, 'ciudad': 'saltillo'}
person3 = {'nombre': 'Alex', 'apellido': 'Perez', 'edad': 24, 'ciudad': 'saltillo'}
persons = [person1, person2, person3]
for person in persons:
    print(f"Su nombre es {person['nombre']}, se apellida {person['apellido']}, tiene {person['edad']} y es de {person['ciudad']}")

'''6-8. Pets: Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your list
and as you do print everything you know about each pet'''
pets1 = {'ndueño': 'Luis','nmascota': 'Mago', 'tipo': 'Conejo'}
pets2 = {'ndueño': 'Claudia','nmascota': 'Max', 'tipo': 'Schanuzer'}
pets3 = {'ndueño': 'Horacio','nmascota': 'Pinguino', 'tipo': 'Chihuahua'}
pets = [pets1, pets2, pets3]
for pet in pets:
    print(f"{pet['ndueño']} tiene a {pet['nmascota']} como mascota y es un {pet['tipo']}")

'''6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places.'''
favorite_places = {'Luis': {'name': 'luis', 'lugar': 'Nueva Zelanda'}, 'Alex': {'name': 'alex', 'lugar': 'Korea'}, 'Jhona': {'name': 'jhona', 'lugar': 'China'}}
for place, place_info in favorite_places.items():
    print(f'Mi amigo {place_info["name"]} su lugar favorito para ir de viaje es {place_info["lugar"]}')

'''6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.'''
favorite_number = {'luis': {'nombre': 'luis', 'numero1': 7, 'numero2': 15}, 'alex': {'nombre': 'alex', 'numero1': 3, 'numero2': 19}, 'jhona': {'nombre': 'jhona', 'numero1': 4, 'numero2': 67}}
for number, number_info in favorite_number.items():
    print(f'Mi amigo {number_info["nombre"]} sus numeros favoritos son {number_info["numero1"]} - {number_info["numero2"]}')

'''6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information
you have stored about it.'''

cities = {'Saltillo': {'name': 'Saltillo', 'suceso': 'Nace Eulalio Gutierrez' ,'poblacion': 769671, 'pais': 'mexico'}, 'Noruega': {'name': 'Kathegag', 'suceso': 'Nace Ragnar Lovtjbrok', 'poblacion': 100000, 'pais': 'noruega'}, 'España': {'name': 'Barcelona', 'suceso': 'Esta el Barca', 'poblacion': 1615000, 'pais': 'España'}}
for citi, citi_info in cities.items():
    print(f'El nombre de la ciudad es {citi_info["name"]}, es famoso porque {citi_info["suceso"]}, tiene un poblacion estimada de {citi_info["poblacion"]} y esta en el pais de {citi_info["pais"]}')

'''6-12. Extensions: We’re now working with examples that are complex enough
that they can be extended in any number of ways. Use one of the example programs
from this chapter, and extend it by adding new keys and values, changing
the context of the program or improving the formatting of the output'''
ities = {'Saltillo': {'name': 'Saltillo', 'suceso': 'Nace Eulalio Gutierrez' ,'poblacion': 769671, 'pais': 'mexico'}, 'Noruega': {'name': 'Kathegag', 'suceso': 'Nace Ragnar Lovtjbrok', 'poblacion': 100000, 'pais': 'noruega'}, 'España': {'name': 'Barcelona', 'suceso': 'Esta el Barca', 'poblacion': 1615000, 'pais': 'España'}}
for citi, citi_info in cities.items():
    print(f'El nombre de la ciudad es -> {citi_info["name"]}' + f'\nEs famoso porque -> {citi_info["suceso"]}' + f'\nTiene un poblacion estimada de -> {citi_info["poblacion"]}' + f'\nEsta en el pais de -> {citi_info["pais"]}')
