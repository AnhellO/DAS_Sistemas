from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Rectangulo(Figura):
    def _init_(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class CalculadorArea:
    def _init_(self, figuras):
        assert isinstance(figuras, list)
        self.figuras = figuras

    def suma_areas(self):
        total = 0
        for figura in self.figuras:
            total += figura.calcular_area()
        return total

# ¿Que sucederia si quisieramos sumar las areas de otros tipos de figuras?
# Se tendría que hacer una clase para esa figura, que herede de la clase 'Figura'.
# y la misma tendría que implementar el metodo 'calcular_area(self)' que devuelva un valor numerico.

# ¿Que tendriamos que hacer para poder sumar volumenes ademas de areas?
# Crearíamos una interfaz 'Cuerpo' o 'Figura3d', que contenga un metodo 'calcular_volumen(self)'.
# y se tendrían que crear clases que hereden de ella

if __name__ == '_main_':
    r = Rectangulo(3, 4)
    r2 = Rectangulo(5, 6)
    r3 = Rectangulo(2, 3.5)
    calc = CalculadorArea([r, r2, r3])
    print(calc.suma_areas())