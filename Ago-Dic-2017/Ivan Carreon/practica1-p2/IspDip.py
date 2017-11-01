import abc

class Peleador(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def prepararseluchar(self):
        pass

class PeleadorDistancia(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def atacaquedistacia(self):
        pass

class PeleadorCuerpoCuerpo(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def ataquefisico(self):
        pass

class Poder:
    def getPoder(self):
        poder = 100
        return poder


class Dan(Peleador, PeleadorCuerpoCuerpo):
    def __init__(self,espiritu):
        self.espiritu = espiritu

    def getPower(self):
        print('Poder: {}Kg'.format(self.espiritu.getPoder() ))

    def prepararseluchar(self):
        print('*El luchador se prepara para el combate*')

    def ataquefisico(self):
        print('Ataque más poderoso: \n Atacar con todo lo que se pueda... hasta con la silla :v')

class Dhalsim(Peleador,PeleadorDistancia):
    def __init__(self,espiritu):
        self.espiritu = espiritu

    def getPower(self):
        print('Poder: {}Kg'.format(self.espiritu.getPoder() ))

    def prepararseluchar(self):
        print('*El combatiente se prepara para luchar*')

    def atacaquedistacia(self):
        print('Ataque más poderoso: \n Yoga Fire!!')

class Ryu(Peleador,PeleadorDistancia,PeleadorCuerpoCuerpo):
    def __init__(self,espiritu):
        self.espiritu = espiritu

    def getPower(self):
        print('Poder: {}Kg'.format(self.espiritu.getPoder() ))

    def prepararseluchar(self):
        print('*El peleador se prepara meditando antes del encuentro*')

    def atacaquedistacia(self):
        print('Ataque más poderoso: \n Shinku Hadouken!!!!!!!!!!!!!!!!')

    def ataquefisico(self):
        print('Ataque más poderoso: \n Shin Shoriuken!　と　Shinku Tatsumaki Senpukyaku!')
