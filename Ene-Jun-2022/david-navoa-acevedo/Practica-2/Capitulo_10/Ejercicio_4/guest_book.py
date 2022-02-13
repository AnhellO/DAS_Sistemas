guest_book_txt = "Ene-Jun-2022/david-navoa-acevedo/Practica-2/Capitulo_10/Ejercicio_4/guest_book.txt"

def greethings():

    print("please write Your name: ")
    print("(just press enter at any time to quit)\n")

    while True:
        name = input("name: ")

        with open(guest_book_txt, 'a') as opened_file:
            opened_file.write(name)
            opened_file.write("\n")
            
        if name == "":
            break
        print("Greetings! " + name + " Enjoy your visit!")

greethings()