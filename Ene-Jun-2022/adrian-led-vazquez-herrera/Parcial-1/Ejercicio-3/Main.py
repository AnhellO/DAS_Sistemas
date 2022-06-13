#DAS 8vo semestre
#Parcial 1, E: 3 Factory Method
#Main

import pytest
from Factory import PolygonFactory

#   Para evitar repetirnos creamos el objeto de la clase factory
# como un objeto global
factory=PolygonFactory

def test_Triangle():
    #Revisamos que el polígono si sea un triángulo
    shape=factory.create_polygon("Triangle")
    assert shape.getType()=="Triangle"
    
def test_Square():
    #Revisamos que el polígono si sea un cuadrado
    shape=factory.create_polygon("Square")
    assert shape.getType()=="Square"
    
def test_Pentagon():
    #Revisamos que el polígono si sea un pentágono
    shape=factory.create_polygon("Pentagon")
    assert shape.getType()=="Pentagon"
    
def test_Circle():
    #Revisamos que el polígono no exista
    shape=factory.create_polygon("Circle")
    assert shape=="Polygon not found"

if __name__ == "__main__":
    
    test_Triangle()
    test_Square()
    test_Pentagon()
    test_Circle()
