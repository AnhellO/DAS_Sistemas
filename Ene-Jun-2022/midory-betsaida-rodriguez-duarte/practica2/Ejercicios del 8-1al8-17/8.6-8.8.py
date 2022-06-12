#8.6
def nombre_cuidad(ciudad, pais): #es el regresar sin imprimir return
    return ciudad + ", " + pais # tenemos que ponerle los parametros, para ser impresos

print(nombre_cuidad("Monterrey", "Mexico"))
print(nombre_cuidad("Saltillo", "Mexico"))
print(nombre_cuidad("Durango", "Mexico"))

#8.7
def album(artista, titulo, canciones=5):
    return {"nombre": artista, "titulo": titulo, "canción":canciones} #diccionario

print(album("Eminem", "8 miles"))

#8.8
contador = 0

while contador < 2:
    entrada = input("Nombre del artista:")
    titulo = input("Nombre del titulo:")
    canciones = input("Numero de canciónes:")
    
    print(album(entrada, titulo, canciones))
    contador += 1


