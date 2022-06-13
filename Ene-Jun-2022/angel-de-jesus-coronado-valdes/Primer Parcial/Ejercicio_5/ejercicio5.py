from abc import ABC, abstractmethod

# tenemos una clase animal abtracta que va a heredar
# a las de mas clases de animales sus metodos abtracto
class Animal(ABC):
    # metodo abtracto para retornar nombre
    @abstractmethod
    def get_nombre(self):
        pass
    # metodo abtracto para retornar sonido
    @abstractmethod
    def get_sonido(self):
        pass


# aqui tenemos y se agregan diferentes tipos de clases
# cada que se quiera agregar un nuevo animal al programa
class León(Animal): 
    def get_nombre(self):# retorna nombre del animal
        return "león"
    
    def get_sonido(self):# retorna sonido del animal
        return "roar"

class Raton(Animal): 
    def get_nombre(self):# retorna nombre del animal
        return "ratón"
    
    def get_sonido(self):# retorna sonido del animal
        return "squeak"

class Cerdo(Animal): 
    def get_nombre(self):# retorna nombre del animal
        return "cerdo"
    
    def get_sonido(self):# retorna sonido del animal
        return "oink"


# codigo cliente animal 
class ClienteAnimal:
    #constructor nos resive una lista de animales existentes
    # y un nombre a buscar para obtener el sonido del animal
    def __init__(self,animals:list,nombre:str):
        self.animals = animals
        self.nombre = nombre
    
    # metodo para buscar al animal elegido
    def sonido(self):
        count = 0 # nos ayudara a contar las iteraciones en nuestro for
        for animal in self.animals:# recorre la lista de animales
            count += 1
            
            # si el animal existe retorna el sonido del animal
            if animal.get_nombre() == self.nombre:
                return "El "+animal.get_nombre()+" hace: '"+animal.get_sonido()+"'"
            
            # si el contador es igual al tamaño de la lista y no retorno el sonido
            # siginifica que el animal no exites y retornara  que el animal no exixte
            elif animal.get_nombre() != self.nombre and count == len(self.animals):
                return "El animal no esta registrado"


def main():
    # lista de las clases de animales que estan registrados
    animales = [
    León(),
    Raton(),
    Cerdo()
    ]
    
    # instanciamos la clase cliente y mandando en sus parametros
    # la lista de animales y el animal a buscar para escuchar su sonido
    animal = ClienteAnimal(animales,"león")
    
    #imprimir el sonido o el mensaje de que no existe el animal
    print(animal.sonido())
    
if __name__ == "__main__":
    main()
