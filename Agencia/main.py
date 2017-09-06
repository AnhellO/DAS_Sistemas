import Agencia, Automovil, Motocicleta, Camion, Vendedor, Cliente

# Listas para trabajar en runtime.

autos = []
motos = []
camiones = []

autos_vendidos = []
motos_vendidas = []
camiones_vendidos = []

cartera_clientes = []

# Dummy data.

def cargar_datos_autos():
    x = Automovil.Automovil('Chevrolet Aveo 2017', 'Rojo', 'Automático', '2.0L',
    '4', 'CHE-AV-S-01', 5, True, 15, 'Sedán')
    autos.append(x)
    x = Automovil.Automovil('Chevrolet Cavalier 2017', 'Azul', 'Automático', '2.0L',
    '4', 'CHE-CA-S-01', 5, True, 13, 'Sedán')
    autos.append(x)
    x = Automovil.Automovil('Chevrolet Spark 2017', 'Plata', 'Manual', '1.8L',
    '4', 'CHE-SP-S-01', 5, False, 17, 'Hatchback')
    autos.append(x)

def cargar_datos_motos():
    x = Motocicleta.Motocicleta('Ducati Monster 1200S 2017', 'Negro', 'Cadena',
    'Testastretta 11° L-Twin', 4, 'DUC-MON-1200S-01', 'Urbana', 1198)
    motos.append(x)
    x = Motocicleta.Motocicleta('Yamaha FJR1300A 2017', 'Rojo', 'Cadena',
    'DOHC', 4, 'YAM-FJR-1300A-01', 'Urbana/Carreras', 998)
    motos.append(x)
    x = Motocicleta.Motocicleta('Yamaha YZ450F 2017', 'Azul', 'Cadena',
    'DOHC', 4, 'YAM-YZ4-1300A-01', 'Motocross', 449)
    motos.append(x)

def cargar_datos_camiones():
    x = Camion.Camion('Scania R730', 'Rojo', 'Scania GRSO905R',
    'Scania DC16 500 16Litre 90° V8', 6, 'SCA-R730-01', 2, '19 toneladas')
    camiones.append(x)
    x = Camion.Camion('Scania J302', 'Negro', 'Scania GRSO905Z',
    'Scania DC16 500 16Litre 90° V8', 6, 'SCA-J302-01', 2, '21 toneladas')
    camiones.append(x)
    x = Camion.Camion('Scania B165', 'Blanco', 'Scania GRSO905J',
    'Scania DC16 500 16Litre 90° V8', 6, 'SCA-B165-01', 2, '17 toneladas')
    camiones.append(x)

def venta_auto(modelo):
    found = False
    for item in autos:
        if modelo.lower() in item.modelo.lower() and item.existencia > 0:
            item.decrementa_existencia()
            autos_vendidos.append(item)
            found = True
            print("Auto comprado: \n{}".format(item.get_info_automovil()))
            print("Existencias restantes: {}\n".format(item.get_existencia()))
            break
        if item.existencia < 1:
            print("\nExistencias agotadas!\n")
    if found == False:
        print("Lo sentimos, el modelo que busca no está en el catálogo.\n")

def venta_moto(modelo):
    found = False
    for item in motos:
        if modelo.lower() in item.modelo.lower() and item.existencia > 0:
            item.decrementa_existencia()
            motos_vendidas.append(item)
            found = True
            print("Motocicleta comprada: \n{}".format(item.get_info_motocicleta()))
            print("Existencias restantes: {}\n".format(item.get_existencia()))
            break
        if item.existencia < 1:
            print("\nExistencias agotadas!\n")
    if found == False:
        print("Lo sentimos, el modelo que busca no está en el catálogo.\n")

def venta_camion(modelo):
    found = False
    for item in camiones:
        if modelo.lower() in item.modelo.lower() and item.existencia > 0:
            item.decrementa_existencia()
            camiones_vendidos.append(item)
            found = True
            print("Camión comprado: \n{}".format(item.get_info_camion()))
            print("Existencias restantes: {}\n".format(item.get_existencia()))
            break
        if item.existencia < 1:
            print("\nExistencias agotadas!\n")
    if found == False:
        print("Lo sentimos, el modelo que busca no está en el catálogo.\n")


def main():
    ag = Agencia.Agencia('Rivero Motors', 'Chevrolet',
    'Miguel Alemán 5400 Col. Torres de Lindavista', 'SHDFS238RY28')
    cargar_datos_autos()
    cargar_datos_motos()
    cargar_datos_camiones()

    print("\n[[Sistema de agencias {} para la marca {}]]\n".format(ag.get_nombre_agencia(),
    ag.get_concesionaria()))
    while True:
        print("Especifique el tipo de usuario.")
        user = input("\t1. Cliente.\n\t2. Vendedor.\n\t3. Salir del programa.\n\t")
        if user == '3':
            break

        while user == '1':
            print("¿Qué desea hacer?")
            action = input("\t1. Ver catálogo de vehículos.\n\t2. Comprar vehículo.\n\t3. Registrarse como cliente.\n\t4. Salir.\n\t")

            if action == '1':
                print("¿Qué tipo de vehículos desea ver?")
                opt = input("\t1. Automóvil.\n\t2. Motocicleta.\n\t3. Camión.\n\t")
                if opt == '1':
                    print("\n[[[Catálogo {} 2017]]]\n".format(ag.get_concesionaria()))
                    print('-------------------------------------------')
                    for item in autos:
                        print(item.get_info_automovil())
                        print("Existencias: {}".format(item.get_existencia()))
                        print('-------------------------------------------')
                elif opt == '2':
                    print("\n[[[Catálogo Motos 2017]]]\n")
                    print('-------------------------------------------')
                    for item in motos:
                        print(item.get_info_motocicleta())
                        print("Existencias: {}".format(item.get_existencia()))
                        print('-------------------------------------------')
                elif opt == '3':
                    print("\n[[[Catálogo Camiones 2017]]]\n")
                    print('-------------------------------------------')
                    for item in camiones:
                        print(item.get_info_camion())
                        print("Existencias: {}".format(item.get_existencia()))
                        print('-------------------------------------------')
                else:
                    print("Catálogo inválido.")

            elif action == '2':
                print("¿Qué tipo de vehículo desea comprar?")
                opt = input("\t1. Automóvil.\n\t2. Motocicleta.\n\t3. Camión.\n\t")
                if opt == '1':
                    modelo = input("Teclee el modelo del automóvil que desea comprar.\n\t")
                    venta_auto(modelo)
                elif opt == '2':
                    modelo = input("Teclee el modelo de la motocicleta que desea comprar.\n\t")
                    venta_moto(modelo)
                elif opt == '3':
                    modelo = input("Teclee el modelo del camión que desea comprar.\n\t")
                    venta_camion(modelo)
                else:
                    print("Tipo de vehículo inválido.")

            else:
                break

    print("Fin del programa.")


if __name__ == '__main__':
    main()
