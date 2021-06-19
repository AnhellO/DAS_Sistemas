import unittest
from paginaysitioweb import PaginaWeb,SitioWeb

class TestClases(unittest.TestCase):
    def test_SiteWeb(self):
        self.paginaA = PaginaWeb("www.facebook.com/LuFlores","/Facebook/Users/LuFlores","HTML","<body>Lu Flores</body>","Lu Flores Facebook","lu-flores-facebook",('red social','facebook'))
        self.paginaB = PaginaWeb("www.facebook.com/LuFlores","/Facebook/Users/LuFlores","HTML","<body>Lu Flores</body>","Lu Flores Facebook","lu-flores-facebook",('red social','facebook'))
        self.paginaC = PaginaWeb("www.facebook.com/LuFlores","/Facebook/Users/LuFlores","HTML","<body>Lu Flores</body>","Lu Flores Facebook","lu-flores-facebook",('red social','facebook'))
        self.paginaD = PaginaWeb("www.facebook.com/LuFlores","/Facebook/Users/LuFlores","HTML","<body>Lu Flores</body>","Lu Flores Facebook","lu-flores-facebook",('red social','facebook'))
        self.paginaE = PaginaWeb("www.facebook.com/LuFlores","/Facebook/Users/LuFlores","HTML","<body>Lu Flores</body>","Lu Flores Facebook","lu-flores-facebook",('red social','facebook'))
        self.paginaF = PaginaWeb("www.facebook.com/LuFlores","/Facebook/Users/LuFlores","HTML","<body>Lu Flores</body>","Lu Flores Facebook","lu-flores-facebook",('red social','facebook'))
        self.paginas=(self.paginaA,self.paginaB,self.paginaC,self.paginaD,self.paginaE,self.paginaF)
        self.sitio = SitioWeb("facebook.com","red social",self.paginas)
        self.resultado=f"dominio: facebook.com"
        self.resultado+=f"\ncategoria: red social"
        self.resultado+=f"\npaginas:\n"
        self.resultado+=f"\n"
        self.resultado+=f"{self.paginaA}\n"
        self.resultado+=f"\n"
        self.resultado+=f"{self.paginaB}\n"
        self.resultado+=f"\n"
        self.resultado+=f"{self.paginaC}\n"
        self.resultado+=f"\n"
        self.resultado+=f"{self.paginaD}\n"
        self.resultado+=f"\n"
        self.resultado+=f"{self.paginaE}\n"
        self.resultado+=f"\n"
        self.resultado+=f"{self.paginaF}\n"
        self.assertEqual(str(self.sitio),self.resultado)
if __name__ == '__main__':
    unittest.main()