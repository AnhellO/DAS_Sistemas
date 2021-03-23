import unittest

from decorator import *

class DecoratorTest(unittest.TestCase):
    def test_character_without_equipment(self):
        character = CharacterConcreteComponent(name='Luxor')
        self.assertEqual(
            character.equip(),
            "Luxor equipment: Empty"
        )

    def test_character_with_armor(self):
        character = CharacterConcreteComponent(name='Luxor')
        armor = ArmorConcreteDecorator(character)
        self.assertEqual(
            armor.equip(),
            "Luxor equipment:\nArmor: Yes"
        )

    def test_character_with_sword(self):
        character = CharacterConcreteComponent(name='Luxor')
        sword = SwordConcreteDecorator(character)
        self.assertEqual(
            sword.equip(),
            "Luxor equipment:\nSword: Yes"
        )
    
    def test_character_with_armor_and_sword(self):
        character = CharacterConcreteComponent(name='Luxor')
        armor = ArmorConcreteDecorator(character)
        sword = SwordConcreteDecorator(armor)
        self.assertEqual(
            sword.equip(),
            "Luxor equipment:\nArmor: Yes\nSword: Yes"
        )

    def test_character_with_armor_and_sword_and_shield(self):
        character = CharacterConcreteComponent(name='Luxor')
        armor = ArmorConcreteDecorator(character)
        sword = SwordConcreteDecorator(armor)
        shield = ShieldConcreteDecorator(sword)
        self.assertEqual(
            shield.equip(),
            "Luxor equipment:\nArmor: Yes\nSword: Yes\nShield: Yes"
        )
    
    def test_character_with_armor_and_sword_and_shield_and_powerups(self):
        character = CharacterConcreteComponent(name='Luxor')
        armor = ArmorConcreteDecorator(character)
        sword = SwordConcreteDecorator(armor)
        shield = ShieldConcreteDecorator(sword)
        power_ups= PowerUpsConcreteDecorator(shield)
        self.assertEqual(
            power_ups.equip(),
            "Luxor equipment:\nArmor: Yes\nSword: Yes\nShield: Yes\nPower-ups: Yes"
        )

if __name__ == "__main__":
    unittest.main()