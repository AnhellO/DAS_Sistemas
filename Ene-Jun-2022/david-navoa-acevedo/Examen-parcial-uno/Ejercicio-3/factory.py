from abc import ABC,abstractclassmethod
#Interface creadora
class Creador(ABC):
    @abstractclassmethod
    def getPolygon(self):
        pass
    #metodo para que haga algo segun refactoryGuru(En este caso solo imprime el objeto)
    def do_something(self):
        product = self.getPolygon()
        result = f"{product.getType()}"
        return result
#Clase PolygonFactory que implementa la interfaz Creador, esta clase solo se encarga de crear productos
class PolygonFactory(Creador):

    def __init__(self, product):
        self.product = product
    
    def getPolygon(self):
        return self.product
#Interfaz Polygon
class Polygon(ABC):
    @abstractclassmethod
    def getType(self):
        pass
#Clase Triangle la cual implementa la interfaz Polygon, esta clase regresa un String el cual explica
#Porque es un poligono
class Triangle(Polygon):
    def getType(self):
        return "El triangulo es un poligono con 3 lados"
#Clase Square que implementa la interfaz Polygon, esta clase regresa un string explicando porque
#es un poligono
class Square(Polygon):
    def getType(self):
        return "El cuadrado es un poligono con 4 lados"
#Clase Pentagon que implementa la interfaz Polygon, esta clase retorna un String que explica porque es un poligono
class Pentagon(Polygon):
    def getType(self):
        return "El pentagono es un poligono con 5 lados"
#Clase Cliente, este cliente recibe un creador como parametro y contiene el metodo main
#el cual devuelve el string que contiene el objeto creado
class Cliente:
    def __init__(self, creador: Creador):
        self.creador = creador

    def main(self) -> str:
        return f"{self.creador.do_something()}"


if __name__ == "__main__":
    #creacion de triangulo
    triangle = Cliente(PolygonFactory(Triangle()))
    #creacion de cuadrado
    cuadrado = Cliente(PolygonFactory(Square()))
    #creacion de pentagono
    pentagono = Cliente(PolygonFactory(Pentagon()))
    print(triangle.main())
    print(cuadrado.main())
    print(pentagono.main())


