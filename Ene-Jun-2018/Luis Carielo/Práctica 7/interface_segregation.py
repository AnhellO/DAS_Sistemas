from abc import ABCMeta, abstractmethod

class Banda:
    __metaclass__ = ABCMeta

    @abstractmethod
    def banda_musical(self):
        self.nombre = args.get('nombre')
        self.integrantes = args.get('integrantes')
        self.genero = args.get('genero')
        self.logo = args.get('logo')

class Bailar:
    __metaclass__ = ABCMeta

    @abstractmethod
    def baile_genero(self):
        pass

class Premios:
    __metaclass__=ABCMeta

    @abstractmethod
    def premios_musicales(self):
        pass


class AbstractBanda(Banda,Bailar,Premios):
        pass

class Job(AbstractBanda):
    def banda_musical(self):
        print(nombre,integrantes,genero,logo)
    def Bailar(self):
        print("¡Ah bailar!")

class Job2(AbstractBanda):
    def banda_musical(self):
        print(nombre,integrantes,genero,logo)
    def premios_musicales(self):
        print("Premios")

    def main():
        job=Job()
        job2=Job2()