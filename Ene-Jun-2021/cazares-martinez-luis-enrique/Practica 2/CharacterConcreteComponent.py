from character import Character


class CharacterConcreteComponent(Character):

    character = Character

    def __init__(self, name):
        self.name = name

    def equip(self):
        return f'{self.name} equipment: Empty'
