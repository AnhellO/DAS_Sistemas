from IIterator import IIterator

class BTIterator(IIterator):

    """Iterador Concreto del Binary Tree para el ejemplo de patron Iterator"""

    def __init__(self, root):
        
        # Array con todos los nodos sorteados 
        self.nodes_sorted = []
        
        # index del elemento mas chico en el arbol
        self.index = -1
        
        # Flatteneo el arbol a una lista, como es un arbol binario ya va a venir ordenada
        self.inorder(root)
        
    def inorder(self, root):
        if not root:
            return

        self.inorder(root._left)
        self.nodes_sorted.append(root._val)
        self.inorder(root._right)    

    def getNext(self):
        #Como ya esta el arbol en forma de lista, para conseguir el siguiente solo la recorre y aumento el indice cada vez

        self.index += 1
        return self.nodes_sorted[self.index]

    def hasMore(self):
        #Como ya esta el arbol en forma de lista el len de la lista conseguida son los numeros totales de elementos

        return self.index + 1 < len(self.nodes_sorted)