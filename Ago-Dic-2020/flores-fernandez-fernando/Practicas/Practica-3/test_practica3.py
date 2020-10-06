import Practica3
import unittest

class TestPractica3(unittest.TestCase):
    def test_turn_on(self):
        on = Practica3.TurnedOn().change_state()
        self.assertEqual(on,"ON")   

    def test_turn_off(self):
        off = Practica3.TurnedOff().change_state()
        self.assertEqual(off,"OFF")   

    def test_get_state(self):
        state = Practica3.RadioStation().get_state()
        self.assertEqual(state,None)   

    def test_set_state(self):
        radio = Practica3.RadioStation()
        on = Practica3.TurnedOn()
        radio.set_state(on)
        radio.change_state()
        state = radio.get_state()
        self.assertEqual(state,"ON")   

if __name__ == "__main__":
     unittest.main()
