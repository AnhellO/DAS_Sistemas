class FactoryInterface:
    def add_part(self, part: str):
        raise NotImplementedError()

class GenericFactory(FactoryInterface):
    def add_part(self, part: str):
        parts = {
            'llantas': GenericTires(),
            'manillar': GenericHandlebar()
        }
        
        if part in parts.keys():
            return parts[part]
        
        return None

class MountainFactory(FactoryInterface):
    def add_part(self, part: str):
        parts = {
            'llantas': RuggedTires(),
            'manillar': HardHandlebar()
        }
        
        if part in parts.keys():
            return parts[part]
        
        return None

class RoadFactory(FactoryInterface):
    def add_part(self, part: str):
        parts = {
            'llantas': RoadTires(),
            'manillar': SportHandlebar()
        }
        
        if part in parts.keys():
            return parts[part]
        
        return None

class GenericTires:
    def part_type(self):
        return 'llantas genéricas'

class RuggedTires:
    def part_type(self):
        return 'llantas 4x4'

class RoadTires:
    def part_type(self):
        return 'llantas para carretera'

class GenericHandlebar:
    def part_type(self):
        return 'manillar genérico'

class HardHandlebar:
    def part_type(self):
        return 'manillar rígido'

class SportHandlebar:
    def part_type(self):
        return 'manillar deportivo'

class Bicycle:
    def __init__(self, factory: FactoryInterface = GenericFactory):
        self.type = self.get_type()
        self.llantas = factory().add_part('llantas')
        self.manillar = factory().add_part('manillar')
    
    def get_type(self):
        return f"Bicicleta"