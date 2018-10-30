def show_magicians(wizar): #lista original que se estara modificando
    for magician in wizar:
        print(magician)

def make_great(wizar): #en esta funcion agregaremos "great" al inicio de los nombre de los wizar en la lista
    great_wizar = [] #se crea la lista de grean wizar

#    while wizar:
#        magician = wizar.pop() # ".pop()"nos permite quitar y devuelver el último elemento de la lista.
#        great_magician = magician + ' the Great' #tomamos el ultimo elemento con el .pop y al agregarlo coloa "the great"
#        great_wizar.append(great_magician) #appen es para agregar un elemento a la lista great_magician
    for magician in wizar: #puedo usar for magician in range(, len(great_wizar))
        great_wizar.append(magician + ' the Great')
    return great_wizar

wizar = ['Natsu', 'Lucy', 'Grey', 'Ainz'] #Lista de los magos
show_magicians(wizar) #Imprime el nombre de la lista
print("\n")
show_magicians(make_great(wizar)) #imprime le nombre de la lista modificada
