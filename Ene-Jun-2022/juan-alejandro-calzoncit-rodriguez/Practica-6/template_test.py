import unittest
from unittest import mock
from template import *

class TestTemplate(unittest.TestCase):

    def test_create_concret_class(self):
        obj = FireFighter()
        self.assertIsInstance(obj,FireFighter)

        obj = Lumberjack()
        self.assertIsInstance(obj,Lumberjack)

        obj = Postman()
        self.assertIsInstance(obj,Postman)

        obj = Manager()
        self.assertIsInstance(obj,Manager)

    def test_FireFighter(self):
        obj = FireFighter()        

        salidaEsperada = ['Despertando','Comiendo el desayuno','Yendo al trabajo',
        'Soy un bombero','Regresando del trabajo','Momento chill','Mimir']
        with mock.patch('sys.stdout') as fake_stdout:
            obj.DailyToutine()
        fake_stdout.assert_has_calls([mock.call.write(salidaEsperada[0]), 
        mock.call.write('\n'),mock.call.write(salidaEsperada[1]),mock.call.write('\n'),
        mock.call.write(salidaEsperada[2]),mock.call.write('\n'),
        mock.call.write(salidaEsperada[3]),mock.call.write('\n'),
        mock.call.write(salidaEsperada[4]),mock.call.write('\n'),
        mock.call.write(salidaEsperada[5]),mock.call.write('\n'),
        mock.call.write(salidaEsperada[6]),mock.call.write('\n')])

    def test_Lumberjack(self):
        obj = Lumberjack()

        salidaEsperada = ['Despertando','Comiendo el desayuno','Yendo al trabajo',
        'Soy un leñador','Regresando del trabajo','Momento chill','Mimir']
        with mock.patch('sys.stdout') as fake_stdout:
            obj.DailyToutine()
        fake_stdout.assert_has_calls([mock.call.write(salidaEsperada[0]), 
        mock.call.write('\n'),mock.call.write(salidaEsperada[1]),mock.call.write('\n'),
        mock.call.write(salidaEsperada[2]),mock.call.write('\n'),
        mock.call.write(salidaEsperada[3]),mock.call.write('\n'),
        mock.call.write(salidaEsperada[4]),mock.call.write('\n'),
        mock.call.write(salidaEsperada[5]),mock.call.write('\n'),
        mock.call.write(salidaEsperada[6]),mock.call.write('\n')])

    def test_Postman(self):
        obj = Postman()

        salidaEsperada = ['Despertando','Comiendo el desayuno','Yendo al trabajo',
        'Soy un cartero','Regresando del trabajo','Momento chill','Mimir']
        with mock.patch('sys.stdout') as fake_stdout:
            obj.DailyToutine()
        fake_stdout.assert_has_calls([mock.call.write(salidaEsperada[0]), 
        mock.call.write('\n'),mock.call.write(salidaEsperada[1]),mock.call.write('\n'),
        mock.call.write(salidaEsperada[2]),mock.call.write('\n'),
        mock.call.write(salidaEsperada[3]),mock.call.write('\n'),
        mock.call.write(salidaEsperada[4]),mock.call.write('\n'),
        mock.call.write(salidaEsperada[5]),mock.call.write('\n'),
        mock.call.write(salidaEsperada[6]),mock.call.write('\n')])

    def test_Manager(self):
        obj = Manager()

        salidaEsperada = ['Despertando','Comiendo el desayuno','Yendo al trabajo',
        'Soy un gerente','Regresando del trabajo','Viendo una serie','Mimir']
        with mock.patch('sys.stdout') as fake_stdout:
            obj.DailyToutine()
        fake_stdout.assert_has_calls([mock.call.write(salidaEsperada[0]), 
        mock.call.write('\n'),mock.call.write(salidaEsperada[1]),mock.call.write('\n'),
        mock.call.write(salidaEsperada[2]),mock.call.write('\n'),
        mock.call.write(salidaEsperada[3]),mock.call.write('\n'),
        mock.call.write(salidaEsperada[4]),mock.call.write('\n'),
        mock.call.write(salidaEsperada[5]),mock.call.write('\n'),
        mock.call.write(salidaEsperada[6]),mock.call.write('\n')])

if __name__ == '__main__':
    unittest.main()