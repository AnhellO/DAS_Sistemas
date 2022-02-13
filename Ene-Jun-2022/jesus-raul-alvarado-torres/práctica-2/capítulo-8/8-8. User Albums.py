""" Practica 8-8 - User Albums

Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title.
Once you have that information, call make_album() with the
user’s input and print the dictionary that’s created.
Be sure to include a quit value in the while loop."""

def make_album(artista, titalb, pistas=0):
    AlbAtc = {f"Artista: {artista.title()} Titulo: {titalb.title()}"}
    if pistas != 0:
        AlbAtc = {f"Artista: {artista.title()} Titulo: {titalb.title()} Pistas: {pistas}"}
    return AlbAtc

#       Pedir datos
titulo_buscado = "\nIntroduce el album que buscas: "
artista_buscado = "Introduce el artista que buscas: "

#       Opcion para salir
print("Escribe 'exit' para salir")

while True:
    titalb = input(titulo_buscado)
    if titalb == 'exit':
        break
    artista = input(artista_buscado)
    if artista == 'exit':
        break

    album = make_album(artista, titalb)
    print(album)