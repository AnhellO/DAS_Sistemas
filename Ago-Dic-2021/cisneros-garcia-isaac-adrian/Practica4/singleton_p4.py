from abc import ABCMeta, abstractstaticmethod

class Jefe(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_data():
        pass


class ElUnico(Jefe):
    __instance = None

@staticmethod
def get_instance():
    if ElUnico.__instance == None:
        ElUnico("Nombre", "Puesto")
    return ElUnico.__instance

def __init__(self, nombre, puesto):
    if ElUnico.__instance != None:
        raise Exception("No Carnal, así no se puede")
    else:
        self.nombre = nombre
        self.puesto = puesto
        ElUnico.__instance = self

@staticmethod
def print_data():
    print(f"Nombre: {ElUnico.__instance.nombre}, Puesto: {ElUnico.__instance.puesto}")

print("El Jefe es:")
p = ElUnico("Salvador Hernández Vélez","Rector")
print(p)
p.print_data()

