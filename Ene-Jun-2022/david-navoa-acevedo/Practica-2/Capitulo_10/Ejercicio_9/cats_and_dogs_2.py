dogos = "Ene-Jun-2022/david-navoa-acevedo/Practica-2/Capitulo_10/Ejercicio_9/dogs.txt"
cats = "Ene-Jun-2022/david-navoa-acevedo/Practica-2/Capitulo_10/Ejercicio_9/cats.txt"

animals = [dogos, cats]

for each_animal in animals:

    
    try:
        with open(each_animal) as animal_file:
            animal_names = animal_file.read()
            
    except FileNotFoundError:
        pass
    else:
        print("\nnow showing " + each_animal + " file \n")
        print(animal_names)