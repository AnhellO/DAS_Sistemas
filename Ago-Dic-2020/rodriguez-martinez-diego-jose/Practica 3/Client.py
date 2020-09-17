from mRange import mRange
from mArbolBinario import mBTree


def recorrerIterable(iterable):
    ### Input: Iterable
    ### Output: Sus elementos printeados, si es que tengo interfaz para recorrerlo
    
    elementosIterable = []

    try:

        #Iterador concreto
        iterador = iterable.createIterator()
        
        while iterador.hasMore():
            elementosIterable.append(iterador.getNext())

    except Exception:
        raise ValueError("Interfaz no disponible")

    return elementosIterable



if __name__ == "__main__":

    #Colecciones concretas
    myRange = mRange(start = 1, stop = 10)
    myTree = mBTree(10)

    #Relleno el arbol
    for i in range(11,16):
        myTree.insert(i)


    for i in (recorrerIterable(myRange)) + (recorrerIterable(myTree)):
        print(i)

 

#############################

    # # ### Usando __iter__ y __next__:
    # for i in myRangeIter:
    #     print(i)