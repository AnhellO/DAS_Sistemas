from CreateDB import CREATE_DB
from Api import API
from ORM import *

def main():
    #CREA BASE DE DATOS
    CREATE_DB()

    #CREA VARIABLE TIPO API
    data = API()

    #CREA UN ARREGLO DE DICCIONARIOS CON LA INFO DE LA API
    civilizaciones = data.getCiv()
    unidades = data.getUni()
    tecnologias = data.getTec()
    estructuras = data.getEst()

    db.connect()
    
    #ALMACENA INFORMACION DE LA API A LA BD LOCAL
    for i in civilizaciones:
        CIVILIZACIONES.get_or_create(nombre=i.get("nombre"),expansion=i.get("expansion"),tipo=i.get("tipo"))
    
    for i in unidades:
        UNIDADES.get_or_create(nombre=i.get("nombre"),descripcion=i.get("descripcion"),expansion=i.get("expansion"),edad=i.get("edad"),rango=i.get("rango"),ataque=i.get("ataque"))
    
    for i in tecnologias:
        TECNOLOGIAS.get_or_create(nombre=i.get("nombre"),descripcion=i.get("descripcion"),expansion=i.get("expansion"),edad=i.get("edad"))

    for i in estructuras:
        ESTRUCTURAS.get_or_create(nombre=i.get("nombre"), expansion= i.get("expansion"), edad= i.get("edad"), tiempo = i.get("tiempo"))
