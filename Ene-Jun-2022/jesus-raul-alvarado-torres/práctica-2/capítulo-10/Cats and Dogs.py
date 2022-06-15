filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print("\nLeyendo archivo: " + filename)
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
            
    except FileNotFoundError:
        print("El archivo no fue encontrado.")