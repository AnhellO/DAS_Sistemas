import unittest

from videogame_native import *

class VideoGameNativeTest(unittest.TestCase):
    def test_human_with_armor(self):
        @Armor
        def EquipWeapon():
            return Human().__str__()

        self.assertEqual("Selected human with armor", EquipWeapon())

    def test_human_with_sword(self):
        @Shield
        def EquipWeapon():
            return Human().__str__()

        self.assertEqual("Selected human with shield", EquipWeapon())

    def test_human_with_armor_sword(self):
        @ArmorSword
        def EquipWeapon():
            return Human().__str__()

        self.assertEqual("Selected human with armor and sword", EquipWeapon())

    def test_human_with_flamethrower(self):
        @Flamethrower
        def EquipWeapon():
            return Human().__str__()

        self.assertEqual("Selected human with flamethrower", EquipWeapon())

if __name__ == "__main__":
    unittest.main()