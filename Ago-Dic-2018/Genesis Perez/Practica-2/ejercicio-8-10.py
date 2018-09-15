magos = ["Dynamo", "Enmascarado", "Chris Angel", "Mago De Oz"]

def show_magicians(lista):
  for mago in lista:
    print(mago)

show_magicians(magos)

def make_great(lista):
    for mago in lista:
        presentacion = "The Great " + mago.title()
        print(presentacion)

make_great(magos)
show_magicians(magos)
