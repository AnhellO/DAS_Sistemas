class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura


class CalculadorArea:

    def __init__(self, figuras):
        assert isinstance(figuras, list), "`shapes` should be of type `list`."
        self.figuras = figuras

    def suma_areas(self):
        total = 0
        
        for figura in self.figuras:
            total += figura.base * figura.altura

        return total

r = Rectangulo(3, 4)
calc = CalculadorArea([r])
print(calc.suma_areas())