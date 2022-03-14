import unittest
from unittest import mock
from factory_method import *

class FactoryMethodTest(unittest.TestCase):
    def test_WindowDialog(self):
        ob = WindowsDialog()        
        
        self.assertIsInstance(ob.createButton(),WindowsButton)
        self.assertIsInstance(ob.createButton(),Button)
        salidaEsperada = ["Vincula un evento clic de OS nativo",
        "Representa un botón en estilo Windows"]        
        with mock.patch('sys.stdout') as fake_stdout:
            ob.render()
        fake_stdout.assert_has_calls([mock.call.write(salidaEsperada[0]), 
        mock.call.write('\n'),mock.call.write(salidaEsperada[1]),mock.call.write('\n')])

    def test_WebDialog(self):
        ob = WebDialog()        
        
        self.assertIsInstance(ob.createButton(),HTMLButton)
        self.assertIsInstance(ob.createButton(),Button)
        salidaEsperada = ["Vincula un evento clic de navegador web",
        "Representa un botón en HTML"]        
        with mock.patch('sys.stdout') as fake_stdout:
            ob.render()
        fake_stdout.assert_has_calls([mock.call.write(salidaEsperada[0]), 
        mock.call.write('\n'),mock.call.write(salidaEsperada[1]),mock.call.write('\n')])

    def test_Application(self):
        ob = Application()        
        
        salidaEsperada = ["Vincula un evento clic de OS nativo",
        "Representa un botón en estilo Windows"]        
        with mock.patch('sys.stdout') as fake_stdout:
            ob.main('Windows') 
        fake_stdout.assert_has_calls([mock.call.write(salidaEsperada[0]), 
        mock.call.write('\n'),mock.call.write(salidaEsperada[1]),mock.call.write('\n')])

        ob = Application()

        salidaEsperada = ["Vincula un evento clic de navegador web",
        "Representa un botón en HTML"]        
        with mock.patch('sys.stdout') as fake_stdout:
            ob.main('Web') 
        fake_stdout.assert_has_calls([mock.call.write(salidaEsperada[0]), 
        mock.call.write('\n'),mock.call.write(salidaEsperada[1]),mock.call.write('\n')])


if __name__ == '__main__':
    unittest.main()
