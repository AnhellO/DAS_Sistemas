responses_file = "Ene-Jun-2022/david-navoa-acevedo/Practica-2/Capitulo_10/Ejercicio_5/Responses.txt"

def people_responses_function():


    print("\n(just press enter at any time to quit)\n")

    while True:
        response = input("please write why you like programming: ")

        with open(responses_file, 'a') as opened_file:
            opened_file.write(response)
            opened_file.write("\n\n")
            
        if response == "":
            break

people_responses_function()