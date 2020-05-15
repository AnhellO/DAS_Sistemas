from modelo import *
from breakingApi import breakingAPI
import logging

def main():
    api = breakingAPI()
    chars = api.get_character()
    for i in chars:
        perso = PERSONAJES.get_or_create(nombre = i["nombre"],fechaNac = i["fechaNac"],ocupacion = str(i["ocupacion"]), imagen = i["imagen"], estado = i["estado"], nickname= i["nickname"], apariciones= str(i["apariciones"]), actor= i["actor"], categoria= i["categoria"])
if __name__ == '__main__':
    main()