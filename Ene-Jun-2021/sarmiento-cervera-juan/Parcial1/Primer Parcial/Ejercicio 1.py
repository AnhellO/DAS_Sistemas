class PaginaWeb:
    #Variable de la clase
    Page = 'Necesito aprender a programar pero me aburre'
    def _init_(self, URL, Ruta, Formato, Contenido, Titulo, Slug,Meta_tags):
        ##variables de instancia
        self.URL=URL
        self.Ruta=Ruta
        self.Formato = Formato
        self.Contenido = Contenido
        self.Titulo = Titulo
        self.Slug = Slug
        self.Meta_tags = Meta_tags    
    def Mostrar_URL(self):
        print(self.URL)
    def Muestra_Ruta(self):
        print(self.Ruta)
    def Muestra_Formato(self, Formato):
       print("El Formato e la paguina es: " + Formato)
    def Muestra_Contenido(self, Contenido):
        print("El contenido es: " + Contenido)
    def Muestra_Titulo(self, Titulo):
        print("El Titulo es: " + Titulo)
    def Muestra_Slug(self, Slug):
        print("El Titulo es: " + Slug)
    def Muestra_Meta_tags(self, Meta_tags):
        print("El Meta Tag es: " + Meta_tags)
    def Mostrar_Datos(self):
        print("URL: "+self.URL+"\nRuta: " +self.Ruta+"\nFormato: "+
        self.Formato+"\nContenido: "+self.Contenido+"\nTutulo: "+self.Titulo)    
    def __str_(self):
        print ( self.URL+" "+self.Ruta+" "+self.Formato+" "+self.Contenido+" "+self.Titulo+" "+self.Slug+" "+self.Meta_tags)

class SitioWeb(PaginaWeb):
    #Variable de la clase
    sitio = 'Muero de sueño'
    def _init_(self, Dominio, Categoria, Paginas):
    #Variables de instancia
        self.Dominio=Dominio
        self.Categoria=Categoria
        self.Paginas=Paginas    
    def Mostrar_Dominio(self):
        print(self.Dominio)
    def Mostrar_Categoria(self):
        print(self.Categoria)
    def Mostrar_Paginas(self):
        print(self.Paginas)

    def _str_(self):
       return self.Dominio + "\n" + self.Categoria + "\n" + str(self.Paginas)
   
mi_Pagina = PaginaWeb("www.twitch.tv/black994", 'img src = "Foto.jpg"', "HTML", "Juegos", "La Historia de los vodeojuegos", "slug", "Tags")        
mi_Sitio = SitioWeb("www.twitch.tv", 'Streaming', "Canales")      
print(mi_Sitio)
mi_Pagina.Mostrar_Datos()