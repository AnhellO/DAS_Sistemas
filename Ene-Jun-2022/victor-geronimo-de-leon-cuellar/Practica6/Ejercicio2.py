class Oveja:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def set_nombre(self, nombre):
        self.nombre

    def get_nombre(self):
        return self.nombre

    def set_tipo(self, tipo):
        self.tipo

    def get_tipo(self):
        return self.tipo  


class dolly():

    def rutinadolly(self):
        self.descanso()
        self.dormir()
        self.alimento()
        self.comer()
        self.ejercicio()
        self.Caminar()

    def descanso(sel):
        pass

    def dormir(self):
        print("Esta durmiendo")

    def alimento(sel):
        pass

    def comer(self):
        print("Es hora de comer")    

    def ejercicio(sel):
        pass

    def Caminar(self):
        print("A caminar")

class prueba(dolly):

    def case(self) -> None:
        return "Caso 1"


class Test(dolly):

    def nuevo(self) -> None:
        return "Haciendo algo nuevo"

    def cargar(self) -> None:
        return "Recargando"

def client_code(addres: dolly) -> None:
    add = []
    add.append(addres.descanso())
    add.append(addres.dormir())
    add.append(addres.alimento())
    add.append(addres.comer())
    add.append(addres.ejercicio())
    add.append(addres.caminar())
    
    for i in add:
        if i != None:
            print(i)

if __name__ == "__main__":
    
    Test(prueba())
    print("Yeah")