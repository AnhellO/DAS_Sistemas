print("Escribe quit para salir, gracias.\n")

while True:
 try:
     y = input("dime un numero: ")
     if y == 'q':
            break
     y = int(y)

     x = input("dime un numero: ")
     if x == 'q':
             break
     x = int(x)

 except ValueError:
   print("necesito un numero.")

 else:
  sumas = y + x
  print("la suma es " + str(y) + " y " + str(x) + " es" + str(sumas) + ".")
