import abc

class raiz(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def ruta(self, ubicacion):
        print("/")
        pass

class Etc(raiz):
    def ruta(self, ubicacion):
        print(ubicacion + "etc")

class Var(raiz):
    def ruta(self, ubicacion):
        print(ubicacion + "var")

class Log(Var,raiz):
    def ruta(self, ubicacion):
        print(ubicacion + "log")


class Mail(Var,raiz):
    def ruta(self, ubicacion):
        print(ubicacion + "mail")


class Bin(raiz):
    def ruta(self, ubicacion):
        print(ubicacion + "bin")


class Usr(raiz):
    def ruta(self, ubicacion):
        print(ubicacion + "usr")


class Lib(Usr,raiz):
    def ruta(self, ubicacion):
        print(ubicacion + "lib")

class Local(Usr,raiz):
    def ruta(self, ubicacion):
        print(ubicacion + "local")

class Include(Usr,raiz):
    def ruta(self, ubicacion):
        print(ubicacion + "include")

class Home(raiz):
    def ruta(self, ubicacion):
        print(ubicacion + "home")

class Users(Home,raiz):
    def ruta(self, ubicacion):
        print(ubicacion + "home")

class Juan(Users,Home,raiz):
    def ruta(self, ubicacion):
        print(ubicacion + "home")

class Luis(Users,Home,raiz):
    def ruta(self, ubicacion):
        print(ubicacion + "home")





class Imprimiendo_ruta(raiz):
    def __init__(self):
        self.raizes = []

    def ruta(self, ubicacion):
        for ru in self.raizes:
            ru.ruta(ubicacion)

    def agregar_ruta(self, ru):
        self.raizes.append(ru)


if __name__ == '__main__':
    var1 = Var()
    var2 = Var()
    etc = Etc()

    imprimiendo_ruta = Imprimiendo_ruta()
    imprimiendo_ruta.agregar_ruta(var1)
    imprimiendo_ruta.agregar_ruta(var2)
    imprimiendo_ruta.agregar_ruta(etc)

    imprimiendo_ruta.ruta("/")
