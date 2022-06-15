""" Practica 8-10 - Great Magicians

Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the
list of magicians by adding the phrase the Great to each magician’s name.
Call show_magicians() to see that the list has actually been modified"""

def show_messages(mensajes):
    print("Mostrando todos los mensajes:")
    for mensaje in mensajes:
        print(mensaje)
        
def send_messages(mensajes, mensajes_enviados):
    print("\nEnviando mensajes:")
    while mensajes:
        mensaje_actual = mensajes.pop()
        print(mensaje_actual)
        mensajes_enviados.append(mensaje_actual)

mensajes = ["Hola", "Hello", "Hi"]
show_messages(mensajes)

mensajes_enviados = []
send_messages(mensajes, mensajes_enviados)

print("\nFinal lists:")
print(mensajes)
print(mensajes_enviados)