#Para comenzar como se menciona en la descripcion del ejercicio ambos tine los mismo lados tanto un cuadrado como un rectangulo,
#pero existe un problema en el momento de representarlos en el codigo(abstraccion) ya que al momento de hablar de numero de lados si son iguales, pero al
#momento de representar sus lados surgen conflictos nos esperados ya que la cantidad de lados es igual mas no la medida, y el principio de Liskov nos dice que la clase principal puede ser
#sustituida por una clase derivada sin que ocurra algo un comportamiendo no deseado
#Una solucion seria el crear clases diferentes ya que tiene somportamientos diferentes

class Rectangulo(object):
    def set_altura(self, altura):
        self.altura = altura
        return self
    def set_base(self, base):
        self.base = base
        return self
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return self.base + self.base + self.altura + self.altura
#se agrega una clase cuadrado la cual ahora si sus metodos son mas adecuados a los de un cuadrado
class Cuadro(object):
    def set_Lado(self,lado):
        self.lado = lado
        return self
    def area(self):
        return self.lado * self.lado
    def perimetro(self):
        return self.lado * 4


class circulo(object):
    def set_radio(self,radio):
        self.radio = radio
        def area(self):
            return math.pi*self.radio**
        def perimetro(self):
            return math.pi*2*self.radio


class GeneradorGraficos(object):
    def __init__(self, rectangulo = None):
        self.rectangulo = rectangulo
        self.cuadro=cuadro
        self.circulo=circulo
    def set_rectangulo(self, rectangulo):
        self.rectangulo = rectangulo
        return self
    def dibujar_rectangulo(self):
        return self.rectangulo.area()
    def dibujar_perimetroRect(self):
        return self.rectangulo.perimetro()
    def set_cuadro(self,cuadro):
        self.cuadro=cuadro
    def dibujar_cuadro(self):
        return self.cuadro.area()
    def dibujar_perimetroCuad(self):
        return self.cuadro.perimetro()
    def dibujar_circulo(self):
        return self.circulo.area()
    def dibujar_perimetroCuad(self):
        return self.circulo.perimetro()

if __name__ == '__main__':

    rectangulo = Rectangulo()
    rectangulo.set_altura(4).set_base(2)
    cuadrado = Rectangulo()
    try:
    cuadrado.set_altura(5).set_base(5)
    generador_de_graficos = GeneradorGraficos(rectangulo)
    except:
        pass:
    print(generador_de_graficos.dibujar_rectangulo())

    print(generador_de_graficos.dibujar_rectangulo())

    #Para el caso del circulo de igual manera se implemento otra clase que tengas metodos con mas coerencia con respecto a un circulo
