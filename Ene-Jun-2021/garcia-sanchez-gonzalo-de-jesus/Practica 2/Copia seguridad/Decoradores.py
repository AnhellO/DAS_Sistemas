import abc

# Componente
class Component(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def equip(self):
        pass
    
# Concrete Component
class CharacterConcreteComponent(Component):
    def __init__(self, name: str):
        self._name = name 
    def equip(self):
        return f"{self._name} equipment:"
# Decorator
class BaseDecorator(Component, metaclass=abc.ABCMeta):
    def __init__(self, Base_component: Component):
        self._Base_component = Base_component

    @abc.abstractmethod
    def equip(self):
        pass

# Concrete Decorator Armor
class ArmorConcreteDecorator(BaseDecorator):
    def equip(self):
        return f"{self._Base_component.equip()}\nArmor: Yes"

# Concrete Decorator Sword
class SwordConcreteDecorator(BaseDecorator):
    def equip(self):
        return f"{self._Base_component.equip()}\nSword: Yes"

# Concrete Decorator Sword And Armor
class SwordandArmorConcreteDecorator(BaseDecorator):
    def equip(self):
        return f"{self._Base_component.equip()} \nArmor: Yes\nSword: Yes"

# Concrete Decorator Ring
class RingConcreteDecorator(BaseDecorator):
    def equip(self):
        return f"{self._Base_component.equip()}\nRing: Yes"

# Concrete Decorator Shield
class ShieldConcreteDecorator(BaseDecorator):
    def equip(self):
        return f"{self._Base_component.equip()}\nShield: Yes"

# Concrete Decorator Ring And Shied
class RingAndShieldConcreteDecorator(BaseDecorator):
    def equip(self):
        return f"{self._Base_component.equip()} \nRing: Yes\nShield: Yes"

# Concrete Decorator All
class AllConcreteDecorator(BaseDecorator):
    def equip(self):
        return f"{self._Base_component.equip()} \nArmor: Yes\nSword: Yes\nRing: Yes\nShield: Yes"


def main():
    # Empty
    print(CharacterConcreteComponent("Luxor").equip())
    # Armor
    print(ArmorConcreteDecorator(CharacterConcreteComponent('Luxor')).equip())
    # Sword
    print(SwordConcreteDecorator(CharacterConcreteComponent('Luxor')).equip())
    # Sword and Armor
    print(SwordandArmorConcreteDecorator(CharacterConcreteComponent('Luxor')).equip())
    # Ring
    print(RingConcreteDecorator(CharacterConcreteComponent('Luxor')).equip())
    # Shield
    print(ShieldConcreteDecorator(CharacterConcreteComponent('Luxor')).equip())
    # Ring and Shield
    print(RingAndShieldConcreteDecorator(CharacterConcreteComponent('Luxor')).equip())
    #All
    print(AllConcreteDecorator(CharacterConcreteComponent('Luxor')).equip())
    
if __name__ == "__main__":
    main()