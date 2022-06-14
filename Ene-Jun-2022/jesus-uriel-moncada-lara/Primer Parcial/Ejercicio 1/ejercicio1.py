from email.mime import base
from select import select


class page:
    def __init__(self, url , path, etiquetas, imagenes, hipervinculos, videos, api, base_datos, botones , formulario) -> None:
        self.url = url
        self.path = path
        self.etiquetas = etiquetas
        self.imagenes = imagenes
        self.hipervinculos = hipervinculos
        self.videos = videos
        self.api = api
        self.base_datos = base_datos
        self.botones = botones
        self.formulario = formulario

class website:
    def __init__(self, dominio, sub_dominio, url_wbst, hosting) -> None:
        self.dominio = dominio
        self.sub_dominio = sub_dominio
        self.url_wbst = url_wbst
        self.hosting = hosting

class buscador:
    def search(website,page):
        if website == page:
            print("pagina encontrada")
        else:
            print('pagina perdida')

def main():
    p = page('www.godad.mx','nadw','h1,h2','link => wwww.google/images.com','www.google.com','www.youtube.com','wwww.tuapi.com','encrypted','refec','True')
    w = website('https','wixx','www.godad.mx','dawdwa')
    buscar = buscador(p,w)

if __name__ == '__main__':
    main()