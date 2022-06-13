#10.8
filenombres = ['perros.txt', 'gatos.txt']

for filenombre in filenombres:
    print("\lectura de archivo: " + filenombre)
    try:
        with open(filenombre) as filenombre:
            contents = filenombre.read()
            print(contents)
    
    except FileNotFoundError:
        print("  no es posible encontrar el archivo.")
    
    else:
        print("\leyendo aricho: " + filenombre)
        print(contents)