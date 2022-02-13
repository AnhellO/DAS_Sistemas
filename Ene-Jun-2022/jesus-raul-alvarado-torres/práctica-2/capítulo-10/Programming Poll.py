filename = 'programming_poll.txt'

respuestas = []
while True:
    respuesta = input("\n¿Por que te gusta programar?")
    respuestas.append(respuesta)

    continue_poll = input("¿Deseas terminar la encuesta? (y/n) ")
    if continue_poll != 'n':
        break

with open(filename, 'a') as f:
    for respuesta in respuestas:
        f.write(respuesta + "\n")