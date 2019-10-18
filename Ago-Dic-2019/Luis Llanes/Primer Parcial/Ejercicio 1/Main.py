from Automovil import automovil
from Avion import avion
from Barco import barco

def Filtrar(tipo, lista):
    listaF = []
    for i in range (0,len(lista)):
        if lista[i].get_Tipo() == tipo:
            listaF.append(lista[i])
    return listaF

def main():
    Vehiculo1 = automovil('Terrestre', 'carrito', marca = 'Chevrolet', color = 'rojo')
    Vehiculo2 = automovil('Terrestre', 'Tsuru', marca = 'Nissan', color = 'naranja')
    Vehiculo3 = automovil('Terrestre', 'Spark', marca = 'Chevrolet', color = 'rojo')
    Vehiculo4 = automovil('Terrestre', 'Accent', marca = 'Hyundai', color = 'blanco')
    Vehiculo5 = automovil('Terrestre', 'Aveo', marca = 'Chevrolet', color = 'azul')
    print('------------------------------------------')

    Vehiculo6 = avion('aereo', 'papelito', color = 'blanco', nPasajeros = 5)
    Vehiculo7 = avion('aereo', 'Delux', color = 'Dorado', nPasajeros = 35)
    Vehiculo8 = avion('aereo', 'Turistico', color = 'blanco', nPasajeros = 100)
    Vehiculo9 = avion('aereo', 'Turistico', color = 'azul', nPasajeros = 150)
    Vehiculo10 = avion('aereo', 'Avioneta', color = 'blanco', nPasajeros = 2)
    print('------------------------------------------')

    Vehiculo11 = barco('maritimo', 'pesquero', nombre = 'elisa', color = 'verde', capacidad = 30)
    Vehiculo12 = barco('maritimo', 'Carguero', nombre = 'max', color = 'azul', capacidad = '2 toneladas')
    Vehiculo13 = barco('maritimo', 'crusero', nombre = 'Titanic', color = 'balnco', capacidad = 250)
    Vehiculo14 = barco('maritimo', 'pesquero', nombre = 'churrito', color = 'amarillo', capacidad = 25)
    Vehiculo15 = barco('maritimo', 'crusero', nombre = 'taquito', color = 'dorado', capacidad = 150)

    lista = [Vehiculo1,
    Vehiculo2,Vehiculo3,Vehiculo4,Vehiculo5,Vehiculo6,Vehiculo7,Vehiculo8,Vehiculo9,Vehiculo10,
    Vehiculo11,Vehiculo12,Vehiculo13,Vehiculo14,Vehiculo15]

    listaFiltrada = Filtrar('maritimo',lista)

    for i in range(0,len(listaFiltrada)):
        print(listaFiltrada[i])
        print('----------------------------------')

if __name__ =='__main__':
    main()