class FactoryInterface:
    def add_tires(self):
        raise NotImplementedError()

    def add_handlebar(self):
        raise NotImplementedError()

class GenericFactory(FactoryInterface):
    def add_tires(self):
        return GenericTires()

    def add_handlebar(self):
        return GenericHandlebar()        

class MountainFactory(FactoryInterface):
    def add_tires(self):
        return RuggedTires()

    def add_handlebar(self):
        return HardHandlebar()        

class RoadFactory(FactoryInterface):
    def add_tires(self):
        return RoadTires()

    def add_handlebar(self):
        return SportHandlebar()        

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
        self.llantas = factory().add_tires()
        self.manillar = factory().add_handlebar()
    
    def get_type(self):
        return f"Bicicleta"