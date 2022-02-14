#10.9

filenombres = ['perros.txt', 'gatos.txt']

for filenombre in filenombres:
    print("\lectura de archivo: " + filenombre)
    try:
        with open(filenombre) as filenombre:
            contents = filenombre.read()
            print(contents)
    
    except FileNotFoundError:
         pass

    else:
        print("\nlectura archivos: " + filenombre)
        print(contents)