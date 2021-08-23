import abc

# Component
class Component(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def equip(self):
        pass
    
# Concrete Component
class CharacterConcreteComponent(Component):
    def __init__(self, **args) -> None:
        self._name = args.get('name', 'X')

    def equip(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f"{self._name} equipment: Empty"

# Base Decorator
class BaseDecorator(Component):
    def __init__(self, component: Component):
        self._component = component

    def equip(self):
        return self._component.equip()

# Concrete Decorator A
class ArmorConcreteDecorator(BaseDecorator):
    def equip(self):
        return f"{super().equip().replace(' Empty', '')}\nArmor: Yes"

# Concrete Decorator B
class SwordConcreteDecorator(BaseDecorator):
    def equip(self):
        return f"{super().equip().replace(' Empty', '')}\nSword: Yes"

# Concrete Decorator C
class ShieldConcreteDecorator(BaseDecorator):
    def equip(self):
        return f"{super().equip().replace(' Empty', '')}\nShield: Yes"

# Concrete Decorator D
class RingConcreteDecorator(BaseDecorator):
    def equip(self):
        return f"{super().equip().replace(' Empty', '')}\nRing: Yes"