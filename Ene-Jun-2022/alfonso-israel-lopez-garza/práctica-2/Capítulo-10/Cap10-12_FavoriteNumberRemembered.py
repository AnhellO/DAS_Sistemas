from fileinput import filename
import json

#Guardado
def guardarnumero():
    try:
        favorite = int(input("Ingrese su numero favorito: "))
    except ValueError:
        print("No es un numero.")
    else:
        print("Recordare tu numero favorito.")
        filename = 'number.json'
        with open(filename, 'w' ) as f_obj:
            json.dump(favorite,f_obj)

def getNumero():
    ##Carga
    filename = 'number.json'
    with open(filename) as f_obj:
        number = json.load(f_obj)

    return number


numero = getNumero()
if numero:
    print("Tu numero favorito es: " +str(numero))
else:
    guardarnumero()
    numero = getNumero()
    print('Tu numero favorito es:' +str(numero))