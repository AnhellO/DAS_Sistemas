from Television import Television
from Refrigerador import Refrigerador
from Lavadora import Lavadora

televisiones = []
refrigeradores = []
lavadoras = []

def cargar_televisiones():
    x = Television('Sony', 'Vaio', 'Gris', 30, 60, 40)
    televisiones.append(x)
    x = Television('Toshiba', 'L621U', 'Negra', 35, 65, 35)
    televisiones.append(x)
    x = Television('Panasonic', 'TC-49ES600', 'Gris', 40, 60, 40)
    televisiones.append(x)

def cargar_refrigeradores():
    x = Refrigerador('Frigidaire', 'Pro', 'Gris', 30, 60, 40)
    refrigeradores.append(x)
    x = Refrigerador('Mabe', 'RMA1025YMX', 'Gris', 35, 65, 35)
    refrigeradores.append(x)
    x = Refrigerador('Whirlpool', '460', 'Gris', 40, 60, 40)
    refrigeradores.append(x)

def cargar_lavadoras():
    x = Lavadora('Whirlpool', '2095I', 'Gris', 30, 60, 40)
    lavadoras.append(x)
    x = Lavadora('Mabe', 'LMD1800B2', 'Gris', 35, 65, 35)
    lavadoras.append(x)
    x = Lavadora('Daewoo', 'DG361', 'Gris', 40, 60, 40)
    lavadoras.append(x)

def main():
    cargar_televisiones()
    cargar_refrigeradores()
    cargar_lavadoras()

    while True:
        print("¿Qué desea hacer?")
        opt = input("\t1. Cambiarle el canal a la tele.\n\t2. Meter algo a congelar al refri.\n\t3. Lavar algo.\n\t4. Salir.\n\t")
        if opt != '4':
            if opt == '1':
                print(televisiones[0].cambiar_canal())
            elif opt == '2':
                print(refrigeradores[0].congelar())
            elif opt == '3':
                print(lavadoras[0].lavar())
        else:
            break


if __name__ == '__main__':
    main()
