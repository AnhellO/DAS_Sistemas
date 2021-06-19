class CharacterComponent:
    def __init__(self, name):
        self.name=name
    def equip(self):
        pass

class CharacterConcreteComponent(CharacterComponent):
    def equip(self):
        return f'{self.name} equipment:'

class Decorator(CharacterComponent):
    _character: CharacterComponent
    def __init__(self, _character:CharacterComponent):
        self._character=_character
    def equip(self):
        return self._character.equip()

class ArmorConcreteDecorator(Decorator):
    def equip(self):
        return f'{self._character.equip()}\nArmor: Yes'

class SwordConcreteDecorator(Decorator):
    def equip(self):
        return f'{self._character.equip()}\nSword: Yes'

class RingConcreteDecorator(Decorator):
    def equip(self):
        return f'{self._character.equip()}\nRing: Yes'

class NecklaceConcreteDecorator(Decorator):
    def equip(self):
        return f'{self._character.equip()}\nNecklace: Yes'