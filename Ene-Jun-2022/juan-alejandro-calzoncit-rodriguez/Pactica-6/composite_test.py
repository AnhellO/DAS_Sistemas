from composite import *
from unittest import mock
import unittest

class CompositeTest(unittest.TestCase):
    def test_crear_composite(self):
        raiz = ArchivoComposite('/')
        self.assertIsInstance(raiz,ArchivoComposite)

    def test_crear_leaf(self):
        ejemplo1 = ArchivoLeaf('ejemplo1.py')
        self.assertIsInstance(ejemplo1,ArchivoLeaf)
    
    def test_imprime_estructura_simple(self):
        raiz = ArchivoComposite('/')
        ejemplo1 = ArchivoLeaf('ejemplo1.py')

        salidaEsperada = "Nombre : '/' , Tipo : 'Directorio'"                        

        with mock.patch('sys.stdout') as fake_stdout:
            raiz.imprimeEstructura()
        fake_stdout.assert_has_calls([mock.call.write(salidaEsperada), 
        mock.call.write('\n')])

        salidaEsperada = "Nombre : 'ejemplo1.py' , Tipo : 'Archivo'"                        
        with mock.patch('sys.stdout') as fake_stdout:
            ejemplo1.imprimeEstructura()
        fake_stdout.assert_has_calls([mock.call.write(salidaEsperada), 
                                    mock.call.write('\n')])

        raiz.add(ejemplo1)                                
        salidaEsperada = ["Nombre : '/' , Tipo : 'Directorio'",
        "Nombre : 'ejemplo1.py' , Tipo : 'Archivo'"]        
        with mock.patch('sys.stdout') as fake_stdout:
            raiz.imprimeEstructura()
        fake_stdout.assert_has_calls([mock.call.write(salidaEsperada[0]), 
        mock.call.write('\n'),mock.call.write(salidaEsperada[1]),mock.call.write('\n')])

    def test_imprime_estructura_noTanSimple(self):
        raiz = ArchivoComposite('/')
        etc = ArchivoComposite('/etc')
        bin = ArchivoComposite('/bin')
        home = ArchivoComposite('/home')
        users = ArchivoComposite('/users')
        juan = ArchivoComposite('/juan')
        ejemplo1 = ArchivoLeaf('ejemplo1.py')

        raiz.add(etc)
        raiz.add(bin)
        raiz.add(home)

        home.add(users)
        users.add(juan)
        juan.add(ejemplo1)                                

        salidaEsperada = ["Nombre : '/' , Tipo : 'Directorio'",
        "Nombre : '/etc' , Tipo : 'Directorio'",
        "Nombre : '/bin' , Tipo : 'Directorio'",
        "Nombre : '/home' , Tipo : 'Directorio'",
        "Nombre : '/users' , Tipo : 'Directorio'",
        "Nombre : '/juan' , Tipo : 'Directorio'",
        "Nombre : 'ejemplo1.py' , Tipo : 'Archivo'"]        
        with mock.patch('sys.stdout') as fake_stdout:
            raiz.imprimeEstructura()
        fake_stdout.assert_has_calls([mock.call.write(salidaEsperada[0]), 
        mock.call.write('\n'),mock.call.write(salidaEsperada[1]),
        mock.call.write('\n'),mock.call.write(salidaEsperada[2]),
        mock.call.write('\n'),mock.call.write(salidaEsperada[3]),
        mock.call.write('\n'),mock.call.write(salidaEsperada[4]),
        mock.call.write('\n'),mock.call.write(salidaEsperada[5]),
        mock.call.write('\n'),mock.call.write(salidaEsperada[6]),
        mock.call.write('\n')])

if __name__ == '__main__':
    unittest.main()