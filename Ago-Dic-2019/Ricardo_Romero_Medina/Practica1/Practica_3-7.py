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