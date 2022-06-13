#10.5
filenombre = 'programming_poll.txt'

respuesta = []
while True:
    respuestas = input("\nPorque te gusta la programacion? ")
    respuesta.append(respuestas)

    continuar_respuestas = input("Quieres que alguien mas pueda responder esto? ")
    if continuar_respuestas != 'y':
        break

with open(filenombre, 'a') as filenombre:
    for respuesta in respuesta:
        filenombre.write(respuesta + "\n")