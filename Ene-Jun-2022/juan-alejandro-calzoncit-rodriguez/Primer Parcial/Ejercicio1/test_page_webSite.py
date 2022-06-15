from page import Page
from webSite import WebSite
import unittest

'''
Suite de prubas unitarias para las clases : 
        Page    &   WebSite 
'''

class TestClases(unittest.TestCase):
    def test_crear_pagina(self):
        page = Page()
        page.setUrl('www.themeforest.net')    
        page.setHipervinculos('<a href="https://themeforest.net/category/wordpress?sort=date">Hipervinculo</a>')
        page.setTitulo('<h1>Forest</h1>')
        page.setContenido('<p>Contenido de la página.</p')
        page.setFormato('HTML')

        self.assertIsInstance(page, Page)        
        self.assertEqual(page.url, 'www.themeforest.net')
        self.assertEqual(page.hipervinculos, '<a href="https://themeforest.net/category/wordpress?sort=date">Hipervinculo</a>')
        self.assertEqual(page.titulo , '<h1>Forest</h1>')
        self.assertEqual(page.contenido , '<p>Contenido de la página.</p')
        self.assertEqual(page.formato , 'HTML')

    def test_crear_webSite(self):
        wb = WebSite()
        wb.setDominio('amazon')
        wb.setSubdominio('www')
        wb.setExtension('.com')
        wb.setDescripcion('Shopping')
        wb.setHosting('Hosting El Mariachi')
        wb.setAdaptadoMoviles(True)

        page = Page()
        page.setUrl('www.themeforest.net')    
        page.setHipervinculos('<a href="https://themeforest.net/category/wordpress?sort=date">Hipervinculo</a>')
        page.setTitulo('<h1>Forest</h1>')
        page.setContenido('<p>Contenido de la página.</p')
        page.setFormato('HTML')

        page2 = Page()
        page2.setUrl('https://refactoring.guru/')
        page2.setFolder('datos')
        page2.setHipervinculos('<a href="https://refactoring.guru/es/design-patterns/builder">Hipervinculo</a>')
        page2.setTitulo('<h1>Forest</h1>')
        page2.setFormato('HTML')

        page3 = Page()
        page3.setUrl('https://www.youtube.com/')
        page3.setFolder('proyecto')        
        page3.setTitulo('<h1>YouTube</h1>')  

        wb.setPaginas([page,page2])

        self.assertIsInstance(wb , WebSite)
        self.assertEqual(wb.dominio, 'amazon')
        self.assertEqual(wb.subdominio , 'www')
        self.assertEqual(wb.extension , '.com')
        self.assertEqual(wb.descripcion , 'Shopping')
        self.assertEqual(wb.hosting , 'Hosting El Mariachi')
        self.assertEqual(wb.adaptadoMoviles , True)
        self.assertEqual(wb.paginas , [page, page2])
        self.assertEqual(wb.buscador(page), "Encontrado")
        self.assertEqual(wb.buscador(page2), "Encontrado")
        self.assertEqual(wb.buscador(page3), "No encontrado")


if __name__ == '__main__':
    unittest.main()