def show_magicians(wizar): #Imprimir los nombres de los magos en la lista
    for magician in wizar:
        print(magician.title()) #.title() me devuelve una copia de la cadena en la que los primeros caracteres aparecen en mayúscula.

wizar = ['natsu', 'lucy', 'grey', 'ainz']
show_magicians(wizar)
