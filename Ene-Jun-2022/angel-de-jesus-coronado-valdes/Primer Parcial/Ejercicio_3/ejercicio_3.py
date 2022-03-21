from abc import ABC, abstractmethod

# tenemos nuestra interfas polygonfactory
class PolygonFactory(ABC):
    
    # nuestro metodo abtracto
    @abstractmethod
    def polygon_method():
        pass
    
    #metodo get que nos retorna la infromacion de las figuras
    def getPolygon(self):     
        product = self.polygon_method()
        return f"The Information is: {product.getType()}"


# creamos nuestra clase CreatePolygon que hereda de la interfas PolygonFactor
#el metodo polygon_method
#concrete
class CreatePolygon(PolygonFactory):
    #contructor que resive el producto de las diferentes clases de figuras
    def __init__(self,product) -> None:
        self.product = product
    
    # retornamos del metodo abtracto heredado de la interfas polygonfactor
    # se retorna lo que retorne del producto selecionado
    def polygon_method(self):
        return self.product



# interfas Polygon de las figuras
class Polygon(ABC):
    # metodo abtracto de obtener el typo de figura
    @abstractmethod
    def getType(self) -> str:
        pass

# clases de las figuras 
class Triangle(Polygon):
    # retorna un string el metodo getType heredado de la interface abtracta de Polygon
    def getType(self) -> str:
        return "The Triangle has 3 side"

class Square(Polygon):
    # retorna un string el metodo getType heredado de la interface abtracta de Polygon
    def getType(self) -> str:
        return "The Square has 4 side"

class Pentagon(Polygon):
    # retorna un string el metodo getType heredado de la interface abtracta de Polygon
    def getType(self) -> str:
        return "The Pentagon has 5 side"


class Client:
    def __init__(self,creator: PolygonFactory) -> None:
        self.creator = creator
    # funcion cliente _code resive el concrete "CreatePoLygon" y a su ves resivira la figura
    def client_code(self) -> str:
        return f"{self.creator.getPolygon()}" # nos retornara el string de la figura seleccionada


def main():
    #instanciamos la funcion client_code client
    #resive el concrete "CreatePlygon"
    # y as us ves ingresamos la clase de la figura que seleccionemos para retornar un string
    #con la información de la figura
    triangle = Client(CreatePolygon(Triangle()))
    triangle = triangle.client_code()
    print(triangle)
    print()
    square = Client(CreatePolygon(Square()))
    square = square.client_code()
    print(square)
    print()
    pentagon = Client(CreatePolygon(Pentagon()))
    pentagon = pentagon.client_code()
    print(pentagon)


if __name__ == "__main__":
    main()