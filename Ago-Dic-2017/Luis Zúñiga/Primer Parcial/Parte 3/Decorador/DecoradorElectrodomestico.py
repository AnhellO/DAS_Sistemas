from Electrodomestico import Electrodomestico

class DecoradorElectrodomestico(Electrodomestico):

    def __init__(self, electrodomestico):
        self.__electrodomestico = electrodomestico

    def imprimeAtributos(self):
        self.__electrodomestico.imprimeAtributos()
        print('''
        Ahora soy también un robot
        ''')