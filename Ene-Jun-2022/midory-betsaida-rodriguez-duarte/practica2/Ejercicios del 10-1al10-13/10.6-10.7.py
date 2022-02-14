#10.6

try: 
    numero = int(input("Dame numero 1 :"))
    numero2 = int(input("Dame numero 2 :"))

    suma = numero + numero2
    print(suma)
    
except ValueError:
    print("Ese no es un numero entero.")

#10.7
while True:
    try: 
        numero = int(input("Dame numero 1 :"))
        numero2 = int(input("Dame numero 2 :"))

        suma = numero + numero2
        print(suma)
        break
    except ValueError:
        print("Ese no es un numero entero.")
    

        
