from clases import *

guitarra = Guitarra('cuerdas', 'maple', 'negro', 'diestro', 7)
guitarra.imprime_atributos()

bateria = Bateria('percusión', 'roble', 'plateado', 15)

print(isinstance(guitarra, Guitarra))
print(isinstance(guitarra, Instrumento))
print(isinstance(bateria, Bateria))
print(isinstance(bateria, Instrumento))

bateria.imprime_atributos()
bateria.suena_instrumento()
