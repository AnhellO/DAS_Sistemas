import abc

class Character(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def show(self):
        pass

class Human(Character):
    def show(self):
        return "Selected human"

class Robot(Character):
    def show(self):
        return "Selected robot"

class CharacterDecorator(Character, metaclass=abc.ABCMeta):
    
    def __init__(self, decorated_character):
        self.decorated_character = decorated_character

    @abc.abstractmethod
    def show(self):
        self.decorated_character.show()

class EquipArmor(CharacterDecorator):
    def __init__(self, decorated_character: Character):
        super().__init__(decorated_character)

    def show(self):
        character = self.decorated_character.show()
        weapon = self.set_armor(self.decorated_character)

        return "{} with {}".format(character, weapon)

    def set_armor(self, decorated_character: Character):
        return "armor"

class EquipSword(CharacterDecorator):
    def __init__(self, decorated_character: Character):
        super().__init__(decorated_character)

    def show(self):
        character = self.decorated_character.show()
        weapon = self.set_sword(self.decorated_character)

        return "{} with {}".format(character, weapon)

    def set_sword(self, decorated_character: Character):
        return "sword"

class EquipArmorSword(CharacterDecorator):
    def __init__(self, decorated_character: Character):
        super().__init__(decorated_character)

    def show(self):
        character = self.decorated_character.show()
        weapon = self.set_armor(self.decorated_character)

        return "{} with {}".format(character, weapon)

    def set_armor(self, decorated_character: Character):
        return "armor and sword"

class EquipShield(CharacterDecorator):
    def __init__(self, decorated_character: Character):
        super().__init__(decorated_character)

    def show(self):
        character = self.decorated_character.show()
        weapon = self.set_shield(self.decorated_character)

        return "{} with {}".format(character, weapon)

    def set_shield(self, decorated_character: Character):
        return "shield"

class EquipFlamethrower(CharacterDecorator):
    def __init__(self, decorated_character: Character):
        super().__init__(decorated_character)

    def show(self):
        character = self.decorated_character.show()
        weapon = self.set_flamethrower(self.decorated_character)

        return "{} with {}".format(character, weapon)

    def set_flamethrower(self, decorated_character: Character):
        return "flamethrower"