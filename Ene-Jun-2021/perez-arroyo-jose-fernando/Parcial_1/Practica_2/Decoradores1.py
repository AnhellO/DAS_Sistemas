class componente:
    def equip(self):
        pass

class CharacterConcreteComponent(componente):
    def __init__(self, name: str):
        self.name = name 
    def equip1(self, x):
        return f"{self.name} equipment:{x}"
    def equip(self, equip1=" Empty"):
        return self.equip1(equip1)

class ArmorConcreteDecorator():
    def __init__(self, character):
        self.character = character
    def equip(self, equip1=''):
        return self.character.equip("\nArmor: Yes"+equip1)

class SwordConcreteDecorator():
    def __init__(self, character):
        self.character = character
    def equip(self, equip1=''):
        return self.character.equip("\nSword: Yes"+equip1)

class RingPowerConcreteDecorator():
    def __init__(self, character):
        self.character = character
    def equip(self, equip1=''):
        return self.character.equip("\nRing: Yes"+equip1)

class ShieldConcreteDecorator():
    def __init__(self, character):
        self.character = character
    def equip(self, equip1=''):
        return self.character.equip("\nShield: Yes"+equip1)

    
if __name__ == "__main__":
    main()