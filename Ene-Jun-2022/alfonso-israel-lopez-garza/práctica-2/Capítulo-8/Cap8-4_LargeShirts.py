def make_shirt(size='Large', msg='I love Python.'):
    '''Muestra el tamaño de la playera, junto con el texto impreso en ella.
        Ahora con valores por Default'''
    print(f"El tamaño de la playera es {size} y el texto en ella es {msg}")

make_shirt() #Usando los valores por default.
make_shirt('Medium') #Enviando solo un argumento (La primera variable tomara ese valor).
make_shirt('Small','I love Java') #Enviando el segundo parametro con sus argumentos.