# ARCHIVO DONDE SE HACEN TODAS LAS OPERACIONES Y SE CREA UN MENÚ

# Se importan las clases a usar
from agencia import Agencia
from vendedor import Vendedor
from cliente import Cliente
from automovil import Automovil
from camion import Camion
from motocicleta import Motocicleta

# Se declara la agencia donde se realizan las compra/ventas
agencia = Agencia("COMPRA Y VENTA DE VEHICULOS CHIDOS 'POKIMON :D'","Enrique Segoviano #8, Colonia Zaka Mo-Koh")

# Los datos de la agencia se guardan en una variable
datosAgencia = "\n{0}\nVisitanos en: {1}\n".format(agencia.getNombre(), agencia.getDireccion())

# Declaracion de cinco vendedores (W.E.T)
Vend1 = Vendedor("Gokú", "Kakaroto", "Chavez", "30", "Monte Paozu #1", "4658-46873", "1")
Vend2 = Vendedor("Nikola", "Tesla", "Edison", "39", "Smiljan #1006", "3491-6581", "2")
Vend3 = Vendedor("José Doroteo", "Arango", "Arámbula", "45", "Division del Norte #1913", "3291-8781", "3")
Vend4 = Vendedor("Benito Amilcare", "Andrea", "Mussolini", "61", "Predappio #29", "5491-3881", "4")
Vend5 = Vendedor("Napoleone", "di", "Buonaparte", "51", "Ajaccio #15", "1281-9671", "5")

# Declaracion de cinco clientes (W.E.T)
Cl1 = Cliente("Juanito", "Lopez", "Lopez", "35", "Bonita #23", "5159-4864")
Cl2 = Cliente("Lalito", "Flores", "Peña", "29", "Privada pública #40", "9786-8451")
Cl3 = Cliente("Rubencito", "Martinez", "Salinas", "40", "Carmen Salinas S/N", "2135-4886")
Cl4 = Cliente("Germancito", "Hernandez", "Gil", "27", "Florencia #651", "6584-6685")
Cl5 = Cliente("Ramoncito", "Garza", "Perez", "25", "Sin Datos", "6548-9447")

# Declaracion de cinco Automoviles (W.E.T)
Aut1 = Automovil("Ford", "Mustang", "Rojo", "Automatico", "6 cilindros", "494,000", "Motor V6", "5", "2 puertas", "Equipado: No", "14km/L")
Aut2 = Automovil("KIA", "Optima", "Negro", "Automatico", "4 cilindros", "389,400", "2.4L GDI ", "5", "4 puertas", "Equipado: Si", "18.36km/L")
Aut3 = Automovil("Honda", "Accord", "Rojo", "Manual", "4 cilindros", "393,900", "2.4L EXL V6", "5", "4 puertas", "Equipado: Si", "18.5km/L")
Aut4 = Automovil("Chevrolet", "Camaro", "Amarillo", "Manual", "6 cilindros", "473,400", " 2.0L Turbo", "5", "2 puertas", "Equipado: No", "13.1km/L")
Aut5 = Automovil("Dodge", "Charger", "Gris", "Automatico", "8 cilindros", "711,900", "Hemi V8 5.7L", "5", "4 puertas", "Equipado: Si", "13km/L")

# Declaracion de cinco Camiones (W.E.T)
Cam1 = Camion("Ford", "Truck T-1", "Negro", "Manual", "cilindros", "", "motor", "5", "ejes", "potencia")
Cam2 = Camion("Ford", "Truck T-2", "Azul", "Manual", "cilindros", "precio", "motor", "5", "ejes", "potencia")
Cam3 = Camion("Ford", "Truck T-3", "Blanco", "Manual", "cilindros", "precio", "motor", "5", "ejes", "potencia")
Cam4 = Camion("Ford", "Truck T-4", "Rojo", "Manual", "cilindros", "precio", "motor", "5", "ejes", "potencia")
Cam5 = Camion("Ford", "Truck T-5", "Gris", "Manual", "cilindros", "precio", "motor", "5", "ejes", "potencia")

