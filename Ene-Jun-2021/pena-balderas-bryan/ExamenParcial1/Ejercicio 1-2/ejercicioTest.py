import unittest

from ejercicioUnoDos import *


class DecoratorTest(unittest.TestCase):
    def test_principal(self):
        paginasLista=[]
        paginaw=PaginaWeb("www.pagina.com","/pagina.html","html","<html><body><p>hola</p></body></html>","Pagina","Pagina",["ciencia","tecnologia"])
        paginasLista.append(paginaw)
        sitio=SitioWeb("pagina","tecnologia",paginasLista)
        buscador=BuscadorConcreteDecorator(sitio)
        self.assertEqual(buscador.buscar(paginaw),"Pagina Existe")

    def test_no_existe(self):
        paginasLista=[]
        paginat=PaginaWeb("www.pagina.com","/pagina.html","html","<html><body><p>hola</p></body></html>","Pagina","Pagina",["ciencia","tecnologia"])
        paginasLista.append(paginat)
        sitiof=SitioWeb("pagina","tecnologia",paginasLista)
        buscador=BuscadorConcreteDecorator(sitiof)
        paginados=PaginaWeb("www.paginados.com","/paginados.html","html","<html><body><p>hola dos</p></body></html>","Paginados","Paginados",["ciencia","tecnologia"])
        self.assertEqual(buscador.buscar(paginados),"No Existe")


if __name__=="__main__":
    unittest.main()