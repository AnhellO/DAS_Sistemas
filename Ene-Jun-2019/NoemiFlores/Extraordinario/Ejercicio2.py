#Para utilizar el principio Open Closed haré tres clases...

#Esta primera clase sera de 'Figura', en la que tendrá un único método llamado 'area'
class Figura(object):
    def area(self):
        pass

#La segunda clase hereda y reimplementa el método 'area'
class Rectangulo(Figura):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

#Y la tercera clase será la que sume las áreas de las figuras geometricas
class CalculadorArea(Figura):

    def __init__(self, figuras):
        assert isinstance(figuras, list), "'shapes' should be of type 'list'."
        self.figuras = figuras

    def suma_areas(self):
        total = 0

        for figura in self.figuras:
            total += figura.base * figura.altura

        return total


r1 = Rectangulo(3, 4)
r2 = Rectangulo(7,4)
r3 = Rectangulo(2,3)
calc = CalculadorArea([r1,r2,r3])
print(calc.suma_areas())

#¿Qué sucedería si quisieramos sumar las áreas de otros tipos de figuras?
    #No se podría, ya que solo tenemos el tipo Rectangulo, si queremos sumar las areas de otras figuras
    #primero debemos agregar mas clases de las figuras que queremos.
#¿Qué tendríamos que hacer para poder sumar volúmenes además de áreas?
    #Hacer una funcion más en la clase Figura que sea de volumenes,
    #y una nueva función suma_volumenes en una nueva clase CalculadorVolumen