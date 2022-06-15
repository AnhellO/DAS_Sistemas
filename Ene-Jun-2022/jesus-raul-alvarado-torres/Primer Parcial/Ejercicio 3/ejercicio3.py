from abc import ABC, abstractmethod

# Se crea una 'interface' ue representa un polígono.
class Polygon(ABC):
    @abstractmethod
    def get_type(self) -> str:
        pass

# Triangle, Square y Pentagon implementan la interface Polygon.
class Triangle(Polygon):
    def get_type(self) -> str:
        return 'I am a triangle!'

class Square(Polygon):
    def get_type(self) -> str:
        return 'I am a square!'

class Pentagon(Polygon):
    def get_type(self) -> str:
        return 'I am a pentagon!'

# Creator es una interface que da lineamientos a seguir para crear 
# diferentes 'Creators'.
class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Polygon:
        pass

    def get_type(self) -> str:

        polygon = self.factory_method()

        return polygon.get_type()

# Aquí se crean los 'creators' correspondientes a los polígonos
# siguiendo los lineamientos de la interface Creator.
class TraingleCreator(Creator):
    def factory_method(self) -> Polygon:
        return Triangle()

class SquareCreator(Creator):
    def factory_method(self) -> Polygon:
        return Square()

class PentagonCreator(Creator):
    def factory_method(self) -> Polygon:
        return Pentagon()
    
    def get_type(self) -> str:
        return super().get_type()

# Función director para simplificar los tests unitarios.
def director(text: str) -> str:
    if text == 'triangle':
        return TraingleCreator().get_type()
    elif text == 'square':
        return SquareCreator().get_type()
    elif text == 'pentagon':
        return PentagonCreator().get_type()
