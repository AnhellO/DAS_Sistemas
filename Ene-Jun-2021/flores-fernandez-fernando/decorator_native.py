import abc

#inteface Component

class ICharacterComponent(metaclass=abc.ABCMeta):

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def equip(self):
        pass

# Concrete Component
class CharacterConcreteComponent(ICharacterComponent):
    def equip(self):
        return "Luxor equipment: Empty"


# Base Decorator
class CharacterDecorator(ICharacterComponent):
    def __init__(self, ICharacterComponent: ICharacterComponent):
        self._wrapper = ICharacterComponent
    _wrapper: ICharacterComponent = None
    w = _wrapper

    def BaseDecorator(self, w: ICharacterComponent):
        return self._wrapper

    def equip(self):
        return self._wrapper.equip()


class ArmorConcreteDecorator(CharacterDecorator):
    def __init__(self, decorator: CharacterDecorator):
        self._decorator = decorator

    def equip(self):  
        if ( " Empty" in self._decorator.equip()):
            return f"{self._decorator.equip()[0:-6]}\nArmor: Yes"
        return f"{self._decorator.equip()}\nArmor: Yes"


class SwordConcreteDecorator(CharacterDecorator):
    def __init__(self, decorator: CharacterDecorator):
        self._decorator = decorator

    def equip(self):
        if ( " Empty" in self._decorator.equip()):
            return f"{self._decorator.equip()[0:-6]}\nSword: Yes"
        return f"{self._decorator.equip()}\nSword: Yes"



def main():
    character = CharacterConcreteComponent(name = "Luxor")
    armor = ArmorConcreteDecorator(character)
    p = armor.equip()


    print(p)

if __name__ == "__main__":
    main()