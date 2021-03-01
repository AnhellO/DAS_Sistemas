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

    def test_character_with_staff(self):
        character = CharacterConcreteComponent(name='Luxor')
        staff = StaffConcreteDecorator(character)
        self.assertEqual(
            staff.equip(),
            "Luxor equipment:\nStaff: Yes"
        )
    def test_character_with_medallion(self):
        character = CharacterConcreteComponent(name='Luxor')
        medallion = MedallionConcreteDecorator(character)
        self.assertEqual(
            medallion.equip(),
            "Luxor equipment:\nMedallion: Yes"
        )
    
    def test_character_with_armor_sword_staff_and_medallion(self):
        character = CharacterConcreteComponent(name='Luxor')
        armor = ArmorConcreteDecorator(character)
        sword = SwordConcreteDecorator(armor)
        staff = StaffConcreteDecorator(sword)
        medallion = MedallionConcreteDecorator(staff)

        self.assertEqual(
            medallion.equip(),
            "Luxor equipment:\nArmor: Yes\nSword: Yes\nStaff: Yes\nMedallion: Yes"
        )

if __name__ == "__main__":
    unittest.main()