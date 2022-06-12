from page_builder import PageBuilder


class Page:
    def __init__(self, titulo, texto):
        self.titulo = titulo
        self.texto = texto
        self.cuerpo = []
        self.imagenes = []
        self.folders = []
        self.links = []
        self.cabezeras = []
        self.scripts = []
        self.css = []
        self.urls = []

    @property
    def titulo(self):
        return self.titulo

    @titulo.setter
    def titulo(self, value):
        self.titulo = value

    @property
    def texto(self):
        return self.texto

    @texto.setter
    def texto(self, value):
        self.texto = value

    @property
    def cuerpo(self):
        return self.cuerpo

    @cuerpo.setter
    def cuerpo(self, value):
        self.cuerpo = value

    @property
    def imagenes(self):
        return self.imagenes

    @imagenes.setter
    def imagenes(self, value):
        self.imagenes = value

    @property
    def folders(self):
        return self.folders

    @folders.setter
    def folders(self, value):
        self.folders = value

    @property
    def links(self):
        return self.links

    @links.setter
    def links(self, value):
        self.links = value

    @property
    def cabezeras(self):
        return self.cabezeras

    @cabezeras.setter
    def cabezeras(self, value):
        self.cabezeras = value

    @property
    def scripts(self):
        return self.scripts

    @scripts.setter
    def scripts(self, value):
        self.scripts = value

    @property
    def css(self):
        return self.css

    @css.setter
    def css(self, value):
        self.css = value

    @property
    def url(self):
        return self.urls

    @url.setter
    def url(self, value):
        self.urls = value

    def __str__(self):
        mensaje = "\n* titulo: " + self.titulo
        mensaje += "\n* texto: " + self.texto
        mensaje += "\n* cuerpo: " + self.cuerpo
        mensaje += "\n* URL: " + self.url
        mensaje += "\n* imagenes: " + self.imagenes
        mensaje += "\n* folder: " + self.folders
        mensaje += "\n* Links: " + self.links
        mensaje += "\n* cabezeras: " + self.cabezeras
        mensaje += "\n* scripts: " + self.scripts
        mensaje += "\n* css: " + self.css
        return mensaje


class ConcretePageBuilder(PageBuilder):
    def __init__(self, titulo, texto):
        self._page = Page(titulo, texto)

    def set_cuerpo(self, cuerpo):
        self._page.cuerpo = cuerpo
        return self

    def add_imagen(self, imagen):
        self._page.imagenes.append(imagen)
        return self

    def add_folder(self, folder):
        self._page.folders.append(folder)
        return self

    def add_link(self, link):
        self._page.links.append(link)
        return self

    def add_cabezera(self, cabezera):
        self._page.cabezeras.append(cabezera)
        return self

    def add_script(self, script):
        self._page.scripts.append(script)
        return self

    def add_CSS(self, css):
        self._page.css.append(css)
        return self

    def add_url(self, url):
        self._page.urls.append(url)
        return self

    def build(self):
        return self._page