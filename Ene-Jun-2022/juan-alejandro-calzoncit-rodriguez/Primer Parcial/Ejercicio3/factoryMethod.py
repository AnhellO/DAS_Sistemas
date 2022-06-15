import abc
'''
Patron de diseño Factory Method para el diagra de UML del ejercicio 3
'''

# Interface de Producto
class Interface_Polygon(abc.ABC):
    @abc.abstractmethod
    def getType(self) -> str:
        pass

# Creador
class PolygonFactory:
    def getPolygon(self, polygon : Interface_Polygon):        
        return polygon.getType()
    
# Clase de producto concreto, implementa la interface
class Triangle(Interface_Polygon):
    # Sobrescribe el método de la interface, returna su 'Type'
    def getType(self) -> str:
        return "It's a triangle"

class Square(Interface_Polygon):
    def getType(self) -> str:
        return "It's a square"

class Pentagon(Interface_Polygon):
    def getType(self) -> str:
        return "It's a pentagon"

# Cliente
def main():
    polygonFactory= PolygonFactory()    # Objeto tipo Polygonfactory
    tri = Triangle()    # Objeto de un producto concreto
    print(polygonFactory.getPolygon(tri))
    # La clase trabaja con cualquier tipo de producto
    print(polygonFactory.getPolygon(Square()))
    print(polygonFactory.getPolygon(Pentagon()))

    '''
    It's a triangle
    It's a square
    It's a pentagon
    '''

if __name__ == '__main__':
    main()