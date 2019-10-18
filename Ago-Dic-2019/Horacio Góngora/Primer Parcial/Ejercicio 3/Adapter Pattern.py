class Smartphone():
    voltaje_maximo = 5

    @classmethod
    def _carga(cls, voltaje_entrante):
        if voltaje_entrante > cls.voltaje_maximo:
            print(f"Voltaje Entrada: {voltaje_entrante}V Mestoy quemando :C!!!")
        else:
            print(f"Voltaje Salida: {voltaje_entrante}V -- Cargando...")

    def carga(self, voltaje_entrante):
        """Carga el smartphone con el voltaje de entrada proporcionado."""
        self._carga(voltaje_entrante)

class Enchufe(object):
    voltaje_de_salida = None

class EnchufeEuropeo(Enchufe):
    voltaje_de_salida = 220

class EnchufeAmericano(Enchufe):
    voltaje_de_salida = 120

class AdapterEuropeo(object):
    voltaje_entrante = EnchufeEuropeo.voltaje_de_salida
    voltaje_de_salida = Smartphone.voltaje_maximo


class AdapterAmericano(object):
    voltaje_entrante = EnchufeAmericano.voltaje_de_salida
    voltaje_de_salida = Smartphone.voltaje_maximo

def main():
    smartphone = Smartphone()
    smartphone.carga(AdapterEuropeo.voltaje_de_salida)
    smartphone.carga(AdapterAmericano.voltaje_de_salida)

if __name__ == '__main__':
    main()