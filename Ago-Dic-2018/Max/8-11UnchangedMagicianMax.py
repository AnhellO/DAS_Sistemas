def show_magicians(wizar): #lista original que se estara modificando
    for magician in wizar:
        print(magician)

def make_great(wizar): #en esta funcion agregaremos "great" al inicio de los nombre de los wizar en la lista
    great_wizar = [] #se crea la lista de grean wizar

    for magician in wizar:
        great_wizar.append(magician + ' the Great')
    return great_wizar

wizar = ['Natsu', 'Lucy', 'Grey', 'Ainz'] #Lista de los magos
show_magicians(wizar) #Imprime el nombre de la lista
print("\n")
ListTemp = wizar[:] #creo la copia de la lista original
show_magicians(make_great(wizar)) #Imprimo lista modificada
print("\n")
show_magicians(ListTemp) #Imprimo lista original
