invitados=['Freddie Mercury','Chester Bennington','Brian May','John Deacon','Roger Taylor']

invitados.insert(0,'Michael Jackson')

invitados.insert(2,'Keanu Reeves')

invitados.append('James Hetfield')


for i in range(len(invitados)):
    message="Hola como estas " + invitados[i].title() + " te invito a una cena esta noche en el restaurante Meson Principal."

    print(message)