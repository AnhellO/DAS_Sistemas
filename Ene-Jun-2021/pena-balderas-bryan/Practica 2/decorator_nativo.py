class CharacterConcreteComponent():
    def __init__(self,name):
        self.name=name
        self.inentario=''

    def equipamento(self,func,equipado='Empty'):
        def equipo():
            self.inentario=self.inentario+equipado
            return func+self.inentario
        
        return equipo

    @equipamento
    def equip(self):
        return f'{self.name} equipment: '

class ArmorConcreteDecorator(CharacterConcreteComponent):
    def __init__(self, name):
        self.name=name
        self.equipamento('\nArmor: Yes')

    def equip(self):
        return super().equip()

class SwordConcreteDecorator(CharacterConcreteComponent):
    def __init__(self, name):
        self.name=name
        self.equipamento('\nSword: Yes')

    def equip(self):
        return super().equip()