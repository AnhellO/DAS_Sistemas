from abc import ABCMeta, abstractmethod

class Banda:
    __metaclass__ = ABCMeta

    @abstractmethod
    def banda(self):
        self.nombre = args.get('nombre')
        self.integrantes = args.get('integrantes')
        self.genero = args.get('genero')
        self.logo = args.get('logo')

class Bailar:
    __metaclass__ = ABCMeta

    @abstractmethod
    def baile(self):
        pass

class Premios:
    __metaclass__=ABCMeta

    @abstractmethod
    def premios(self):
        pass


class AbstractBanda(Banda,Bailar,Premios):
        pass

class Work(AbstractBanda):
    def banda(self):
        print(nombre,integrantes,genero,logo)
    def Bailar(self):
        print("SI SE PUEDE BAILAR")

class Work2(AbstractBanda):
    def banda(self):
        print(nombre,integrantes,genero,logo)
    def premios(self):
        print("Premios")

    def main():
        work=Work()
        work2=Work2()
