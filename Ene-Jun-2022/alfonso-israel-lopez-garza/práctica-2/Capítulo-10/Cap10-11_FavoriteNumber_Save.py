from fileinput import filename
import json
try:
    favorite = int(input("Ingrese su numero favorito: "))
except ValueError:
    print("No es un numero.")
else:
    print("Recordare tu numero favorito.")
    filename = 'number.json'
    with open(filename, 'w' ) as f_obj:
        json.dump(favorite,f_obj)