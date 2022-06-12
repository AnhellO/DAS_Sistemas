def make_shirt(size, message):
    '''Muestra el tamaño de la playera, junto con el texto impreso en ella.'''
    print(f"El tamaño de la playera es: {size} y el texto en ella es: {message}")

make_shirt('Chica','Felicidades') #Llamado de la función enviando Positional Arguments
make_shirt(size = 'Grande', message = 'Hasta luego!') #Llamando a la función make_shirt usando Keyword arguments