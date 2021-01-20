
from Ejercicio1 import *

def disco():
    print('')

def decorador(function):
    def wrapper():
        print('Pura rola buena papá lml')
        function()
        print('Fin de la lista.')


    return wrapper

    x = decorador(disco)
    disco()
    x()


@decorador
def disco():
	print('')

disco()

def nueva(function):
    def wrapper():
        print('Desea agregar otra melodia?')
        if print() == 'si':
            print("Porfavor corre de nuevo el programa")
        else:
            print("Ayos!")

    return wrapper

