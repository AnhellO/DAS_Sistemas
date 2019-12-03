invitados=['Freddie Mercury','Chester Bennington','Brian May','John Deacon','Roger Taylor']

for i in range(len(invitados)):
    message="Hola como estas " + invitados[i].title() + " te invito a una cena esta noche en el restaurante Meson Principal."

    print(message)

print("Se invitaron a " , len(invitados) , "personas.")

invitados=['Freddie Mercury','Chester Bennington','Brian May','John Deacon','Roger Taylor']

message1="El invitado " + invitados[1].title() + " no asistira a la cena" 

print(message1)

invitados[1]="Michael Jackson"

for i in range(len(invitados)):
    message="Hola como estas " + invitados[i].title() + " te invito a una cena esta noche en el restaurante Meson Principal."

    print(message)

print("Se invitaron a " , len(invitados) , "personas.")

invitados=['Freddie Mercury','Chester Bennington','Brian May','John Deacon','Roger Taylor']

invitados.insert(0,'Michael Jackson')

invitados.insert(2,'Keanu Reeves')

invitados.append('James Hetfield')


for i in range(len(invitados)):
    message="Hola como estas " + invitados[i].title() + " te invito a una cena esta noche en el restaurante Meson Principal."

    print(message)

print("Se invitaron a " , len(invitados) , "personas.")

invitados=['Freddie Mercury','Chester Bennington','Brian May','John Deacon','Roger Taylor']

message="Solo se puede invitar a dos personas mas debido a que la mesa nueva no llegara a tiempo"

print(message)

for i in range(len(invitados)):
    if len(invitados) > 2:
        invitados.pop(i)
        i = 0

for i in range(len(invitados)):
    message2="Hola como estas " + invitados[i].title() + " te invito a una cena esta noche en el restaurante Meson Principal."

    print(message2)

print("Se invitaron a " , len(invitados) , "personas.")