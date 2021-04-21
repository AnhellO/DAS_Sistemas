import abc

class Character(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def equip(self):
        pass

class CharacterConcreteComponent(Character):
    def __init__(self,name: str):
        self._name = name
        
    def equip(self):
        return f"{self._name} equipment:"

class CharacterDecorator(Character, metaclass=abc.ABCMeta):
    def __init__(self,character_component: Character):
        self._character_component = character_component

    @abc.abstractmethod
    def equip(self):
        pass

class ArmorConcreteDecorator(CharacterDecorator):
    def equip(self):
        return f"{self._character_component.equip()}\nArmor: Yes"

class SwordConcreteDecorator(CharacterDecorator):
    def equip(self):
        return f"{self._character_component.equip()}\nSword: Yes"

class RingConcreteDecorator(CharacterDecorator):
    def equip(self):
        return f"{self._character_component.equip()}\nRing: Yes"

class ShieldConcreteDecorator(CharacterDecorator):
    def equip(self):
        return f"{self._character_component.equip()}\nShield: Yes"

def main():
    print(CharacterConcreteComponent("Luxor").equip())
    print(ArmorConcreteDecorator(CharacterConcreteComponent("Luxor")).equip())
    print(SwordConcreteDecorator(CharacterConcreteComponent("Luxor")).equip())
    print(SwordConcreteDecorator(ArmorConcreteDecorator(CharacterConcreteComponent("Luxor"))).equip())

if __name__ == "__main__":
    main()


