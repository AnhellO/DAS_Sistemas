invitados=['Freddie Mercury','Chester Bennington','Brian May','John Deacon','Roger Taylor']

message1="El invitado " + invitados[1].title() + " no asistira a la cena" 

print(message1)

invitados[1]="Michael Jackson"

for i in range(len(invitados)):
    message="Hola como estas " + invitados[i].title() + " te invito a una cena esta noche en el restaurante Meson Principal."

    print(message)