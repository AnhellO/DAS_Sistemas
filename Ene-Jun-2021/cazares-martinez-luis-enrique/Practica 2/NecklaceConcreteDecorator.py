from CharacterConcreteComponent import CharacterConcreteComponent


class NecklaceConcreteDecorator(CharacterConcreteComponent):

    def equip(self):
        return f'{self.name} equipment:\nNeckLace: Yes'
