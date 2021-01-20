import unittest

from Composite import Component, Child, Component

class TestComposite(unittest.TestCase):
    def setUp(self):
        pass

    def test_top(self):
        esperado = top
        actual = top
        self.assertEqual(actual, esperado)

if __name__ == "__main__":
    unittest.main(