#8.12


def sandiwch(*ingredientes): # el asterisco es para multiples argumentos o sea en printo puse varios argumentos
    print(*ingredientes)

sandiwch("pan", "jamon", "queso")
sandiwch("pan", "jamon")
sandiwch("tomate")

#8.13
def crear_perfil(nombre, apellido, **adicional): #** dos astericos son para poner las llaves
    """Build a dictionary containing everything we know about a user."""
    perfil = {}
    perfil['Nombre'] = nombre
    perfil['Apellido'] = apellido
    for llave, value in adicional.items():
        perfil[llave] = value
    return perfil
usuario = crear_perfil('albert', 'einstein',
localidad='princeton',
profe='physics')
print(usuario)

print(crear_perfil("Midory", "Duarte", estado_civil="Solterona", dedicación="universidad", edad="22"))

#8.14
def coche(marca, color, **adicional):
    carro = {}
    carro['Marca'] = marca
    carro['Color del carro'] = color
    for llave, value in adicional.items():
        carro[llave] = value
    return carro

print(crear_perfil("tsuru", "amarillo", plaqueado="si", es_taxi="no"))




