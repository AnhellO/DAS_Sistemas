lenguajes_favoritos = {
     'jen': 'python',    
     'sarah': 'c',    
     'edward': 'ruby',    
     'phil': 'python',
     'pedro':'',
     'juan':'',
     'julio':'',   
}

nombre=lenguajes_favoritos.keys()

lenguaje=lenguajes_favoritos.values()

elemen=lenguajes_favoritos.items()

for nombre, lenguaje in elemen:
    if lenguaje == '':

        print("Porfavor contesta la encuesta es importante ",nombre)

    else:

        print("Gracias por contestar la encuesta ",nombre)        