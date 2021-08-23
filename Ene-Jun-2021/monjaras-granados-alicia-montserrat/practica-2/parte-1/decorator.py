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

    def equip(self)-> str:
        message = self._dec.equip()    
        return f"{message.replace(' Empty', '')}\nArmor: Yes"


class SwordConcreteDecorator(Decorator):
    def __init__(self, dec: Decorator):
        self._dec = dec

    def equip(self)-> str:
        message = self._dec.equip()    
        return f"{message.replace(' Empty', '')}\nSword: Yes"



def main():
    concrete_component = CharacterConcreteComponent('Luxor')
    #print(concrete_component.equip())
    concrete_decorator_a = ArmorConcreteDecorator(concrete_component)
    #print(concrete_decorator_a.equip())
    concrete_decorator_b = SwordConcreteDecorator(concrete_decorator_a)
    concrete_decorator_b.equip()
    #print(concrete_decorator_b.equip())


if __name__ == "__main__":
    main()
