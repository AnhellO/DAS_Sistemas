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
    print("Me entraron 220") #Verificar la salida



class EnchufeAmericano(Enchufe):
    """docstring for EnchufeAmericano"""
    voltaje_de_salida = 110
    print("Me entraron 110")#Verificar la salida

class EuropeoAdapter(object):
    voltaje_entrante = EnchufeAmericano.voltaje_de_salida #Tomamos El voltaje de salida del Enchufeamericano para convertirlo al entrante del Europeo que se convertira en una salida de 5v
    voltaje_de_salida = Smartphone.voltaje_maximo
    print("Convirtiendo: ",voltaje_entrante,"Volts a ",voltaje_de_salida," volts")
  
class AmericanoAdapter(object):
    voltaje_entrante = EnchufeEuropeo.voltaje_de_salida #Tomameos El voltaje de salida del EnchufeEuropeo para convertirlo al entrante del Americano que se convertira en una salida de 5v
    voltaje_de_salida = Smartphone.voltaje_maximo
    print("Convirtiendo: ",voltaje_entrante,"Volts a ",voltaje_de_salida," volts")

smartphone = Smartphone()
smartphone.carga(EuropeoAdapter) # Mestoy quemando :C!!!

smartphone = Smartphone()
smartphone.carga(AmericanoAdapter)