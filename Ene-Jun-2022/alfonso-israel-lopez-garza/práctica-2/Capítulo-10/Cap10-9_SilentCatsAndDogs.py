def libros(filename):
    '''Muestra el contenido del archivo'''
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        print(contents +"\n")


#usando la lista para ambos archivos
filenames = ['Cats.txt','Dogs.txt']
for filename in filenames:
    libros(filename)