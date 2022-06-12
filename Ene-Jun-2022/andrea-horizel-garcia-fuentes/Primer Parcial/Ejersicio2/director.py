class Director:
    def __init__(self):
        self.builder = None

    @property
    def builder(self):
        return self.builder

    @builder.setter
    def builder(self, builder):
        self.builder = builder

    def instagram_page(self):
        self.builder.set_titulo("Check")
        self.builder.add_texto("texto1").add_texto("texto2")
        self.builder.add_cuerpo("https://www.instagram.com")
        self.builder.add_links("link")
        self.builder.add_css("<style>")

    def menu_page(self):
        self.builder.set_titulo("menu")
        self.builder.add_texto("texto")
        self.builder.add_cuerpo("cuerpo de pagina")
        self.builder.add_imagenes("imagenes")
        self.builder.add_folder("carpeta")
        self.builder.add_links("http://www.JustinBieber.com")
        