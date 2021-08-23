from PaginaWeb import PaginaWeb #importamos la clase PaginaWeb

#clase SitioWeb
class SitioWeb(PaginaWeb):
    def __init__(self, dominio, cate, paginas: list):
        self.dominio = dominio
        self.cate = cate
        self.paginas = paginas

#funciones getters y setters
    def set_dominio(self, dominio):
        self.dominio = dominio
    def get_dominio(self):
        return self.dominio
    def set_cate(self, cate):
        self.cate = cate
    def get_cate(self):
        return self.cate
#agrega paginas
    def add_paginas(self, PaginaWeb):
        self.paginas.append(PaginaWeb)
    def get_paginas(self):
        return self.paginas

    #search pages
    def buscador(self, pagina=''):
        if pagina in self.paginas:
            print('** PAGINA ENCONTRADA! **')
            print(pagina)
        else:
            print('Pagina no encontrada!')


#main
Pagina1 = PaginaWeb(url='https://www.youtube.com/', ruta='FreeTime', link='https://www.youtube.com/', formato='html', contenido='', titulo='Youtube', metaT='meta name: description\ncontent: Disfruta de los vídeos y la música que te gustan, sube material original y comparte el contenido con tus amigos, tu familia y el resto del mundo en YouTube. Vídeo, compartir, teléfono con cámara, teléfono con vídeo, gratis, subida')
Pagina2 = PaginaWeb(url= 'https://www.rottentomatoes.com', ruta='Series', link='https://www.rottentomatoes.com/tv/wandavision', formato='html', contenido='Marvel Studios presents "WandaVision," a blend of classic television and the Marvel Cinematic Universe in which Wanda Maximoff (Elizabeth Olsen) and Vision (Paul Bettany) -- two super-powered beings living idealized suburban lives -- begin to suspect that everything is not as it seems.', titulo='WandaVision', metaT='meta name: description\nContent: Marvel Studios Presents ** WANDAVISION **')    

paginas = [Pagina1, Pagina2]
sitio = SitioWeb('.net', 'developers.', paginas)

print('==========================')
sitio.buscador(Pagina1)