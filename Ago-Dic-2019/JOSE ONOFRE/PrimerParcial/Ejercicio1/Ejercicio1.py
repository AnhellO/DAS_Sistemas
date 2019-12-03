from abc import ABCMeta, abstractmethod

class Vehiculo(object):
    ##Clase Traslado
    def traslado(self):
        pass


class Automovil(Vehiculo):
   
    def __init__(self, tipo,marca,modelo):  
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo

    def traslado(self):  
        return "Viajando sobre 4 ruedas"

    def __str__(self):  
        return "Transporte: {}".format(self.traslado())
    
    def get_tipo(self):
        return self.tipo


class Avion(Vehiculo):
    
    def __init__(self, tipo,marca,modelo):  
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo

    def traslado(self):  
        return "Viajando sobre el cielo"

    def __str__(self):  
        return "Transporte: {}".format(self.traslado())

    def get_tipo(self):
        return self.tipo



class Barco(Vehiculo):
    
    def __init__(self, tipo,marca,modelo):  
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo

    def traslado(self):  
        return "Viajando sobre el mar"

    def __str__(self):  
        return "Transporte: {}".format(self.traslado())

    def get_tipo(self):
        return self.tipo


def main():
    # Instanciar los objetos
    Auto1 = Automovil(
        tipo='terrestre',
        marca='Chevrolet',
        modelo='Chevy'

    )  
    print(Auto1)

    Auto2 = Automovil(
        tipo='terrestre',
        marca='Ford',
        modelo='Fiesta'

    )  
    print(Auto2)

    Auto3 = Automovil(
        tipo='terrestre',
        marca='Ford',
        modelo='Lobo'

    )  
    print(Auto3)

    Auto4 = Automovil(
        tipo='terrestre',
        marca='Chevrolet',
        modelo='Camaro'

    )  
    print(Auto4)

    Auto5 = Automovil(
        tipo='terrestre',
        marca='Nissan',
        modelo='Skyline'

    )  
    print(Auto5)

    Avion1 = Avion(
        tipo='aereo',
        marca='British Airways',
        modelo='Boeing 747-400'

    )  
    print(Avion1)

    Avion2 = Avion(
        tipo='aereo',
        marca='United Airlines',
        modelo='Boeing 777'

    )  
    print(Avion2)

    Avion3 = Avion(
        tipo='aereo',
        marca='Airbus',
        modelo='Airbus A340'

    )  
    print(Avion3)

    Avion4 = Avion(
        tipo='aereo',
        marca='US Airways',
        modelo='Airbus A330-300'

    )  
    print(Avion4)

    Avion5 = Avion(
        tipo='aereo',
        marca='McDonell Douglas',
        modelo='MD-80'

    )  
    print(Avion5)

    Barco1 = Barco(
        tipo='maritimo',
        marca='Sunseeker',
        modelo='Manhattan 73'

    )  
    print(Barco1)

    Barco2 = Barco(
        tipo='maritimo',
        marca='Dios',
        modelo='Titanic'

    )  
    print(Barco2)

    Barco3 = Barco(
        tipo='maritimo',
        marca='NE',
        modelo='BAAR'

    )  
    print(Barco3)

    Barco4 = Barco(
        tipo='maritimo',
        marca='MAS',
        modelo='MEME'

    )  
    print(Barco4)

    Barco5 = Barco(
        tipo='maritimo',
        marca='SOH',
        modelo='MANS'

    )  
    print(Barco5)
    print("------------------------------------------------------------")

    lista = [Auto1,Auto2,Auto3,Auto4,Auto5,Avion1,Avion2,Avion3,Avion4,Avion5,Barco1,Barco2,Barco3,Barco4,Barco5]

    def Lista(tipo, lista):
        nueva = []
        for i in range(0,len(lista)):
            if lista[i].get_tipo() == tipo:
                nueva.append(lista[i])
        return nueva

    re = Lista('aereo',lista)
    for i in range(0,len(re)):
        print(re[i])

    
    print(Avion1.get_tipo()) ##Prueba de que me imprime solo los aereos


if __name__ == '__main__':
    main()
