
File_to_Read = "Ene-Jun-2022/david-navoa-acevedo/Practica-2/Capitulo_10/Ejercicio_1/Learning_python.txt"
def changing_words(word, replaced_word):
    
    with open(File_to_Read) as file_opened:
        list = file_opened.readlines()

    for each_line in list:
       print(each_line.rstrip().replace(word, replaced_word))


changing_words('Python', 'C')
