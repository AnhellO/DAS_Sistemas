mascotas = []

mascota = {
'tipo de animal': 'perro',
    'color': 'cafe',
    'nombre': 'Hachiko',
    'dueño': 'Daniel',
}

mascotas.append(mascota)

mascota1 = {
'tipo de animal': 'gato',
    'color': 'naranja',
    'nombre': 'Garfield',
    'dueño': 'Ernesto',
}

mascotas.append(mascota1)

mascota2 = {
'tipo de animal': 'ave',
    'color': 'rojo',
    'nombre': 'Fito',
    'dueño': 'Luisa',
}

mascotas.append(mascota2)

mascota3 = {
'tipo de animal': 'raton',
    'color': 'blanco',
    'nombre': 'coco',
    'dueño': 'Raul',
}

mascotas.append(mascota3)

for mascota in mascotas:
    print("\nLo que se sobre " + mascota['nombre'].title() + " es:")
    for key, value in mascota.items():
        print("\t" + key + ": " + value)