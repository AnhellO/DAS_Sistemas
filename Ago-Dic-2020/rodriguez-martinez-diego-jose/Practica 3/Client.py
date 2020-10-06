from mRange import MRange
from mArbolBinario import MBTree


def recorrer_iterable(iterable):
    ### Input: Iterable
    ### Output: Sus elementos printeados, si es que tengo interfaz para recorrerlo
    
    elementos_iterable = []

    try:

        #Iterador concreto
        iterador = iterable.create_iterator()
        
        while iterador.has_more():
            elementos_iterable.append(iterador.get_next())

    except Exception:
        raise ValueError("Interfaz no disponible")

    return elementos_iterable



if __name__ == "__main__":

    #Colecciones concretas
    my_range = MRange(start = 1, stop = 10)
    my_tree = MBTree(10)

    #Relleno el arbol
    for i in range(11,16):
        my_tree.insert(i)


    for i in (recorrer_iterable(my_range)) + (recorrer_iterable(my_tree)):
        print(i)

 

#############################

    # # ### Usando __iter__ y __next__:
    # for i in myRangeIter:
    #     print(i)