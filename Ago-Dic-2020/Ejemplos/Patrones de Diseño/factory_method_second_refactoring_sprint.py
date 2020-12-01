class FactoryInterface:
    def add_part(self, part: str):
        parts = self._get_default_parts()
        
        if part in parts.keys():
            return parts[part]
        
        return None
    
    def _get_default_parts(self):
        raise NotImplementedError()

class GenericFactory(FactoryInterface):
    def _get_default_parts(self):
        return {
            'llantas': GenericTires(),
            'manillar': GenericHandlebar()
        }

class MountainFactory(FactoryInterface):
    def _get_default_parts(self):
        return {
            'llantas': RuggedTires(),
            'manillar': HardHandlebar()
        }

class RoadFactory(FactoryInterface):
    def _get_default_parts(self):
        return {
            'llantas': RoadTires(),
            'manillar': SportHandlebar()
        }

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
    
    def parts(self):
        return [self.llantas.part_type(), self.manillar.part_type()]