
class ICharacterComponent():
    def equip(self):
        pass


class CharacterConcreteComponent(ICharacterComponent):
    def __init__(self,name):
        self.name=name
        self.equipamento=[]

    def equip(self):
        if len(self.equipamento)==0:
            return f'{self.name} equipment: Empty'
        else:
            return f'{self.name} equipment:{"".join(self.equipamento)}'


class ArmorConcreteDecorator(CharacterConcreteComponent):
    def __init__(self, character:CharacterConcreteComponent):
        self.character=character
        self.name=character.name
        self.equipamento=character.equipamento
        self.equipamento.append('\nArmor: Yes')
    
    def equip(self):
        return self.character.equip()
        

class SwordConcreteDecorator(CharacterConcreteComponent):
    def __init__(self, character:CharacterConcreteComponent):
        self.character=character
        self.name=character.name
        self.equipamento=character.equipamento
        self.equipamento.append('\nSword: Yes')

    def equip(self):
        return self.character.equip()

class HelmetConcreteDecorator(CharacterConcreteComponent):
    def __init__(self, character:CharacterConcreteComponent):
        self.character=character
        self.name=character.name
        self.equipamento=character.equipamento
        self.equipamento.append('\nHelmet: Yes')

    def equip(self):
        return self.character.equip()

class BootsConcreteDecorator(CharacterConcreteComponent):
    def __init__(self, character:CharacterConcreteComponent):
        self.character=character
        self.name=character.name
        self.equipamento=character.equipamento
        self.equipamento.append('\nBoots: Yes')

    def equip(self):
        return self.character.equip()