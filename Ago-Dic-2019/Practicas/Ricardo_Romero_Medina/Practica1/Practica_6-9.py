lugar_favorito={
    'Friki Plaza':'Ricardo',
    'Cine':'Jose',
    'Biblioteca':'Juan'
}

lugar=lugar_favorito.keys()

nombre=lugar_favorito.values()

val=lugar_favorito.items()

for lugar,nombre in val:
    print(lugar,'Es el lugar favorito de ',nombre)