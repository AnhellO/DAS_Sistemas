from lavadora import Lavadora
from refrigerador import refrigerador
from television import refrigerador

lavadoras = []
refris= []
teles = []

def listar_lavadoras():
    lavadora1 = Lavadora('Whirlpool', '2095I', 'Gris', 30, 60, 40)
    lavadoras.append(lavadora1)
    lavadora1 = Lavadora('Mabe', 'LMD1800B2', 'Gris', 35, 65, 35)
    lavadoras.append(lavadora1)
    lavadora1 = Lavadora('Daewoo', 'DG361', 'Gris', 40, 60, 40)
    lavadoras.append(lavadora1)
    
def listar_refrigeradores():
     refri = Refrigerador('GT40', 'MABE', 'Gris', 'mb7002619pg', 220)
     refris.append(refri)
     refri = Refrigerador('Dual wt400s', 'Whirlpool', 'Blanco', 'WH90DHB27G', 220)
     refris.append(refri)
     refri = Refrigerador('520L', 'GE', 'Silver', 'GE195rmbmxx01',220)
     refris.append(refri)

def listar_televisiones():
    tv = Television('Elite24', 'Sanyo', 'negro', 'dk453hhfh6', 110)
    teles.append(tv)
    tv = Television('ElementLux', 'Element', 'negro', 'af13fd52', 110)
    teles.append(tv)
    tv= Television('HomePro', 'LG', 'negro', 'SHJ23H3H5', 110)
    teles.append(tv)
 



def main():
    listar_televisiones()
    listar_refrigeradores()
    listar_lavadoras()

    print ("\t1- Exprimir ropa")
    print ("\t2- Hacer hielos")
    print ("\t3- Conectarse a Internet")

while True:

    opcion= input ("Selecciona una opcion...")

    if opcion == "1":
        print(lavadoras[0].exprimir())
        print("Estas usando la lavadora, la ropa se esta exprimiendo")

    elif opcion == "2":
        print(refris[0].hacer_hielo())
        print ("Estas usando el refrigerador, hay hielos")

    elif opcion == "3":
        print(teles[0].conectarse_internet())
        print ("Estas usando la televisión, ya puedes usar Netflix ;)")
        
    else:
        break


if __name__ == '__main__':
    main()




















