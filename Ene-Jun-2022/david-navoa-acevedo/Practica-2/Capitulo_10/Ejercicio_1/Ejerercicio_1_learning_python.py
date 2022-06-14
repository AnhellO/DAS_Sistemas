

File_to_Read = "Ene-Jun-2022/david-navoa-acevedo/Practica-2/Capitulo_10/Ejercicio_1/Learning_python.txt"
with open(File_to_Read) as file_object:
    lines = file_object.read()

def times_to_read(number_of_times):

    x = 0
    while x != number_of_times:
        print(lines)
        x += 1

def storing_file():
    
    with open(File_to_Read) as file_opened:
        list = file_opened.readlines()

    for each_line in list:
        print(each_line.rstrip())

#print(lines) 
#times_to_read(3)
#storing_file()