import abc

#Clase page para crear paginas nuevas
class page:
#Constructor
    def __init__(self, url = None, folder = None, path = None, link = None, hypervinculo= None, content = None, title = None, meta = None, format = None, image = None):
        self.__folder = folder
        self.__url = url
        self.__path = path
        self.__link = link
        self.__hypervinculo = hypervinculo
        self.__contet = content
        self.__title = title
        self.__meta = meta
        self.__format = format
        self.__image = image

#Setters
    def set_url(self, url):
        self.__url= url
    def set_folder(self, folder):
        self.__folder = folder
    def set_path(self, path):
        self.__path = path
    def set_link(self, link):
        self.__link = link
    def set_hypervinculo(self, hypervinculo):
        self.__hypervinculo = hypervinculo
    def set_content(self, content):
        self.__contet = content
    def set_title(self, title):
        self.__title = title
    def set_meta(self, meta):
        self.__meta = meta
    def set_format(self, format):
        self.__format = format
    def set_image(self, image):
        self.__image = image

#getters
    def get_url(self):
        return self.__url
    def get_folder(self):
        return self.__folder
    def get_path(self):
        return self.__path
    def get_link(self):
        return self.__link
    def get_hypervinculo(self):
        return self.__hypervinculo
    def get_content(self):
        return self.__contet
    def get_title(self):
        return self.__title
    def get_meta(self):
        return self.__meta
    def get_format(self):
        return self.__format
    def get_image(self):
        return self.__image
    #metodo toString
    def __str__(self) -> str:
        return " url: {url}\n folder: {folder}\n path: {path}\n link: {link}\n hypervinculo: {hv}\n content: {content}\n title: {title}\n meta: {meta}\n format: {format}\n {image}\n".format(url = self.__url, folder = self.__folder, path = self.__path, link = self.__link, hv = self.__hypervinculo, content = self.__contet, 
        title = self.__title, meta = self.__meta, format = self.__format, image = self.__image)

#Clase website 
class website(page):
    #constructor
    def __init__(self, dominio = None, subdominio = None, paginas = None, dns = None, direccion_ip = None, nombre = None, puerto = None, dueño = None, dir_correo = None, creador = None):
        self.__dominio = dominio
        self.__subdominio = subdominio
        self.__paginas = paginas
        self.__dns = dns
        self.__direccion_ip = direccion_ip
        self.__nombre = nombre
        self.__puerto = puerto
        self.__dueño = dueño
        self.__dir_correo = dir_correo
        self.__creador = creador

    #metodo para agregar nuevas paginas al sitio web ya existente
    def new_page(self, page: page):
        list_page = list(self.__paginas)
        list_page.append(page)
        self.__paginas = list_page

    #getters en caso de que sea necesario
    def get_dominio(self):
        return self.__dominio
    def get_subdominio(self):
        return self.__subdominio
    def get_paginas(self):
        return self.__paginas
    def get_dns(self):
        return self.__dns
    def get_direccion_ip(self):
        return self.__direccion_ip
    def get_nombre(self):
        return self.__nombre
    def get_puerto(self):
        return self.__puerto
    def get_dueño(self):
        return self.__dueño
    def get_dir_correo(self):
        return self.__dir_correo
    def get_creador(self):
        return self.__creador

    #setters 
    def set_dominio(self, dominio):
        self.__dominio = dominio
    def set_subdominio(self, subdominio):
        self.__subdominio = subdominio
    def set_paginas(self, paginas: list):
        self.__paginas = paginas
    def set_dns(self, dns):
        self.__dns = dns
    def set_direcc_ip(self, direccion_ip):
        self.__direccion_ip = direccion_ip
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_puerto(self, puerto):
        self.__puerto = puerto
    def set_dueño(self, dueño):
        self.__dueño = dueño
    def set_dir_correo(self, dir_correo):
        self.__dir_correo = dir_correo
    def set_creador(self, creador):
        self.__creador = creador

    def __str__(self) -> str:
        a = " dominio: {dominio}\n subdominio: {subdominio}\n dns: {dns}\n direccionIP: {dir_ip}\n nombre: {nombre}\n puerto: {puerto}\n dueño: {dueño}\n direccion de correo: {dir_correo}\n creador: {creador}\n PAGINAS: \n".format(dominio = self.__dominio,
         subdominio = self.__subdominio, dns = self.__dns, dir_ip = self.__direccion_ip, nombre = self.__nombre, puerto = self.__puerto, dueño = self.__dueño, dir_correo = self.__dir_correo, creador = self.__creador)
        b = "\n".join(map(str,list(self.__paginas)))
        return a+b

#interfaz en caso de que sean necesarias mas herramientas para el sitio web
class herramienta_website(metaclass = abc.ABCMeta):
    
    def __init__(self, website: website, page: page):
        self.website = website
        self.page = page

    @abc.abstractclassmethod
    def funcionalidad(self):
        pass

#herramienta para buscar la pagina dentro de las paginas del sitio web proporcionado
class herramienta_buscadora(herramienta_website):
    def funcionalidad(self): 
        if self.page in self.website.get_paginas():
            return True
        else:
            return False

if __name__ == "__main__":
    #pruebas burdas de funcionamiento
    potato = page("www.potato.com", "test1", "pedro/juan/potato.html", "rayas", "esteCosoJala", "dkjsaljdsalkjdksla", "Pagina para patatas", "title Tag", "HTML5", "imagen de patata")
    print(potato)
    paginaVacia = page("", "", "", "", "", "", "", "", "", "")
    potatosParaPotatos = website("goDaddy", "goDaddy2", (potato, paginaVacia), "123456", "1324252432", "potatosParaTodos", "80:80")
    potatosParaPotatos.new_page(paginaVacia)
    print(potatosParaPotatos)
    herramienta = herramienta_buscadora(potatosParaPotatos, potato)
    print(herramienta.funcionalidad())