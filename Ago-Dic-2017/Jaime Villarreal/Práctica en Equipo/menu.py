import crud

opcion = 10
while (opcion != 0):
    print("\n"*25+"¿Qué operación deseas realizar?")
    print("1: Ver Banda.")
    print("2: Ver Discografía.")
    print("3: Ver Miembros.")
    print("4: Eliminar Banda(Discografia y Miembros).")
    print("5: Actualizar nombre de Banda.")
    print("6: Actualizar nombre de Disco.")
    print("7: Actualizar nombre de Miembro.")
    print("0: Salir.")

    cond = input("")
    if cond == "":
        print ("Favor de seleccionar una opcion")
        input("Pulse Enter para continuar.")
        opcion = 10
    else:
        opcion = int(cond)


    if opcion == 1:
        print('\n'*25)
        n = input("¿Qué banda deseas ver?(Dejar vacío para ver todo): ")
        crud.selectFromBand(n)
        input("\nPulse Enter para continuar.")

    elif opcion == 2:
        print('\n'*25)
        n = input("Discografía de la banda(Dejar vacío para ver todo): ")
        crud.selectFromDiscography(n)
        input("\nPulse Enter para continuar.")

    elif opcion == 3:
        print('\n'*25)
        n = input("Miembros de la banda(Dejar vacío para ver todo): ")
        crud.selectFromMember(n)
        input("\nPulse Enter para continuar.")

    elif opcion == 4:
        print('\n'*25)
        n = input("¿Qué banda deseas borrar?: ")
        if n =="":
            print("Escribe una banda PLZ.")
            input("\nPulse Enter para continuar.")
        else:
            crud.deleteFromMember(n)
            crud.deleteFromDiscography(n)
            crud.deleteFromBand(n)
            input("Borrado exitoso :c\nPulse Enter para continuar.")

    elif opcion == 5:
        print('\n'*25)
        Oname = input("¿Qué banda quieres actualizar?: ")
        if Oname == "":
            print("\nNo dejar vacío PLZ.")
            input("\nPulse Enter para continuar.")
        else:
            Nname = input("Nuevo nombre: ")
            if Nname == "":
                print("\nNo dejar vacío PLZ.")
                input("\nPulse Enter para continuar.")
            else:
                crud.updateBandName(Oname,Nname)
                input("Actualizacion exitosa.\nPulse Enter para continuar.")

    elif opcion == 6:
        print('\n'*25)
        Oname = input("¿Qué Disco quieres actualizar?: ")
        if Oname == "":
            print("\nNo dejar vacío PLZ.")
            input("\nPulse Enter para continuar.")
        else:
            Nname = input("Nuevo nombre: ")
            if Nname == "":
                print("\nNo dejar vacío PLZ.")
                input("\nPulse Enter para continuar.")
            else:
                crud.updateDiscographyName(Oname,Nname)
                input("Actualizacion exitosa.\nPulse Enter para continuar.")

    elif opcion == 7:
        print('\n'*25)
        Oname = input("¿Qué Miembro quieres actualizar?: ")
        if Oname == "":
            print("\nNo dejar vacío PLZ.")
            input("\nPulse Enter para continuar.")
        else:
            Nname = input("Nuevo nombre: ")
            if Nname == "":
                print("\nNo dejar vacío PLZ.")
                input("\nPulse Enter para continuar.")
            else:
                crud.updateMemberName(Oname,Nname)
                input("Actualizacion exitosa.\nPulse Enter para continuar.")
