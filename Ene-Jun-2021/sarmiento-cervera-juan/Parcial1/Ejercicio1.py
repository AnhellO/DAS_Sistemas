class PaginaWeb:
    Pagina = 'Necesito aprender a programar pero me aburre'

    def _init_(self, URL, Ruta, Formato, Contenido, Titulo, Slug,Meta_tags):
        ##variables de instancia
        self.URL='link'
        self.Ruta='img src = "Foto.jpg"'
        self.Formato = "HTML"
        self.Contenido = Contenido
        self.Titulo = 'Necesito aprender a programar :´('
        self.Slug = 'Slug'
        self.Meta_tags = 'Etiquetas'
        
    def Mostrar_URL(self, URL):
        self.URL = 'link' ## la URL del final de la paguina
        print("www.Facebook.com")
    
    def Ruta(self, Ruta):
        self.Ruta='img src = "Foto.jpg"'
        print("La ruta es: " + Ruta)

    def Formato(self, Formato):
        self.Formato='HTML'
        print("El Formato e la paguina es: " + Formato)

    def Contenido(self, Contenido):
        self.Contenido='img src = "Foto.jpg"'
        print("El contenido es: " + Contenido)

    def Titulo(self, Titulo):
        self.Titulo ='Necesito aprender a programar :´('
        print("El Titulo es: " + Titulo)

    def Slug(self, Slug):
        self.Slug ='Necesito aprender a programar :´('
        print("El Titulo es: " + Slug)

    def Meta_tags(self, Meta_tags):
        self.Meta_tags ='Etiquetas'
        print("El Meta Tag es: " + Meta_tags)



   
mi_pagina = PaginaWeb("www.Facebook.com", 'img src = "Foto.jpg"', "HTML", "Juegos", "La Historia de los vodeojuegos","slug","Tags")        
print(mi_pagina)