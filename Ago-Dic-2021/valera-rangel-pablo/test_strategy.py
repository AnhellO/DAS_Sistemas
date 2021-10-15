import unittest
from strategy import *


class tests(unittest.TestCase):
    def testPassDirecto(self):
        context = playContext(10, 1, 43)
        self.assertEqual(context.play_context(), 'Jugando por aire')

    def testPassMandandoloALlamar(self):
        context = playContext(12, 4, 40)
        passPlay = passPlayStrategy()
        context.set_strategy(passPlay)
        self.assertEqual(context.play_context(), 'Jugando por aire')

    def testRushDirecto(self):
        context = playContext(2, 3, 52)
        self.assertEqual(context.play_context(), 'Jugando por tierra')

    def testRush(self):
        context = playContext(12, 4, 90)
        rushPlay = rushPlayStrategy()
        context.set_strategy(rushPlay)
        self.assertEqual(context.play_context(), 'Jugando por tierra')

    def testFieldGoalDirecto(self):
        context = playContext(15, 4, 78)
        self.assertEqual(context.play_context(), 'Intento de gol de campo')

    def testFieldGoalMandandoloALlamar(self):
        context = playContext(4, 20, 43)
        fieldGoalAttempt = fieldGoalPlayStrategy()
        context.set_strategy(fieldGoalAttempt)
        self.assertEqual(context.play_context(), 'Intento de gol de campo')

    def testPuntDirecto(self):
        context = playContext(15, 4, 10)
        self.assertEqual(context.play_context(), 'Intento de Despeje')

    def testPuntMandandoloALlamar(self):
        context = playContext(10, 1, 43)
        puntAttempt = puntPlayStrategy()
        context.set_strategy(puntAttempt)
        self.assertEqual(context.play_context(), 'Intento de Despeje')


if __name__ == '__main__':
    unittest.main()
