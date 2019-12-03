#Ejercicio 3

#Para el ejemplo de código en el archivo adapter.py:

#Implementa la funcionalidad necesaria utilizando el patrón de diseño Adapter a nivel de objetos,
# de tal manera que podamos adaptar (valga la redundancia) cada uno de los diferentes enchufes
# para poder cargar instancias de la clase Smartphone

#Salida esperada: Voltaje: 5V -- Cargando...


class Smartphone():
    max_volt = 5

    @classmethod
    def _carga(cls, voltaje_entrante):
        if voltaje_entrante > cls.max_volt:
            print(f"Voltaje Entrada: {voltaje_entrante}V --Peligro--")
        else:
            print(f"Voltaje: {voltaje_entrante}V -- Cargando...")

    def carga(self, voltaje_entrante):
        """Carga el smartphone con el voltaje de entrada proporcionado."""
        self._carga(voltaje_entrante)

class Enchufes(object):
    voltaje_de_salida = None

class UK_Plug(Enchufes):
    voltaje_salida = 220

class US_Plug(Enchufes):
    voltaje_salida = 120

class AdapterUK(object):
    """AdapterUK encapsula al cliente (Smartphone) y al proveedor (UKSocket)."""

    voltaje_entrante = UK_Plug.voltaje_de_salida
    voltaje_de_salida = Smartphone.max_volt


class AdapterUS(object):
    """AdapterUS encapsula al cliente (Smartphone) y al proveedor (USSocket)."""

    voltaje_entrante = US_Plug.voltaje_de_salida
    voltaje_de_salida = Smartphone.max_volt

def main():
    smartphone = Smartphone()
    smartphone.carga(AdapterUK.voltaje_de_salida)
    smartphone.carga(AdapterUS.voltaje_de_salida)

if __name__ == '__main__':
    main()