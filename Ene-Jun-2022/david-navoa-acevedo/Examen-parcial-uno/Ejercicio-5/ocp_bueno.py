from abc import ABC,abstractclassmethod

#Interfaz animal que cumple con lo requerido de entregar un sonido
#En cazo de necesitar mas cosas solo se crea otra interfaz pasando Animal como herencia
#y agregarle mas funcionalidades
class Animal(ABC):
    @abstractclassmethod
    def get_nombre(self):
        pass
    @abstractclassmethod
    def get_sonido(self):
        pass
    
#Clase Perro para prueba
class Perro(Animal):
    def __init__(self):
        self.__nombre = "Perro"
        self.__sonido = "Woof"
    def get_nombre(self):
        return self.__nombre
    def get_sonido(self):
        return self.__sonido
    def __str__(self):
        return "animal: {animal}, sonido: {sonido}".format(animal = self.__nombre, sonido = self.__sonido)
#Clase Gato para prueba
class Gato(Animal):
    def __init__(self):
        self.__nombre = "Gato"
        self.__sonido = "Meow"
    def get_nombre(self):
        return self.__nombre
    def get_sonido(self):
        return self.__sonido
    def __str__(self):
        return "animal: {animal}, sonido: {sonido}".format(animal = self.__nombre, sonido = self.__sonido)

#Interfaz de acciones para cualquier funcion que se vaya a hacer en un futuro con los animales
class Acciones(ABC):
    def __init__(self, obj):
        self.obj = obj
    @abstractclassmethod
    def accion_principal(self) -> str:
        pass
#Clase para conseguir el sonido de los animales entregados
class Sonido_de_animales(Acciones):
    def accion_principal(self):
        return "{sonido}".format(sonido = self.obj.get_sonido())

#El metodo main que usara/probara todo el codigo ya creado
def main():
    perro = Perro()
    gato = Gato()
    animalitos = (perro, gato)
    for animal in animalitos:
        sonido = Sonido_de_animales(animal)
        print(sonido.accion_principal())

if __name__ == "__main__":
    main()
