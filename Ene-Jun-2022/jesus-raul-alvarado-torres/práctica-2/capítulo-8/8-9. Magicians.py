""" Practica 8-9 - Magicians

Make a list of magician’s names.
Pass the list to a function called show_magicians(),
which prints the name of each magician in the list ."""

def show_messages(mensaje):
    for mensaje in mensaje:
        print(mensaje)

mensaje = ["Hola soy el mensaje 1", "Hi i am the message 2", "Salut je suis le message 3"]
show_messages(mensaje)