class CharacterConcreteComponent():
    def __init__(self,name):
        self.name = name
        self.inventario=''

    def equipamento(self,func,equipado='Empty'):
        def equipo():
            self.inventario = self.inventario+equipado
            return func + self.inventario

        return equipo

    @equipamento
    def equip(self):
        return f'{self.name} equipment: '

class ArmorConcreteDecorator(CharacterConcreteComponent):
    def __init__(self, name):
        self.name = name
        self.equipamento('\nArmor: Yes')

    def equip(self):
        return super().equip()

class SwordConcreteDecorator(CharacterConcreteComponent):
    def __init__(self, name):
        self.name = name
        self.equipamento('\nSword: Yes')

    def equip(self):
        return super().equip()


       