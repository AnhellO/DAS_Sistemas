# Tuplas

t = (1, 2, 3)
# t[1] = 10 -> Esto va a tirar un error!
print(t)
print(len(t))

# Diccionarios

dictionary = {
    "empleado-1": 19109012,
    "empleado-2": 19109013,
}

print(dictionary)
print(dictionary["empleado-1"])
dictionary['empleado-3'] = 12348503
print(dictionary["empleado-3"])
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

for llave, valor in dictionary.items():
  print(llave, valor)

# Unpacking

x, y, z = dictionary.keys()
x, y, z = [z, y, x]
print(x, y, z)
print(dictionary.get("empleado-4", -1))
print(*[i for i in range(0, 10, 2)])

# Clases y Objetos

class Videojuego:
    
    def __init__(self, **args):
        self.__nombre = args.get('nombre', '')
        self.__genero = args.get('genero', '')
        self.__precio = args.get('precio')
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_genero(self, genero):
        self.__genero = genero
        
    def set_precio(self, precio):
        self.__precio = precio
    
    def get_nombre(self):
        return self.__nombre
    
    def get_genero(self):
        return self.__genero
    
    def get_precio(self):
        return self.__precio
    
    def __str__(self):
        # return "Nombre: " + self.__nombre + "\nGenero: " + self.__genero -> Concatenando strings
        # return "Nombre: {}\nGénero: {}".format(self.__nombre, self.__genero) -> Función format
        return f"Nombre: {self.__nombre.upper()}\nGénero: {self.__genero.upper()}\nPrecio: {self.__precio}" # -> f String desde python 3.5 o 3.6
    
game = Videojuego(precio=70.5, nombre='Zelda')
print(game)
game.set_nombre('Calofdiuri')
print(game.get_nombre())
game.set_genero('Shooter')
print(game.get_genero())