# Declaracion de cinco Motocicletas (W.E.T)
Moto1 = Motocicleta("Honda", "Zoomer X", "Azul/Naranja", "VMATIC", "2 cilindros", "43,990", "SOHC 2V", "5", "Motoneta", "110cc")
Moto2 = Motocicleta("Honda", "CRF 230 F", "Rojo", "Tipo Retorno", "4 cilindros", "77,990", "Motor OHC", "5", "Off Road", "223cc")
Moto3 = Motocicleta("Honda", "CB190R", "Rojo", "Tipo Retorno", "4 cilindros", "50,990", "Motor OHC", "5", "Deportiva", "184.4cc")
Moto4 = Motocicleta("Harley-Davidson", "Street Road", "Negro", "N/A", "6 cilindros", "181,500", "High Output Revolution X", "5", "Deportiva", "750cc")
Moto5 = Motocicleta("Harley-Davidson", "Wide Glide", "Negro", "N/A", "6 cilindros", "290,900", "Twin Cam 103", "5", "Deportiva", "1,690 cc")

# En listaVenta se guardan los datos de la venta realizada
listaVenta = []
# En listaCompra se guardan los datos de la compra realizada
listaCompra = []

# Se inicia el menú con la condicion que opcion sea diferente a 0
opcion = 10
while (opcion != 0):
    print("\n"*25 + datosAgencia)
    print("BIENVENIDO A NUESTRA AGENCIA")
    print("¿Qué operación deseas realizar?")
    print("1: Ver vehiculos.")
    print("2: Existencia de Vehiculos.")
    print("3: Vender vehiculo.")
    print("4: Comprar vehiculo.")
    print("5: Ver Clientes.")
    print("6: Ver Vendedores.")
    print("7: Reportes.")
    print("0: Salir.")

    cond = input("")
    if cond == "":
        print ("Favor de seleccionar una opcion")
        input("Pulse Enter para continuar")
        opcion = 10
    else:
        opcion = int(cond)

    # Opcion 1 crea un submenú para saber que tipo de vehiculo quieres ver
    if opcion == 1 :
        print("\n"*25 + "¿Qué deseas ver?")
        print("1: Automoviles.")
        print("2: Camiones.")
        print("3: Motocicletas.")

        cond = input("")
        if cond == "":
            print ("Favor de seleccionar una opcion")
            input("Pulse Enter para continuar")
            op = 10
        else:
            op = int(cond)

        # En caso 1 se imprimen los datos de los todos los
        # Automoviles usando el metodo informeAutomovil
        if op == 1:
            print("\n"*25)
            print(Aut1.informeAutomovil() + "\n" + "="*80)
            print(Aut2.informeAutomovil() + "\n" + "="*80)
            print(Aut3.informeAutomovil() + "\n" + "="*80)
            print(Aut4.informeAutomovil() + "\n" + "="*80)
            print(Aut5.informeAutomovil() + "\n" + "="*80)
            input("Pulse Enter para continuar")

        # En caso 2 se imprimen los datos de los todos los
        # Camiones usando el metodo informeCamion
        elif op == 2:
            print("\n"*25)
            print(Cam1.informeCamion() + "\n" + "="*80)
            print(Cam2.informeCamion() + "\n" + "="*80)
            print(Cam3.informeCamion() + "\n" + "="*80)
            print(Cam4.informeCamion() + "\n" + "="*80)
            print(Cam5.informeCamion() + "\n" + "="*80)
            input("Pulse Enter para continuar")

        # En caso 3 se imprimen los datos de los todas las
        # Motocicletas usando el metodo informeMotocicleta
        elif op == 3:
            print("\n"*25)
            print(Moto1.informeMotocicleta() + "\n" + "="*80)
            print(Moto2.informeMotocicleta() + "\n" + "="*80)
            print(Moto3.informeMotocicleta() + "\n" + "="*80)
            print(Moto4.informeMotocicleta() + "\n" + "="*80)
            print(Moto5.informeMotocicleta() + "\n" + "="*80)
            input("Pulse Enter para continuar")

    # Opcion 2 crea un submenú para saber que tipo de vehiculo quieres ver
    elif opcion == 2:
        print("\n"*25 + "¿Qué deseas ver?")
        print("1: Automoviles.")
        print("2: Camiones.")
        print("3: Motocicletas.")

        cond = input("")
        if cond == "":
            print ("Favor de seleccionar una opcion")
            input("Pulse Enter para continuar")
            op = 10
        else:
            op = int(cond)

        # En caso 1 se imprime la existencia de cada automovil
        # usando el metodo getExistencia
        if op == 1:
            print("\n"*25 + "Automoviles:\n")
            print(Aut1.getExistencia())
            print(Aut2.getExistencia())
            print(Aut3.getExistencia())
            print(Aut4.getExistencia())
            print(Aut5.getExistencia())
            input("\nPulse Enter para continuar")

        # En caso 2 se imprime la existencia de cada camion
        # usando el metodo getExistencia
        elif op == 2:
            print("\n"*25 + "Camiones:\n")
            print(Cam1.getExistencia())
            print(Cam2.getExistencia())
            print(Cam3.getExistencia())
            print(Cam4.getExistencia())
            print(Cam5.getExistencia())
            input("\nPulse Enter para continuar")

        # En caso 3 se imprime la existencia de cada motocicleta
        # usando el metodo getExistencia
        elif op == 3:
            print("\n"*25 + "Motocicletas:\n")
            print(Moto1.getExistencia())
            print(Moto2.getExistencia())
            print(Moto3.getExistencia())
            print(Moto4.getExistencia())
            print(Moto5.getExistencia())
            input("\nPulse Enter para continuar")

    # Opcion 3 crea un submenú para saber que tipo de vehiculo quieres vender
    elif opcion == 3:
        print("\n"*25 + "¿Qué se venderá?")
        print("1: Automovil.")
        print("2: Camion.")
        print("3: Motocicleta.")

        cond = input("")
        if cond == "":
            print ("Favor de seleccionar una opcion")
            input("Pulse Enter para continuar")
            op = 10
        else:
            op = int(cond)

        # Un submenu para cada caso
        if op == 1:
            print("\n"*25 + "Automovil a vender: ")
            print("1: {0} {1}".format(Aut1.getMarca(), Aut1.getModelo()))
            print("2: {0} {1}".format(Aut2.getMarca(), Aut2.getModelo()))
            print("3: {0} {1}".format(Aut3.getMarca(), Aut3.getModelo()))
            print("4: {0} {1}".format(Aut4.getMarca(), Aut4.getModelo()))
            print("5: {0} {1}".format(Aut5.getMarca(), Aut5.getModelo()))

            cond = input("")
            if cond == "":
                print ("Favor de seleccionar una opcion")
                input("Pulse Enter para continuar")
                op2 = 10
            else:
                op2 = int(cond)

            if op2 == 1:
                if int(Aut1.getNumExistencia()) == 0:
                    print ("No hay {0} {1} disponibles por el momento.SRRY".format(Aut1.getMarca(), Aut1.getModelo()))
                    input("Pulse Enter para continuar")
                else:
                    venta = agencia.ventaVehiculo((Cl3.getNombre() + " " + Cl3.getApellidoPaterno() + " " + Cl3.getApellidoMaterno()),
                            (Aut1.getMarca() + " " + Aut1.getModelo()),
                            (Vend1.getNombre() + " " + Vend1.getApellidoPaterno() + " " + Vend1.getApellidoMaterno()))
                    listaVenta.append(venta)
                    menos = int(Aut1.existencia) - 1
                    Aut1.decrementaExist(menos)
            elif op2 == 2:
                if int(Aut2.getNumExistencia()) == 0:
                    print ("No hay {0} {1} disponibles por el momento.SRRY".format(Aut2.getMarca(), Aut2.getModelo()))
                    input("Pulse Enter para continuar")
                else:
                    venta = agencia.ventaVehiculo((Cl5.getNombre() + " " + Cl5.getApellidoPaterno() + " " + Cl5.getApellidoMaterno()),
                            (Aut2.getMarca() + " " + Aut2.getModelo()),
                            (Vend2.getNombre() + " " + Vend2.getApellidoPaterno() + " " + Vend2.getApellidoMaterno()))
                    listaVenta.append(venta)
                    menos = int(Aut2.existencia) - 1
                    Aut2.decrementaExist(menos)
            elif op2 == 3:
                if int(Aut3.getNumExistencia()) == 0:
                    print ("No hay {0} {1} disponibles por el momento.SRRY".format(Aut3.getMarca(), Aut3.getModelo()))
                    input("Pulse Enter para continuar")
                else:
                    venta = agencia.ventaVehiculo((Cl4.getNombre() + " " + Cl4.getApellidoPaterno() + " " + Cl4.getApellidoMaterno()),
                            (Aut3.getMarca() + " " + Aut3.getModelo()),
                            (Vend3.getNombre() + " " + Vend3.getApellidoPaterno() + " " + Vend3.getApellidoMaterno()))
                    listaVenta.append(venta)
                    menos = int(Aut3.existencia) - 1
                    Aut3.decrementaExist(menos)
            elif op2 == 4:
                if int(Aut4.getNumExistencia()) == 0:
                    print ("No hay {0} {1} disponibles por el momento.SRRY".format(Aut4.getMarca(), Aut4.getModelo()))
                    input("Pulse Enter para continuar")
                else:
                    venta = agencia.ventaVehiculo((Cl2.getNombre() + " " + Cl2.getApellidoPaterno() + " " + Cl2.getApellidoMaterno()),
                            (Aut4.getMarca() + " " + Aut4.getModelo()),
                            (Vend4.getNombre() + " " + Vend4.getApellidoPaterno() + " " + Vend4.getApellidoMaterno()))
                    listaVenta.append(venta)
                    menos = int(Aut4.existencia) - 1
                    Aut4.decrementaExist(menos)
            elif op2 == 5:
                if int(Aut5.getNumExistencia()) == 0:
                    print ("No hay {0} {1} disponibles por el momento.SRRY".format(Aut5.getMarca(), Aut5.getModelo()))
                    input("Pulse Enter para continuar")
                else:
                    venta = agencia.ventaVehiculo((Cl3.getNombre() + " " + Cl3.getApellidoPaterno() + " " + Cl3.getApellidoMaterno()),
                            (Aut5.getMarca() + " " + Aut5.getModelo()),
                            (Vend5.getNombre() + " " + Vend5.getApellidoPaterno() + " " + Vend5.getApellidoMaterno()))
                    listaVenta.append(venta)
                    menos = int(Aut5.existencia) - 1
                    Aut5.decrementaExist(menos)

        elif op == 2:
            print("\n"*25 + "¿Qué camion deseas comprar?")
            print("1: {0} {1}".format(Cam1.getMarca(), Cam1.getModelo()))
            print("2: {0} {1}".format(Cam2.getMarca(), Cam2.getModelo()))
            print("3: {0} {1}".format(Cam3.getMarca(), Cam3.getModelo()))
            print("4: {0} {1}".format(Cam4.getMarca(), Cam4.getModelo()))
            print("5: {0} {1}".format(Cam5.getMarca(), Cam5.getModelo()))

            cond = input("")
            if cond == "":
                print ("Favor de seleccionar una opcion")
                input("Pulse Enter para continuar")
                op2 = 10
            else:
                op2 = int(cond)

            if op2 == 1:
                if int(Cam1.getNumExistencia()) == 0:
                    print ("No hay {0} {1} disponibles por el momento.SRRY".format(Cam1.getMarca(), Cam1.getModelo()))
                    input("Pulse Enter para continuar")
                else:
                    venta = agencia.ventaVehiculo((Cl4.getNombre() + " " + Cl4.getApellidoPaterno() + " " + Cl4.getApellidoMaterno()),
                            (Cam1.getMarca() + " " + Cam1.getModelo()),
                            (Vend5.getNombre() + " " + Vend5.getApellidoPaterno() + " " + Vend5.getApellidoMaterno()))
                    listaVenta.append(venta)
                    menos = int(Cam1.existencia) - 1
                    Cam1.decrementaExist(menos)
            elif op2 == 2:
                if int(Cam2.getNumExistencia()) == 0:
                    print ("No hay {0} {1} disponibles por el momento.SRRY".format(Cam2.getMarca(), Cam2.getModelo()))
                    input("Pulse Enter para continuar")
                else:
                    venta = agencia.ventaVehiculo((Cl2.getNombre() + " " + Cl2.getApellidoPaterno() + " " + Cl2.getApellidoMaterno()),
                            (Cam2.getMarca() + " " + Cam2.getModelo()),
                            (Vend4.getNombre() + " " + Vend4.getApellidoPaterno() + " " + Vend4.getApellidoMaterno()))
                    listaVenta.append(venta)
                    menos = int(Cam2.existencia) - 1
            elif op2 == 3:
                if int(Cam3.getNumExistencia()) == 0:
                    print ("No hay {0} {1} disponibles por el momento.SRRY".format(Cam3.getMarca(), Cam3.getModelo()))
                    input("Pulse Enter para continuar")
                else:
                    venta = agencia.ventaVehiculo((Cl5.getNombre() + " " + Cl5.getApellidoPaterno() + " " + Cl5.getApellidoMaterno()),
                            (Cam3.getMarca() + " " + Cam3.getModelo()),
                            (Vend3.getNombre() + " " + Vend3.getApellidoPaterno() + " " + Vend3.getApellidoMaterno()))
                    listaVenta.append(venta)
                    menos = int(Cam3.existencia) - 1
                    Cam3.decrementaExist(menos)
            elif op2 == 4:
                if int(Cam4.getNumExistencia()) == 0:
                    print ("No hay {0} {1} disponibles por el momento.SRRY".format(Cam4.getMarca(), Cam4.getModelo()))
                    input("Pulse Enter para continuar")
                else:
                    venta = agencia.ventaVehiculo((Cl3.getNombre() + " " + Cl3.getApellidoPaterno() + " " + Cl3.getApellidoMaterno()),
                            (Cam4.getMarca() + " " + Cam4.getModelo()),
                            (Vend2.getNombre() + " " + Vend2.getApellidoPaterno() + " " + Vend2.getApellidoMaterno()))
                    listaVenta.append(venta)
                    menos = int(Cam4.existencia) - 1
                    Cam4.decrementaExist(menos)
            elif op2 == 5:
                if int(Cam5.getNumExistencia()) == 0:
                    print ("No hay {0} {1} disponibles por el momento.SRRY".format(Cam5.getMarca(), Cam5.getModelo()))
                    input("Pulse Enter para continuar")
                else:
                    venta = agencia.ventaVehiculo((Cl1.getNombre() + " " + Cl1.getApellidoPaterno() + " " + Cl1.getApellidoMaterno()),
                            (Cam5.getMarca() + " " + Cam5.getModelo()),
                            (Vend1.getNombre() + " " + Vend1.getApellidoPaterno() + " " + Vend1.getApellidoMaterno()))
                    listaVenta.append(venta)
                    menos = int(Cam5.existencia) - 1
                    Cam5.decrementaExist(menos)

        elif op == 3:
            print("\n"*25 + "¿Qué motocicleta deseas comprar?")
            print("1: {0} {1}".format(Moto1.getMarca(), Moto1.getModelo()))
            print("2: {0} {1}".format(Moto2.getMarca(), Moto2.getModelo()))
            print("3: {0} {1}".format(Moto3.getMarca(), Moto3.getModelo()))
            print("4: {0} {1}".format(Moto4.getMarca(), Moto4.getModelo()))
            print("5: {0} {1}".format(Moto5.getMarca(), Moto5.getModelo()))

            cond = input("")
            if cond == "":
                print ("Favor de seleccionar una opcion")
                input("Pulse Enter para continuar")
                op2 = 10
            else:
                op2 = int(cond)

            if op2 == 1:
                if int(Moto1.getNumExistencia()) == 0:
                    print ("No hay {0} {1} disponibles por el momento.SRRY".format(Moto1.getMarca(), Moto1.getModelo()))
                    input("Pulse Enter para continuar")
                else:
                    venta = agencia.ventaVehiculo((Cl2.getNombre() + " " + Cl2.getApellidoPaterno() + " " + Cl2.getApellidoMaterno()),
                            (Moto1.getMarca() + " " + Moto1.getModelo()),
                            (Vend3.getNombre() + " " + Vend3.getApellidoPaterno() + " " + Vend3.getApellidoMaterno()))
                    listaVenta.append(venta)
                    menos = int(Moto1.existencia) - 1
                    Moto1.decrementaExist(menos)
            elif op2 == 2:
                if int(Moto2.getNumExistencia()) == 0:
                    print ("No hay {0} {1} disponibles por el momento.SRRY".format(Moto2.getMarca(), Moto2.getModelo()))
                    input("Pulse Enter para continuar")
                else:
                    venta = agencia.ventaVehiculo((Cl4.getNombre() + " " + Cl4.getApellidoPaterno() + " " + Cl4.getApellidoMaterno()),
                            (Moto2.getMarca() + " " + Moto2.getModelo()),
                            (Vend4.getNombre() + " " + Vend4.getApellidoPaterno() + " " + Vend4.getApellidoMaterno()))
                    listaVenta.append(venta)
                    menos = int(Moto2.existencia) - 1
                    Moto2.decrementaExist(menos)
            elif op2 == 3:
                if int(Moto3.getNumExistencia()) == 0:
                    print ("No hay {0} {1} disponibles por el momento.SRRY".format(Moto3.getMarca(), Moto3.getModelo()))
                    input("Pulse Enter para continuar")
                else:
                    venta = agencia.ventaVehiculo((Cl3.getNombre() + " " + Cl3.getApellidoPaterno() + " " + Cl3.getApellidoMaterno()),
                            (Moto3.getMarca() + " " + Moto3.getModelo()),
                            (Vend1.getNombre() + " " + Vend1.getApellidoPaterno() + " " + Vend1.getApellidoMaterno()))
                    listaVenta.append(venta)
                    menos = int(Moto3.existencia) - 1
                    Moto3.decrementaExist(menos)
            elif op2 == 4:
                if int(Moto4.getNumExistencia()) == 0:
                    print ("No hay {0} {1} disponibles por el momento.SRRY".format(Moto4.getMarca(), Moto4.getModelo()))
                    input("Pulse Enter para continuar")
                else:
                    venta = agencia.ventaVehiculo((Cl5.getNombre() + " " + Cl5.getApellidoPaterno() + " " + Cl5.getApellidoMaterno()),
                            (Moto4.getMarca() + " " + Moto4.getModelo()),
                            (Vend5.getNombre() + " " + Vend5.getApellidoPaterno() + " " + Vend5.getApellidoMaterno()))
                    listaVenta.append(venta)
                    menos = int(Moto4.existencia) - 1
                    Moto4.decrementaExist(menos)
            elif op2 == 5:
                if int(Moto5.getNumExistencia()) == 0:
                    print ("No hay {0} {1} disponibles por el momento.SRRY".format(Moto5.getMarca(), Moto5.getModelo()))
                    input("Pulse Enter para continuar")
                else:
                    venta = agencia.ventaVehiculo((Cl2.getNombre() + " " + Cl2.getApellidoPaterno() + " " + Cl2.getApellidoMaterno()),
                            (Moto5.getMarca() + " " + Moto5.getModelo()),
                            (Vend2.getNombre() + " " + Vend2.getApellidoPaterno() + " " + Vend2.getApellidoMaterno()))
                    listaVenta.append(venta)
                    menos = int(Moto5.existencia) - 1
                    Moto5.decrementaExist(menos)

    # Opcion 4 crea un submenú para saber que tipo de vehiculo quieres comprar
    elif opcion == 4:
        print("\n"*25 + "¿Qué deseas comprar?")
        print("1: Automovil.")
        print("2: Camion.")
        print("3: Motocicleta.")

        cond = input("")
        if cond == "":
            print ("Favor de seleccionar una opcion")
            input("Pulse Enter para continuar")
            op = 10
        else:
            op = int(cond)

        # Un submenu para cada caso
        if op == 1:
            print("\n"*25 + "¿Qué auto deseas comprar?")
            print("1: {0} {1}".format(Aut1.getMarca(), Aut1.getModelo()))
            print("2: {0} {1}".format(Aut2.getMarca(), Aut2.getModelo()))
            print("3: {0} {1}".format(Aut3.getMarca(), Aut3.getModelo()))
            print("4: {0} {1}".format(Aut4.getMarca(), Aut4.getModelo()))
            print("5: {0} {1}".format(Aut5.getMarca(), Aut5.getModelo()))

            op2 = int(input(""))

            if op2 == 1:
                n = int(input("Cantidad a comprar: "))
                compra = agencia.compraVehiculo(n, (Aut1.getMarca() + " " + Aut1.getModelo()))
                listaCompra.append(compra)
                nvo =  int(Aut1.existencia) + n
                Aut1.incrementaExist(str(nvo))
            elif op2 == 2:
                n = int(input("Cantidad a comprar: "))
                compra = agencia.compraVehiculo(n, (Aut2.getMarca() + " " + Aut2.getModelo()))
                listaCompra.append(compra)
                nvo =  int(Aut2.existencia) + n
                Aut2.incrementaExist(str(nvo))
            elif op2 == 3:
                n = int(input("Cantidad a comprar: "))
                compra = agencia.compraVehiculo(n, (Aut3.getMarca() + " " + Aut3.getModelo()))
                listaCompra.append(compra)
                nvo =  int(Aut3.existencia) + n
                Aut3.incrementaExist(str(nvo))
            elif op2 == 4:
                n = int(input("Cantidad a comprar: "))
                compra = agencia.compraVehiculo(n, (Aut4.getMarca() + " " + Aut4.getModelo()))
                listaCompra.append(compra)
                nvo =  int(Aut4.existencia) + n
                Aut4.incrementaExist(str(nvo))
            elif op2 == 5:
                n = int(input("Cantidad a comprar: "))
                compra = agencia.compraVehiculo(n, (Aut5.getMarca() + " " + Aut5.getModelo()))
                listaCompra.append(compra)
                nvo =  int(Aut5.existencia) + n
                Aut5.incrementaExist(str(nvo))

        elif op == 2:
            print("\n"*25 + "¿Qué camion deseas comprar?")
            print("1: {0} {1}".format(Cam1.getMarca(), Cam1.getModelo()))
            print("2: {0} {1}".format(Cam2.getMarca(), Cam2.getModelo()))
            print("3: {0} {1}".format(Cam3.getMarca(), Cam3.getModelo()))
            print("4: {0} {1}".format(Cam4.getMarca(), Cam4.getModelo()))
            print("5: {0} {1}".format(Cam5.getMarca(), Cam5.getModelo()))

            op2 = int(input(""))

            if op2 == 1:
                n = int(input("Cantidad a comprar: "))
                compra = agencia.compraVehiculo(n, (Cam1.getMarca() + " " + Cam1.getModelo()))
                listaCompra.append(compra)
                nvo =  int(Cam1.existencia) + n
                Cam1.incrementaExist(str(nvo))
            elif op2 == 2:
                n = int(input("Cantidad a comprar: "))
                compra = agencia.compraVehiculo(n, (Cam2.getMarca() + " " + Cam2.getModelo()))
                listaCompra.append(compra)
                nvo =  int(Cam2.existencia) + n
                Cam2.incrementaExist(str(nvo))
            elif op2 == 3:
                n = int(input("Cantidad a comprar: "))
                compra = agencia.compraVehiculo(n, (Cam3.getMarca() + " " + Cam3.getModelo()))
                listaCompra.append(compra)
                nvo =  int(Cam3.existencia) + n
                Cam3.incrementaExist(str(nvo))
            elif op2 == 4:
                n = int(input("Cantidad a comprar: "))
                compra = agencia.compraVehiculo(n, (Cam4.getMarca() + " " + Cam4.getModelo()))
                listaCompra.append(compra)
                nvo =  int(Cam4.existencia) + n
                Cam4.incrementaExist(str(nvo))
            elif op2 == 5:
                n = int(input("Cantidad a comprar: "))
                compra = agencia.compraVehiculo(n, (Cam5.getMarca() + " " + Cam5.getModelo()))
                listaCompra.append(compra)
                nvo =  int(Cam5.existencia) + n
                Cam5.incrementaExist(str(nvo))

        elif op == 3:
            print("\n"*25 + "¿Qué motocicleta deseas comprar?")
            print("1: {0} {1}".format(Moto1.getMarca(), Moto1.getModelo()))
            print("2: {0} {1}".format(Moto2.getMarca(), Moto2.getModelo()))
            print("3: {0} {1}".format(Moto3.getMarca(), Moto3.getModelo()))
            print("4: {0} {1}".format(Moto4.getMarca(), Moto4.getModelo()))
            print("5: {0} {1}".format(Moto5.getMarca(), Moto5.getModelo()))

            op2 = int(input(""))

            if op2 == 1:
                n = int(input("Cantidad a comprar: "))
                compra = agencia.compraVehiculo(n, (Moto1.getMarca() + " " + Moto1.getModelo()))
                listaCompra.append(compra)
                nvo =  int(Moto1.existencia) + n
                Moto1.incrementaExist(str(nvo))
            elif op2 == 2:
                n = int(input("Cantidad a comprar: "))
                compra = agencia.compraVehiculo(n, (Moto2.getMarca() + " " + Moto2.getModelo()))
                listaCompra.append(compra)
                nvo =  int(Moto2.existencia) + n
                Moto2.incrementaExist(str(nvo))
            elif op2 == 3:
                n = int(input("Cantidad a comprar: "))
                compra = agencia.compraVehiculo(n, (Moto3.getMarca() + " " + Moto3.getModelo()))
                listaCompra.append(compra)
                nvo =  int(Moto3.existencia) + n
                Moto3.incrementaExist(str(nvo))
            elif op2 == 4:
                n = int(input("Cantidad a comprar: "))
                compra = agencia.compraVehiculo(n, (Moto4.getMarca() + " " + Moto4.getModelo()))
                listaCompra.append(compra)
                nvo =  int(Moto4.existencia) + n
                Moto4.incrementaExist(str(nvo))
            elif op2 == 5:
                n = int(input("Cantidad a comprar: "))
                compra = agencia.compraVehiculo(n, (Moto5.getMarca() + " " + Moto5.getModelo()))
                listaCompra.append(compra)
                nvo =  int(Moto5.existencia) + n
                Moto5.incrementaExist(str(nvo))

    # Opcion 5 muestra los datos de los clientes
    # usando el metodo informeCliente
    elif opcion == 5:
        print("\n"*25)
        print(Cl1.informeCliente() + "\n" + "="*80)
        print(Cl2.informeCliente() + "\n" + "="*80)
        print(Cl3.informeCliente() + "\n" + "="*80)
        print(Cl4.informeCliente() + "\n" + "="*80)
        print(Cl5.informeCliente() + "\n" + "="*80)
        input("Pulse Enter para continuar")

    # Opcion 6 muestra los datos de los vendedores
    # usando el metodo informeVendedor
    elif opcion == 6:
        print("\n"*25)
        print(Vend1.informeVendedor() + "\n" + "="*80)
        print(Vend2.informeVendedor() + "\n" + "="*80)
        print(Vend3.informeVendedor() + "\n" + "="*80)
        print(Vend4.informeVendedor() + "\n" + "="*80)
        print(Vend5.informeVendedor() + "\n" + "="*80)
        input("Pulse Enter para continuar")

    # Opcion 7 muestra un submenu para saber que tipo de reporte deseas ver
    elif opcion == 7:
        print("\n"*25 + "Reporte de: ")
        print("1: Compras.")
        print("2: Ventas.")

        cond = input("")
        if cond == "":
            print ("Favor de seleccionar una opcion")
            input("Pulse Enter para continuar")
            op = 10
        else:
            op = int(cond)

        # Opcion 1 muestra los datos de listaCompra
        if op == 1:
            print("\n"*25)
            for x in range(len(listaCompra)):
                print("Compra {0}:\n{1}".format(x+1,listaCompra[x]))
                print("="*80)
            input("Pulse Enter para continuar")

        # Opcion 2 muestra los datos de listaVenta
        elif op == 2:
            print("\n"*25)
            for x in range(len(listaVenta)):
                print("Venta {0}:\n{1}".format(x+1,listaVenta[x]))
                print("="*80)
            input("Pulse Enter para continuar")
