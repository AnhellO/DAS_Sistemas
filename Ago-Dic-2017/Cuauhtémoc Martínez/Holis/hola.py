import random

def printHola():
    lista = ['Mundo', 'Hola', 'Guapo', 'Bola', 'Calamardo']

    for x in range(10):
        r = random.randint(0,5)
        print ('Hola', lista[r])


if __name__ == '__main__':
    printHola()
