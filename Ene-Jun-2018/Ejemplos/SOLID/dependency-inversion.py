class Engine(object):
    """Example engine base class.

    Engine is a heart of every car. Engine is a very common term and could be
    implemented in very different ways.
    """
    def __init__(self, **args):
        self._potencia = args.get('potencia')
        self._tipo = None

    def __str__(self):
        return "Motor: {}\nPotencia: {}".format(self._tipo, self._potencia)

    def tipo(self):
        return self._tipo

class GasolineEngine(Engine):
    """Gasoline engine."""
    def __init__(self, **args):
        super().__init__(**args)
        self._tipo = 'Gasoline'

class DieselEngine(Engine):
    """Diesel engine."""
    def __init__(self, **args):
        super().__init__(**args)
        self._tipo = 'Diesel'

class ElectroEngine(Engine):
    """Electro engine."""
    def __init__(self, **args):
        super().__init__(**args)
        self._tipo = 'Electro'

class Car(object):
    """Example car."""
    def __init__(self, engine):
        """Initializer."""
        self._engine = engine  # Engine is injected

    def setEngine(self, engine):
        self._engine = engine

    def __str__(self):
        return "Engine: -> {}".format(self._engine)

class Taller(object):
    """docstring for Taller"""
    def __init__(self, **args):
        self._autos = args.get('carros', {})
        self._nombre = args.get('nombre', 'El Sin Nombre')

    def agregarCarro(self, carro):
        self._autos[len(self._autos) + 1] = carro

    def listaCarros(self):
        return self._autos

    def __str__(self):
        return "Taller: {}\nAutos: {}".format(self._nombre, [str(key) + " # " + str(value) for key, value in self._autos.items()])

porche = Car(GasolineEngine(potencia=558))

taller = Taller(nombre='Los Mofles')
print(taller)

taller.agregarCarro(porche)
print(taller)

porche.setEngine(ElectroEngine(potencia=300))
print(taller)

# https://github.com/ets-labs/python-dependency-injector
