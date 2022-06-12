import unittest
import worker

class TestWorker(unittest.TestCase):
    def test_work(self):
        casos = [
            ("Despierta, Almuerza, Va a trabajar, Apaga incendio, Regresa a casa, Se relaja, Se duerme.",worker.FireFighter()),
            ("Despierta, Almuerza, Va a trabajar, Corta leña, Regresa a casa, Se relaja, Se duerme.",worker.Lumberjack()),
            ("Despierta, Almuerza, Va a trabajar, Papeleo, Regresa a casa, Se relaja, Se duerme.",worker.Manager())
        ]
        for esperado, entrada in casos:
            with self.subTest(esperado = esperado, entrada = entrada):
                obtenido = worker.client_code(entrada)
                self.assertEqual(esperado, obtenido)

if __name__ == "__main__":
    unittest.main()