import math

# Implementa el patrón de diseño Factory Method tomando como referencia
# el ejercicio anterior, de tal manera que podamos crear múltiples
# instancias/figuras dentro de la misma función main, pero ahora utilizando
# la factoría.
# Re-utiliza todo tu código existente, pero dentro de un nuevo archivo
#Crea al menos 5 nuevas instancias de diferente tipo, pero por medio del Factory

class Figura(object):
    """Clase Figura"""
    def area(self):
        pass

class Circulo(Figura):
    """Clase Circulo que hereda de la clase Figura"""
    def __init__(self, radio):  # Constructor
        self.radio = radio

    def area(self):  # Calcular el área de un círculo
        return math.pi * (self.radio ** 2)

    def __str__(self):  # Mostrar área del círculo
        return "Área círculo: {}".format(self.area())

class Triangulo(Figura):
    """Clase Triangulo que hereda de la clase Figura"""
    def __init__(self, base, altura):  # constructor
        self.base = base
        self.altura = altura

    def area(self):  # calcular el área de un triángulo
        return (self.base * self.altura) / 2

    def __str__(self):  # Mostrar área del triángulo
        return "Área triángulo: {}".format(self.area())

class Rectangulo(Figura):
    """Clase Rectangulo que hereda de la clase Figura"""
    def __init__(self, base, altura):  # Constructor
        self.base = base
        self.altura = altura

    def area(self):  # calcular el área de un rectángulo
        return self.base * self.altura

    def __str__(self):  # Mostrar el área de un rectángulo
        return "Área rectángulo: {}".format(self.area())

class Rombo(Figura):
    """Clase Rombo que hereda de la clase Figura"""
    def __init__(self, diagonal_menor, diagonal_mayor):  # Constructor
        self.diagonal_menor = diagonal_menor
        self.diagonal_mayor = diagonal_mayor

    def area(self):  # calcular el área de un rombo
        return (self.diagonal_menor * self.diagonal_mayor) / 2

    def __str__(self):  # Mostrar el área de un rombo
        return "Área rombo: {}".format(self.area())

class Trapecio(Figura):
    """Clase Trapecio que hereda de la clase Figura"""
    def __init__(self, base_mayor, base_menor, altura ):  # Constructor
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura

    def area(self):  # calcular el área de un trapecio
        return self.altura * ((self.base_mayor + self.base_menor) / 2)

    def __str__(self):  # Mostrar el área de un trapecio
        return "Área trapecio: {}".format(self.area())

class Factory(object):
    # función que recibe como parámetro el nombre de la figura
    def getShape(self, shape):
        if shape == 'circulo':
            radio = 3
            return Circulo(radio) # Primer instancia
        if shape == 'triangulo':
            base = 3
            altura = 4
            return Triangulo(base, altura) # Segunda instancia
        if shape == 'rectangulo':
            base = 3
            altura = 4
            return Rectangulo(base, altura) # Tercera instancia
        if shape == 'trapecio':
            base_m = 3
            base_M = 4
            altura = 2
            return Trapecio(base_M, base_m, altura) # Cuarta instancia
        if shape == 'rombo':
            diagonal_m = 3
            diagonal_M = 3
            return Rombo(diagonal_m, diagonal_M) # Quinta instancia :D

def main():
    # Imprimimos áreas de las figuras
    shapes = Factory()
    print(shapes.getShape("circulo"))
    print(shapes.getShape("triangulo"))
    print(shapes.getShape("rectangulo"))
    print(shapes.getShape("trapecio"))
    print(shapes.getShape("rombo"))

if __name__ == '__main__':
    main()
