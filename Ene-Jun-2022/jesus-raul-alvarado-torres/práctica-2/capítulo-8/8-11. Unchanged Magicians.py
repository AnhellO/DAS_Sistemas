""" Practica 8-11 - Unchanged Magicians

Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original
names and one list with the Great added to each magician’s name."""

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
send_messages(mensajes[:], mensajes_enviados)

print("\nFinal lists:")
print(mensajes)
print(mensajes_enviados)