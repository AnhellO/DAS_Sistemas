# Se importa la clase necesaria.
from PrimerParcial import Electrodomestico


# Listas para guardar los respectivos objetos (aunque solo se use el primer creado XD).
listaLavadora = []
listaTv = []
listaRefrigerador = []


# Ola ke ase reusando el Menú o ke ase.
opcion = 10
while (opcion != 0):
    print("\n"*25+"¿Qué operación deseas realizar?")
    print("1: Crear Lavadora.")
    print("2: Lavar en primer lavadora.")
    print("3: Crear Television.")
    print("4: Cambiar de canal en primer TV.")
    print("5: Crear Refrigerador.")
    print("6: Almacenar comida en primer refrigerador.")
    print("0: Salir.")

    # No sale del programa con un Enter lokote.
    cond = input("")
    if cond == "":
        print ("Favor de seleccionar una opcion")
        input("Pulse Enter para continuar")
        opcion = 10
    else:
        opcion = int(cond)

    if opcion == 1:
        # Pedir datos para los atributos.
        marca =  input("Marca: ")
        modelo = input("Modelo: ")
        tipo = input("Tipo de lavadora: ")
        lugar = input("Lugar de la casa donde estará: ")
        altura = input("Altura: ")
        # numFunciones atributo de Lavadora.
        numFunciones = input("Numero de funciones: ")

        # Usando el metodo factory de Electrodomestico.
        lav = Electrodomestico.factory("Lavadora", marca = marca, modelo = modelo, tipo = tipo, lugar = lugar, altura = altura, numFunciones = numFunciones)
        # Se añade a la lista.
        listaLavadora.append(lav)

    if opcion == 2:
        # Si la lista no está vacia entonces hace la pregunta.
        if len(listaLavadora) != 0:
            listaLavadora[0].lavar(input("¿Qué quieres lavar? "))
            input("Pulse Enter para continuar")
        else:
            # Sin Lavadora no se puede lavar chavo. >:c
            print("Favor de crear una lavadora")
            input("Pulse Enter para continuar")


    if opcion == 3:
        # Pedir datos para los atributos.
        marca =  input("Marca: ")
        modelo = input("Modelo: ")
        tipo = input("Tipo de TV: ")
        lugar = input("Lugar de la casa donde estará: ")
        altura = input("Altura: ")
        # resolucion atributo de Television.
        resolucion = input("Resolucion: ")

        # Usando el metodo factory de Electrodomestico.
        tv = Electrodomestico.factory("Television", marca = marca, modelo = modelo, tipo = tipo, lugar = lugar, altura = altura, resolucion = resolucion)
        # Se añade a la lista.
        listaTv.append(tv)

    if opcion == 4:
        # Si la lista no está vacia entonces hace la pregunta.
        if len(listaTv) != 0:
            listaTv[0].cambiarCanal(input("¿A qué canal cambiarás? "))
            input("Pulse Enter para continuar")
        else:
            # No TV no cambio de canal >:C
            print("Favor de crear una television")
            input("Pulse Enter para continuar")

    if opcion == 5:
        # Pedir datos para los atributos.
        marca =  input("Marca: ")
        modelo = input("Modelo: ")
        tipo = input("Tipo de refrigerador: ")
        lugar = input("Lugar de la casa donde estará: ")
        altura = input("Altura: ")
        # numPuertas atributo de Refrigerador.
        numPuertas = input("Numero de puertas: ")

        # Usando el metodo factory de Electrodomestico.
        refri = Electrodomestico.factory("Refrigerador", marca = marca, modelo = modelo, tipo = tipo, lugar = lugar, altura = altura, numPuertas = numPuertas)
        # Se añade a la lista.
        listaRefrigerador.append(refri)

    if opcion == 6:
        # Si la lista no está vacia entonces hace la pregunta.
        if len(listaRefrigerador) != 0:
            listaRefrigerador[0].almacenarComida(input("¿Qué quieres almacenar? "))
            input("Pulse Enter para continuar")
        else:
            # ¿Refrigerar algo sin un refrigerador? HAHAHA NOOOB >:c
            print("Favor de crear un refrigerador")
            input("Pulse Enter para continuar")
