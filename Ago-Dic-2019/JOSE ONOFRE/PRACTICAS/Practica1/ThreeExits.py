prompt= "\nPor favor escriba su edad: "
prompt+= "\nEscriba '-1' cuando haya terminado"

while True:
    edad= int(input(prompt))

    if edad == -1:
        break
    elif edad < 3 and edad!=0 :
        print("Su entrada es gratuita")
    elif edad >= 3 and edad <12:
        print("Son $10 por favor")
    elif edad >=12:
        print("Son $15 por favor")  
    elif edad == 0:
        print("Edad no valida, intente de nuevo")

