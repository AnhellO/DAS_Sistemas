from mRange import mRange
from mArbolBinario import mBTree


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
    myRange = mRange(start = 1, stop = 10)
    myTree = mBTree(10)

    #Relleno el arbol
    for i in range(11,16):
        myTree.insert(i)


    for i in (recorrer_iterable(myRange)) + (recorrer_iterable(myTree)):
        print(i)

 

#############################

    # # ### Usando __iter__ y __next__:
    # for i in myRangeIter:
    #     print(i)