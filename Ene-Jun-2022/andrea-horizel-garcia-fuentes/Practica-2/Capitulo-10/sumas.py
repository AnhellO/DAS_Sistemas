#10.6
try:
    y = input("dime un numero: ")
    y = int(y)

    x = input("dime un numero: ")
    x = int(x)

except ValueError:
    print("necesito un numero.")

else:
    sumas = y + x
    print("la suma es " + str(y) + " y " + str(x) + " es" + str(sumas) + ".")