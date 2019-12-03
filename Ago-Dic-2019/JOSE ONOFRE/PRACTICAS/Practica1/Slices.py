animales = ['Perro','Gato','Hamster','Conejo','Raton']

for animal in animales:
    print(animal)
    print('Un '+animal.title()+' sería una maravillosa mascota')

print('Cualquiera de estos animales sería una mascota fantastica')

print('//////////////////////////')

print("Los primeros tres elementos de la lista son:")
for animal in animales[:3]:
    print(animal.title())

print('//////////////////////////')

print("Los tres elementos del centro de la lista son:")
for animal in animales[1:4]:
    print(animal.title())

print('//////////////////////////')

print("Los tres ultimos elementos de la lista son:")
for animal in animales[2:]:
    print(animal.title()) 