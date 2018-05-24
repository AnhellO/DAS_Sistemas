import unix

class raiz(metaclass=unix.UNIXMeta):
    @unix.abstractmethod
    def archivob(self, archivos):
        print("ESTAS EN LA RAIZ")
        pass

#HOJA
class etc(raiz):

    def __init__(self,archivo):
        print("ESTAS EN ETC)
        self.archivo = archivo
    def archivob(self, archivos):
        return self.archivo
#HOJA
class var(raiz):

    def __init__(self,archivo):
        self.archivo = archivo
    def archivob(self, archivos):
        return self.archivo
#COMPOSITE
class log(raiz):
    def __init__(self):
        self.raiz = []

    def archivob(self, archivos):
        self.archivob = 0
        for sh in self.raiz:
            self.archivob = print("LOG")
        return self.archivob

    def add(self, sh):
        self.raiz.append(sh)

    #def remove(self, sh):
        #self.raiz.remove(sh)

    def clear(self):
        print("FINAL ")
self.raiz = []

class mail(raiz):
    def __init__(self):
        self.raiz = []

    def archivob(self, archivos):
        self.archivob = 0
        for sh in self.raiz:
            self.archivob = print("mail")
        return self.archivob

    def add(self, sh):
        self.raiz.append(sh)

    #def remove(self, sh):
        #self.raiz.remove(sh)

    def clear(self):
        print("FINAL ")

class bin(raiz):

    def __init__(self,archivo):
        self.archivo = archivo
    def archivob(self, archivos):
        return self.archivo

class usr(raiz):

    def __init__(self,archivo):
        self.archivo = archivo
    def archivob(self, archivos):
        return self.archivo

class lib(raiz):
    def __init__(self):
        self.raiz = []

    def archivob(self, archivos):
        self.archivob = 0
        for sh in self.raiz:
            self.archivob = print("lib")
        return self.archivob

    def add(self, sh):
        self.raiz.append(sh)

    #def remove(self, sh):
        #self.raiz.remove(sh)

    def clear(self):
        print("FINAL ")
self.raiz = []

class include(raiz):
    def __init__(self):
        self.raiz = []

    def archivob(self, archivos):
        self.archivob = 0
        for sh in self.raiz:
            self.archivob = print("include")
        return self.archivob

    def add(self, sh):
        self.raiz.append(sh)

    #def remove(self, sh):
        #self.raiz.remove(sh)

    def clear(self):
        print("FINAL ")

class local(raiz):
    def __init__(self):
        self.raiz = []

    def archivob(self, archivos):
        self.archivob = 0
        for sh in self.raiz:
            self.archivob = print("local")
        return self.archivob

    def add(self, sh):
        self.raiz.append(sh)

    #def remove(self, sh):
        #self.raiz.remove(sh)

    def clear(self):
        print("FINAL ")

class home(raiz):

    def __init__(self,archivo):
        self.archivo = archivo
    def archivob(self, archivos):
        return self.archivo

class juan(raiz):
    def __init__(self):
        self.raiz = []

    def archivob(self, archivos):
        self.archivob = 0
        for sh in self.raiz:
            self.archivob = print("juan")
        return self.archivob

    def add(self, sh):
        self.raiz.append(sh)

    #def remove(self, sh):
        #self.raiz.remove(sh)

    def clear(self):
        print("FINAL ")

class luis(raiz):
    def __init__(self):
        self.raiz = []

    def archivob(self, archivos):
        self.archivob = 0
        for sh in self.raiz:
            self.archivob = print("luis")
        return self.archivob

    def add(self, sh):
        self.raiz.append(sh)

    #def remove(self, sh):
        #self.raiz.remove(sh)

    def clear(self):
        print("FINAL ")

self.raiz = []

if __name__ == '__main__':
    arch1 = raiz()
    arch2 = ETC()
    arch3 = var()
    arch4 = log()
    arch5 = mail()
    arch6 = bin()
    arch7= luis()
    arch8 = juan()
    arch9 = lib()
    arch10 = include()
    arch11 = local()
    arch12 = home()
