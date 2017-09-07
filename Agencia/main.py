import Agencia, Automovil, Motocicleta, Camion, Vendedor, Cliente

# Clase main (operaciones)


# Listas para trabajar en runtime.

autos = []
motos = []
camiones = []

autos_vendidos = []
motos_vendidas = []
camiones_vendidos = []

cartera_clientes = []
lista_vendedores = []

log = []


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
        if modelo.lower() in item.modelo.lower():
            found = True
            if item.existencia > 0:
                item.decrementa_existencia()
                autos_vendidos.append(item)
                print("\nAuto comprado: \n{}".format(item.get_info_automovil()))
                print("Existencias restantes: {}\n".format(item.get_existencia()))
                break
            else:
                print("Ya no hay {} disponibles.".format(item.get_modelo()))
                break
    if found == False:
        print("Lo sentimos, el modelo que busca no está en el catálogo.\n")

def venta_moto(modelo):
    found = False
    for item in motos:
        if modelo.lower() in item.modelo.lower():
            found = True
            if item.existencia > 0:
                item.decrementa_existencia()
                motos_vendidas.append(item)
                print("Motocicleta comprada: \n{}".format(item.get_info_motocicleta()))
                print("Existencias restantes: {}\n".format(item.get_existencia()))
                break
            else:
                print("Ya no hay {} disponibles.".format(item.get_modelo()))
                break
    if found == False:
        print("Lo sentimos, el modelo que busca no está en el catálogo.\n")

def venta_camion(modelo):
    found = False
    for item in camiones:
        if modelo.lower() in item.modelo.lower():
            found = True
            if item.existencia > 0:
                item.decrementa_existencia()
                camiones_vendidos.append(item)
                print("Camión comprado: \n{}".format(item.get_info_camion()))
                print("Existencias restantes: {}\n".format(item.get_existencia()))
                break
            else:
                print("Ya no hay {} disponibles.".format(item.get_modelo()))
                break
    if found == False:
        print("Lo sentimos, el modelo que busca no está en el catálogo.\n")



def main():
    ag = Agencia.Agencia('Rivero Motors', 'Chevrolet',
    'Miguel Alemán 5400 Col. Torres de Lindavista', 'SHDFS238RY28')
    cargar_datos_autos()
    cargar_datos_motos()
    cargar_datos_camiones()
    vendedor_actual = None

    print("\n[[Sistema de agencias {} para la marca {}]]\n".format(ag.get_nombre_agencia(),
    ag.get_concesionaria()))

    while True:
        print("\nEspecifique el tipo de usuario.")
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

            elif action == '3':
                print("Registre sus datos.")
                temp_cli = Cliente.Cliente('','','','','','','','')
                aux = input("Nombre: ")
                temp_cli.set_nombre(aux.title())
                aux = input("Apellido Paterno: ")
                temp_cli.set_apellido_paterno(aux.title())
                aux = input("Apellido Materno: ")
                temp_cli.set_apellido_materno(aux.title())
                aux = input("Genero (M/F): ")
                temp_cli.set_genero(aux.title())
                aux = input("Edad: ")
                temp_cli.set_edad(aux)
                aux = input("Domicilio: ")
                temp_cli.set_domicilio(aux.title())
                aux = input("Teléfono (###-###-####): ")
                temp_cli.set_telefono(aux)
                aux = input("Email: ")
                temp_cli.set_email(aux)

                cartera_clientes.append(temp_cli)

                print("\nCliente registrado:\n{}\n".format(temp_cli.get_info_cliente()))

            else:
                break

        while user == '2':
            print("¿Qué desea hacer?")
            act_string = "\t1. Registrar vendedor.\n\t2. Vender vehículo.\n\t"
            act_string += "3. Ver cartera de clientes.\n\t4. Ver lista de vendedores.\n\t5. Consultar meta.\n\t6. Salir\n\t"
            action = input(act_string)

            if action == '1':
                print("Registre sus datos.")
                temp_ven = Vendedor.Vendedor('','','','','','','','')
                aux = input("Nombre: ")
                temp_ven.set_nombre(aux.title())
                aux = input("Apellido Paterno: ")
                temp_ven.set_apellido_paterno(aux.title())
                aux = input("Apellido Materno: ")
                temp_ven.set_apellido_materno(aux.title())
                aux = input("Genero (M/F): ")
                temp_ven.set_genero(aux.title())
                aux = input("Edad: ")
                temp_ven.set_edad(aux)
                aux = input("Domicilio: ")
                temp_ven.set_domicilio(aux.title())
                aux = input("Teléfono (###-###-####): ")
                temp_ven.set_telefono(aux)
                aux = input("Años de experiencia: ")
                temp_ven.set_experiencia(aux)

                lista_vendedores.append(temp_ven)
                if vendedor_actual == None:
                    vendedor_actual = temp_ven
                    print("\n{} {} fue asignado como el vendedor actual.".format(vendedor_actual.get_nombre(),
                    vendedor_actual.get_apellido_paterno()))

                print("\nVendedor registrado:\n{}\n".format(temp_ven.get_info_vendedor()))

            elif action == '2':
                if vendedor_actual == None:
                    print("Debe registrarse como vendedor primero.")
                else:
                    print("Hola {}, ¿qué tipo de vehículo venderá hoy?".format(vendedor_actual.get_nombre()))
                    opt = input("\t1. Automóvil.\n\t2. Motocicleta.\n\t3. Camión.\n\t")
                    if opt == '1':
                        modelo = input("Teclee el modelo del automóvil que desea vender.\n\t")
                        venta_auto(modelo)
                        vendedor_actual.incrementa_vehiculos_vendidos()
                    elif opt == '2':
                        modelo = input("Teclee el modelo de la motocicleta que desea vender.\n\t")
                        venta_moto(modelo)
                        vendedor_actual.incrementa_vehiculos_vendidos()
                    elif opt == '3':
                        modelo = input("Teclee el modelo del camión que desea vender.\n\t")
                        venta_camion(modelo)
                        vendedor_actual.incrementa_vehiculos_vendidos()
                    else:
                        print("Tipo de vehículo inválido.")

            elif action == '3':
                print("\n[[[Cartera de clientes]]]\n")
                print('-------------------------------------------')
                for item in cartera_clientes:
                    print(item.get_info_cliente())
                    print('-------------------------------------------')

            elif action == '4':
                print("\n[[[Lista de vendedores]]]\n")
                print('-------------------------------------------')
                for item in lista_vendedores:
                    print(item.get_info_vendedor())
                    print('-------------------------------------------')

            elif action == '5':
                print(vendedor_actual.cumplio_meta())

            else:
                break

    print("Fin del programa.")


if __name__ == '__main__':
    main()
