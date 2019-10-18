import abc
class Smartphone(object):
    """docstring for Smartphone"""
    voltaje_maximo = 5

    def carga(self, enchufe):
        """Carga el smartphone con el voltaje de entrada proporcionado."""
        self._carga(enchufe.voltaje_de_salida)

    @classmethod
    def _carga(cls, voltaje_entrante):
        if voltaje_entrante > cls.voltaje_maximo:
            print('Voltaje: {}V -- Mestoy quemando :C!!!'.format(voltaje_entrante))
        else:
            print('Voltaje: {}V -- Cargando...'.format(voltaje_entrante))


class Enchufe(object):
    """docstring for Enchufe"""
    voltaje_de_salida = None

class EnchufeEuropeo(Enchufe):
    """docstring for EnchufeEuropeo"""
    voltaje_de_salida = 220

class EnchufeAmericano(Enchufe):
    """docstring for EnchufeAmericano"""
    voltaje_de_salida = 110


#smartphone = Smartphone()
#smartphone.carga(EnchufeAmericano) # Mestoy quemando :C!!!
class Target(metaclass=abc.ABCMeta):
    def __init__(self):
        self._adaptee = Adaptee()

    @abc.abstractmethod
    def request(self):
        pass

class Adapter(Target):
    def request(self, enchufe):
        self.enchufe = enchufe
        if self.enchufe == 220:
            self.enchufe = self.enchufe * ((581) / (25000))
            self._adaptee.carga(self.enchufe)
        elif self.enchufe == 110:
            self.enchufe = self.enchufe * ((952) / (20000)) 
            self._adaptee.carga(self.enchufe)
class Adaptee():
    """docstring for Smartphone"""
    voltaje_maximo = 5

    def carga(self, enchufe):
        """Carga el smartphone con el voltaje de entrada proporcionado."""
        self._carga(enchufe.voltaje_de_salida)

    @classmethod
    def _carga(cls, voltaje_entrante):
        if voltaje_entrante > cls.voltaje_maximo:
            print('Voltaje: {}V -- Mestoy quemando :C!!!'.format(voltaje_entrante))
        else:
            print('Voltaje: {}V -- Cargando...'.format(voltaje_entrante))

def main():
    adapter = Adapter()
    print(adapter.request(EnchufeEuropeo))
if __name__ == '__main__':
    main()