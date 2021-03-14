import unittest
from PagwebySitioweb import PaginaWeb as pw
from PagwebySitioweb import Website as ws

class TestClases(unittest.TestCase):
    def test_Just_One_Page(self):
        self.pagina = pw("www.youtube.com/AnimePlay","/youtube/canales/AnimePlay","HTML","<body>Hola, Bienvenido</body>","AnimePlay Videos","Anime-Play-Videos",('Anime','Videos','Youtube','Reproductor'))
        self.mettags = ('Anime','Videos','Youtube','Reproductor')
        self.tags = ",".join(self.mettags)
        self.r=f'url: www.youtube.com/AnimePlay'
        self.r+=f'\npath: /youtube/canales/AnimePlay'
        self.r+=f'\nformato: HTML'
        self.r+=f'\nconten: <body>Hola, Bienvenido</body>'
        self.r+=f'\ntitle: Anime Play Videos'
        self.r+=f'\nslug: Anime-Play-Videos'
        self.r+=f'\nmeta-tags: {self.tags}'
        self.assertEqual(str(self.pagina),self.r)
if __name__ == '__main__':
    unittest.main()