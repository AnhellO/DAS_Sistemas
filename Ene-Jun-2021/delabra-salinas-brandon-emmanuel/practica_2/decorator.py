#PARTE 1
#INTERFACE
class Component():
    def equip(self):
        pass



class CharacterConcreteComponent(Component):
    def __init__(self,name):
        self.name = name
        self.equipamento = []
# ESTATUS DEL EQUIPO
    def equip(self):
        if len(self.equipamento) == 0:
            return f'{self.name} equipment: Empty'
        else:
            return f'{self.name} equipment:{"".join(self.equipamento)}'




class ArmorConcreteDecorator(CharacterConcreteComponent):
    def __init__(self, character:CharacterConcreteComponent):
        self.character = character
        self.name = character.name
        self.equipamento = character.equipamento
        self.equipamento.append('\n Armor: Yes')

    def equip(self):
        return self.character.equip()




class SwordConcreteDecorator(CharacterConcreteComponent):
    def __init__(self, character:CharacterConcreteComponent):
        self.character = character
        self.name = character.name
        self.equipamento = character.equipamento
        self.equipamento.append('\n Sword: Yes')

    def equip(self):
        return self.character.equip()



