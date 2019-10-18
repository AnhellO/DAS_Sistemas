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

class EnchufeAdaptadorEur(EnchufeEuropeo):
    voltaje_de_salida=5



smartphone = Smartphone()
smartphone.carga(EnchufeAdaptadorEur(EnchufeEuropeo)) # Mestoy quemando :C!!!
