import Agencia, Automovil, Motocicleta, Camion, Vendedor, Cliente

catalogo_autos = []
catalogo_motos = []
catalogo_camiones = []
cartera_clientes = []
autos_vendidos = []

def cargar_catalogo_autos():
    x = Automovil.Automovil('Chevrolet Aveo 2017', 'Rojo', 'Automático', '2.0L',
    '4', 'CHE-AV-S-01', 5, True, 15, 'Sedán')
    catalogo_autos.append(x.get_info_automovil())
    x = Automovil.Automovil('Chevrolet Cavalier 2017', 'Azul', 'Automático', '2.0L',
    '4', 'CHE-CA-S-01', 5, True, 13, 'Sedán')
    catalogo_autos.append(x.get_info_automovil())
    x = Automovil.Automovil('Chevrolet Spark 2017', 'Plata', 'Manual', '1.8L',
    '4', 'CHE-SP-S-01', 5, False, 17, 'Hatchback')
    catalogo_autos.append(x.get_info_automovil())

def cargar_catalogo_motos():
    x = Motocicleta.Motocicleta('Ducati Monster 1200S 2017', 'Negro', 'Cadena',
    'Testastretta 11° L-Twin', 4, 'DUC-MON-1200S-01', 'Urbana', 1198)
    catalogo_motos.append(x.get_info_motocicleta())
    x = Motocicleta.Motocicleta('Yamaha FJR1300A 2017', 'Rojo', 'Cadena',
    'DOHC', 4, 'YAM-FJR-1300A-01', 'Urbana/Carreras', 998)
    catalogo_motos.append(x.get_info_motocicleta())
    x = Motocicleta.Motocicleta('Yamaha YZ450F 2017', 'Azul', 'Cadena',
    'DOHC', 4, 'YAM-YZ4-1300A-01', 'Motocross', 449)
    catalogo_motos.append(x.get_info_motocicleta())

def cargar_catalogo_camiones():
    x = Camion.Camion('Scania R730', 'Rojo', 'Scania GRSO905R',
    'Scania DC16 500 16Litre 90° V8', 6, 'SCA-R730-01', 2, '19 toneladas')
    catalogo_camiones.append(x.get_info_camion())
    x = Camion.Camion('Scania J302', 'Negro', 'Scania GRSO905Z',
    'Scania DC16 500 16Litre 90° V8', 6, 'SCA-J302-01', 2, '21 toneladas')
    catalogo_camiones.append(x.get_info_camion())
    x = Camion.Camion('Scania B165', 'Blanco', 'Scania GRSO905J',
    'Scania DC16 500 16Litre 90° V8', 6, 'SCA-B165-01', 2, '17 toneladas')
    catalogo_camiones.append(x.get_info_camion())

def vender_auto(modelo):
        # To do.


def main():
    ag = Agencia.Agencia('Rivero Motors', 'Chevrolet',
    'Miguel Alemán 5400 Col. Torres de Lindavista', 'SHDFS238RY28')
    cargar_catalogo_autos()
    cargar_catalogo_motos()
    cargar_catalogo_camiones()

    print("\n[[Sistema de agencias {} para la marca {}]]\n".format(ag.get_nombre_agencia(),
    ag.get_concesionaria()))
    while True:
        print("Especifique el tipo de usuario.")
        user = input("\t1. Cliente.\n\t2. Vendedor.\n\t3. Salir del programa.\n\t")
        if user == '3':
            break

        while user == '1':
            print("¿Qué desea hacer?")
            action = input("\t1. Ver catálogo de vehículos.\n\t2. Registrarse como cliente.\n\t3. Salir.\n\t")

            if action == '1':
                print("¿Qué tipo de vehículos desea ver?")
                opt = input("\t1. Automóvil.\n\t2. Motocicleta.\n\t3. Camión.\n\t")
                if opt == '1':
                    print("\n[[[Catálogo Chevrolet 2017]]]\n")
                    print('-------------------------------------------')
                    for item in catalogo_autos:
                        print(item)
                        print('-------------------------------------------')
                elif opt == '2':
                    print("\n[[[Catálogo Motos 2017]]]\n")
                    print('-------------------------------------------')
                    for item in catalogo_motos:
                        print(item)
                        print('-------------------------------------------')
                elif opt == '3':
                    print("\n[[[Catálogo Camiones 2017]]]\n")
                    print('-------------------------------------------')
                    for item in catalogo_camiones:
                        print(item)
                        print('-------------------------------------------')
                else:
                    print("Catálogo inválido.")

            elif action == '2':
                # To do.

            else:
                break

    print("Fin del programa.")


if __name__ == '__main__':
    main()
