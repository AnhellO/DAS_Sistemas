import unittest
import prototype

class TestPrototype(unittest.TestCase):
    def test_copiaOveja(self):
        casos = [
            (["Carmen","Dorper"],["Carmen","Dorper"]),
            (["Cruz","Merina"],["Cruz","Merina"])
        ]

        for esperado, entrada in casos:
            with self.subTest(esperado = esperado, entrada = entrada):
                oveja = prototype.Oveja(entrada[0],entrada[1])
                copia_oveja = prototype.copy.copy(oveja)
                obtenido = []
                obtenido.append(copia_oveja.get_nombre())
                obtenido.append(copia_oveja.get_tipo())
                self.assertEqual(esperado, obtenido)

if __name__ == "__main__":
    unittest.main()