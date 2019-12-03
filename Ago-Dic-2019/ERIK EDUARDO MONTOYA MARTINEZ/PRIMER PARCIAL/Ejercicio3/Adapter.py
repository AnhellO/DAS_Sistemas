class Smartphone(object):

   voltaje_maximo = 5

   @classmethod
   def _carga(cls, voltaje_entrante):
       if voltaje_entrante > cls.voltaje_maximo:
           print("Voltaje: {}V -- Mestoy quemando :C!!!".format(voltaje_entrante))
       else:
           print("Voltaje: {}V -- Cargando...".format(voltaje_entrante))

   def carga(self, voltaje_entrante):
       """Charge the phone with the given input voltage."""
       self._carga(voltaje_entrante)

class Enchufe(object):
    voltaje_de_salida = None


class EnchufeEuropeo(Enchufe):
    voltaje_de_salida = 220


class EnchufeAmericano(Enchufe):
    output_voltage = 110


class AdaptadorEuropeo(object):

    voltaje_entrante = EnchufeEuropeo.voltaje_de_salida
    voltaje_de_salida = Smartphone.voltaje_maximo


class AdaptadorAmericano(object):

   voltaje_entrante = EnchufeAmericano.voltaje_de_salida
   voltaje_de_salida = Smartphone.voltaje_maximo

class AdaptadorSmartphoneEuropeo(Smartphone, EnchufeEuropeo):
       pass


class AdaptadorSmartphoneEuropeo(Smartphone, EnchufeAmericano):
    pass


def main():
    smartphone = Smartphone()
    smartphone.carga(AdaptadorEuropeo.voltaje_de_salida)
    smartphone.carga(AdaptadorAmericano.voltaje_de_salida)

if __name__ == '__main__':
    main()