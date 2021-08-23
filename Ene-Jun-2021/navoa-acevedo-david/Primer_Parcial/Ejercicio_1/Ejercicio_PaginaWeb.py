from slugify import slugify
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup
from os.path import splitext
import requests

class PaginaWeb:

    #El constructor de nuestra pagina, solo recibe url para hacer mas facil el manejo
    def __init__(self, url):
        self.url = url
        self.ruta = self.get_ruta()
        self.formato = self.get_formato()
        self.contenido = self.get_content()
        self.titulo = self.get_titulo()
        self.slug = self.get_slug()
        self.meta_tags = self.get_meta

    #Los metodos para conseguir los atributos basados en la url
    #Cada metodo asigna el valor pedido a cada atributo de la pagina

    #get_meta hace uso de los modulos beautifulSoup para conseguir todos los meta_tags y guardarlos en una lista
    def get_meta(self):
        soup = BeautifulSoup(urlopen(self.url), "lxml-xml")
        tag_list = []
        for tag in soup.find_all("meta"):
            if tag.get("property", None) == "og:title":
                tag_list.append(tag.get("content", None))
            elif tag.get("property", None) == "og:url":
                tag_list.append(tag.get("content", None))
        self.meta_tags = tag_list
        return self.meta_tags

    #Set del meta
    def set_meta(self, meta_nuevo):
        self.meta_tags = meta_nuevo
    
    #get_ruta solo usa el metodo urlparse para conseguir la url y con path nos trae solo la ruta
    def get_ruta(self):
        self.ruta = urlparse(self.url).path
        return self.ruta

    #Set de la ruta
    def set_ruta(self, ruta_nueva):
        self.ruta = ruta_nueva

    #get_titulo hace uso de beautifulSoup para conseguir el titulo de la url que se nos da
    def get_titulo(self):
        soup = BeautifulSoup(urlopen(self.url), "lxml-xml")
        self.titulo = soup.title.get_text()
        return self.titulo

    #Set del titulo
    def set_titulo(self, titulo_nuevo):
        self.titulo = titulo_nuevo

    #Este get_slug nos transforma el titulo de la pagina a slug
    def get_slug(self):
        self.slug = slugify(self.titulo)
        return self.slug

    #Set del slug
    def set_slug(self, slug_nuevo):
        self.slug = slug_nuevo

    #get_content nos trae el type de contenido en la url. Aun falta la comprobacion del
    #contenido con el formato de pagina.
    def get_content(self):
        response = requests.get(self.url)
        content_type = response.headers['content-type']
        self.contenido = content_type
        return self.contenido

    #Set del contenido
    def set_content(self, content_nuevo):
        self.contenido = content_nuevo

    #get_formato nos trae el path de la pagina, despues el splitext nos separa en el url y nos quedamos con el
    #path unicamente que esta en la posicion [1]
    def get_formato(self):
        path = urlparse(self.url).path
        formato = splitext(path)[1]
        self.ruta = formato
        return self.ruta

    #Set del formato
    def set_formato(self, formato_nuevo):
        self.formato = formato_nuevo

    def __str__(self):
        return f'La url del sitio es {self.url}\n La ruta es {self.ruta}\n El formato es {self.formato}\n El contenido es {self.contenido}\n El titulo es {self.titulo}\n El nombre en slug es {self.slug}\n Las metatag son {self.meta_tags}\n'
    
    def __repr__(self):
        return 'url: {}\n ruta: {}\n formato: {}\n contenido: {}\n titulo: {} slug: {}\n meta_tags: {}'.format(self.url, self.ruta, self.formato, self.contenido, self.titulo, self.slug, self.meta_tags)
