import abc

class raiz(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add(self, dir):
        pass

#Salario es la hoja
class carpeta(raiz):

    def add(self, dir): 
        print(dir)

class Directory(raiz):
    def __init__(self):
        self.directorio = []

    def add(self, dir):
        self.directorio.append(dir)


    def imprimirres(self,d):
        for item in self.directorio:
            if item == d:
                return self.directorio

    def remove(self, sh):
        self.directorio.remove(sh)

    def clear(self):
        print("eliminaste directorio ")
        self.directorio = []

if __name__ == '__main__':
    dir1 = carpeta()
    cart = Directory()
    cart.add("bin")

    dir2 = carpeta()
    cart2 = Directory()
    cart2.add("user")

    subDir2_1 = carpeta()
    subDir2_2 = carpeta()
    cart2_2 = Directory()
    cart2_2.add("b")
    cart2_2.add("a")
    cart2.add(cart2)

    dir3 = carpeta()
    cart3 = Directory()
    cart3.add("x")

    x=cart2.imprimirres("bin")
    print(x)
