import abc

# Interface
class Component(metaclass=abc.ABCMeta):

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def equip(self) -> str:
        pass

# Concrete Component
class CharacterConcreteComponent(Component):
    def equip(self) -> str:
        return "Luxor equipment: Empty"


# Clase Decorator
class Decorator(Component):

    _wrapper: Component = None

    def __init__(self, component: Component) -> None:
        self._wrapper = component

    c = _wrapper

    def BaseDecorator(self, c: Component) -> str:
        return self._wrapper

    def equip(self) -> str:
        return self._wrapper.equip()


class ArmorConcreteDecorator(Decorator):
    def __init__(self, dec: Decorator):
        self._dec = dec

    def equip(self):
        message = self._dec.equip()    
        return f"{message.replace(' Empty', '')}\nArmor: Yes"


class SwordConcreteDecorator(Decorator):
    def __init__(self, dec: Decorator):
        self._dec = dec

    def equip(self):
        message = self._dec.equip()    
        return f"{message.replace(' Empty', '')}\nSword: Yes"

class ShieldConcreteDecorator(Decorator):
    def __init__(self, dec: Decorator):
        self._dec = dec

    def equip(self):
        message = self._dec.equip()    
        return f"{message.replace(' Empty', '')}\nShield: Yes"



class PowerUpsConcreteDecorator(Decorator):
    def __init__(self, dec: Decorator):
        self._dec = dec

    def equip(self):
        message = self._dec.equip()    
        return f"{message.replace(' Empty', '')}\nPower-ups: Yes"

if __name__ == "__main__":
    concrete_component = CharacterConcreteComponent('Luxor')
    #print(concrete_component.equip())
    concrete_decorator_a = ArmorConcreteDecorator(concrete_component)
    #print(concrete_decorator_a.equip())
    concrete_decorator_b = SwordConcreteDecorator(concrete_decorator_a)
    #print(concrete_decorator_b.equip())
    concrete_decorator_c = ShieldConcreteDecorator(concrete_decorator_b)
    concrete_decorator_d =PowerUpsConcreteDecorator(concrete_decorator_c)
    concrete_decorator_d.equip()
    #print(concrete_decorator_d.equip())
