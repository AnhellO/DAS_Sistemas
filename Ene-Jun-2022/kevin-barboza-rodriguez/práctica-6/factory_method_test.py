import unittest
from factory_method import *

class dialog_test(unittest.TestCase):
     def test_crear_dialog(self):
        boton = WindowsDialog()
        self.assertIsInstance(boton, Dialog)
        html = HtmlDialog()
        self.assertIsInstance(html, Dialog)

class crear_boton_test(unittest.TestCase):

    def test_crear_boton(self):
        boton = WindowsDialog()
        window = Windows()

        self.assertEqual(boton.render(),window.render())
        self.assertEqual(boton.createButton(),window.onClick())

        boton = HtmlDialog()
        html = Html()

        self.assertAlmostEqual(boton.render(),html.render())
        self.assertAlmostEqual(boton.createButton(),html.onClick())


if __name__=="__main__":
    unittest.main()