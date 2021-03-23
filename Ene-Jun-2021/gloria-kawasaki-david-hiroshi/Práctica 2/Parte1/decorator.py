class CharacterConcreteComponent:
    def __init__(self, name):
        self.name = name
    
    def equipment(self, object):
        return f"{self.name} equipment:{object}"
    
    def equip(self, equipment=" Empty"):
        return self.equipment(equipment)

class ArmorConcreteDecorator:
    def __init__(self, character):
        self.character = character

    def equip(self, equipment=""):
        return self.character.equip("\nArmor: Yes"+equipment)
    
class SwordConcreteDecorator:
    def __init__(self, character):
        self.character = character

    def equip(self, equipment=""):
        return self.character.equip("\nSword: Yes"+equipment)