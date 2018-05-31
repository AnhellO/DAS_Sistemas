import abc

class Raiz(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def imprimir(self, ruta):
        print("Estas en la ruta: /")
        pass

class Etc(Raiz):
    def imprimir(self, ruta):
        print("Estas en la ruta: /etc")


class Var(Raiz):
    def imprimir(self, ruta):
        print("Estas en la ruta: /var")


class Log(Var):
    def imprimir(self, ruta):
        print("Estas en la ruta: /var/log")


class Mail(Var):
    def imprimir(self, ruta):
        print("Estas en la ruta: /var/mail")
    

class Bin(Raiz):
    def imprimir(self, ruta):
        print("Estas en la ruta: /bin")


class Usr(Raiz):
    def imprimir(self, ruta):
        print("Estas en la ruta: /usr")


class Lib(Usr):
    def imprimir(self, ruta):
        print("Estas en la ruta: /usr/lib")


class Include(Usr):
    def imprimir(self, ruta):
        print("Estas en la ruta: /usr/include")


class Local(Usr):
    def imprimir(self, ruta):
        print("Estas en la ruta: /usr/local")


class Home(Raiz):
    def imprimir(self, ruta):
        print("Estas en la ruta: /home")


class Users(Home):
    def imprimir(self, ruta):
        print("Estas en la ruta: /home/users")


class Juan(Users):
    def imprimir(self, ruta):
        print("Estas en la ruta: /home/users/juan")


class Luis(Users):
    def imprimir(self, ruta):
        print("Estas en la ruta: /home/users/luis")

class Imprimiendo(Raiz):
    def __init__(self):
        self.ruta = []

    def imprimir(self, ruta):
        for rt in self.ruta:
            rt.imprimir(ruta)
    
    def agregar(self, rt):
        self.ruta.append(rt)

    def remover(self, rt):
        self.ruta.remove(rt)

    def limpiar(self):
        print("Se vaciaron todas las rutas de Unix")
        self.ruta = []


if __name__ == "__main__":
    #rais = Raiz()
    etc = Etc()
    var = Var()
    log = Log()
    mail = Mail()
    binn = Bin()
    usr = Usr()
    lib = Lib()
    include = Include()
    local = Local()
    home = Home()
    users = Users()
    juan = Juan()
    luis = Luis()

    printing = Imprimiendo()
    printing.agregar(etc)
    printing.agregar(var)
    printing.agregar(log)
    printing.agregar(mail)
    printing.agregar(binn)
    printing.agregar(usr)
    printing.agregar(lib)
    printing.agregar(include)
    printing.agregar(local)
    printing.agregar(home)
    printing.agregar(users)
    printing.agregar(juan)
    printing.agregar(luis)

    printing.imprimir("")