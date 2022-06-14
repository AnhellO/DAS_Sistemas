
dogos = "Ene-Jun-2022/david-navoa-acevedo/Practica-2/Capitulo_10/Ejercicio_8/dogs.txt"
cats = "Ene-Jun-2022/david-navoa-acevedo/Practica-2/Capitulo_10/Ejercicio_8/cats.txt"

animals = [dogos, cats]

for each_animal in animals:

    print("\nnow showing " + each_animal + " file \n")
    try:
        with open(each_animal) as animal_file:
            animal_names = animal_file.read()
            print(animal_names)
    except FileNotFoundError:
        print("\nwe have problems... one file was not found :(\n")