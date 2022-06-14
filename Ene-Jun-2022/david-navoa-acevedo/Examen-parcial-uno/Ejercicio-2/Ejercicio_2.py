import abc
from Ejercicio_1 import page, website

#builder de lo necesario, pagina o sitio web con 7 parametros, en mi caso creo me fuí un poco al extremo
#pero pues hice un builder general de parametros generales
class Builder(metaclass = abc.ABCMeta):

    @abc.abstractclassmethod
    def reset(self):
        pass
    @abc.abstractclassmethod
    def set_first_parameter(self):
        pass
    @abc.abstractclassmethod
    def set_second_parameter(self):
        pass
    @abc.abstractclassmethod
    def set_third_parameter(self):
        pass
    @abc.abstractclassmethod
    def set_forth_parameter(self):
        pass
    @abc.abstractclassmethod
    def set_five_parameter(self):
        pass
    @abc.abstractclassmethod
    def set_six_parameter(self):
        pass
    @abc.abstractclassmethod
    def set_seven_parameter(self):
        pass
    @abc.abstractclassmethod
    def set_eight_parameter(self):
        pass
    @abc.abstractclassmethod
    def set_nine_parameter(self):
        pass
    @abc.abstractclassmethod
    def set_then_parameter(self):
        pass
    @abc.abstractclassmethod
    def get_results(self):
        pass
#Constructor de paginas que recive un constructor
class PageBuilder(Builder):
    def __init__(self) -> None:
        self.page = page()

    def reset(self):
        self.page = page()

    def set_first_parameter(self, url):
        self.page.set_url(url)
    def set_second_parameter(self, folder):
        self.page.set_folder(folder)
    def set_third_parameter(self, path):
        self.page.set_path(path)
    def set_forth_parameter(self, link):
        self.page.set_link(link)
    def set_six_parameter(self, hypervinculo):
        self.page.set_hypervinculo(hypervinculo)
    def set_seven_parameter(self, content):
        self.page.set_content(content)
    def set_five_parameter(self, title):
        self.page.set_title(title)
    def set_eight_parameter(self, meta):
        self.page.set_meta(meta)
    def set_nine_parameter(self, format):
        self.page.set_format(format)
    def set_then_parameter(self, image):
        self.page.set_image(image)

    def get_results(self):
        return self.page

class WebsiteBuilder(Builder):
    def __init__(self):
        self.__website = website()

    def reset(self):
        self.__website = website()

    def set_first_parameter(self, dominio):
        self.__website.set_dominio(dominio)
    def set_second_parameter(self, paginas:list):
        self.__website.set_paginas(paginas)
    def set_third_parameter(self, dns):
        self.__website.set_dns(dns)
    def set_forth_parameter(self, direccion_ip):
        self.__website.set_direcc_ip(direccion_ip)
    def set_five_parameter(self, nombre):
        self.__website.set_nombre(nombre)
    def set_six_parameter(self, puerto):
        self.__website.set_puerto(puerto)
    def set_seven_parameter(self, subdominio):
        self.__website.set_subdominio(subdominio)
    def set_eight_parameter(self, dueño):
        self.__website.set_dueño(dueño)
    def set_nine_parameter(self, dir_correo):
        self.__website.set_dir_correo(dir_correo)
    def set_then_parameter(self, creador):
        self.__website.set_creador(creador)

    def get_results(self):
        return self.__website


class Director:

    def __init__(self, builder: Builder):
        self.__builder = builder

    def change_builder(self, builder: Builder):
        self.__builder = builder

    #metodo para crear pagina web sobre papás
    def webPage(self):
        self.__builder.set_first_parameter("www.potato.com")
        self.__builder.set_second_parameter("webpages")
        self.__builder.set_third_parameter("C:/Documentos/webpages/potato.html")
        self.__builder.set_forth_parameter("https://www.potato.com")
        self.__builder.set_five_parameter("PotatosForPotatos")
        self.__builder.set_six_parameter("PosZelda")
        self.__builder.set_seven_parameter("Aquí encontraras cosas referentes a papas como tu!")
        self.__builder.set_eight_parameter("<meta>Meta Description</meta>")
        self.__builder.set_nine_parameter("HTML5")
        self.__builder.set_then_parameter("imagen de una papa")
        return self.__builder.get_results()

    #metodo para crear sitio web con 2 paginas iguales
    def website(self):
        webpage_builder = PageBuilder()
        director = Director(webpage_builder)
        pages = (director.webPage(), director.webPage())
        self.__builder.set_first_parameter("goDaddy")
        self.__builder.set_second_parameter(pages)
        self.__builder.set_third_parameter("255.255.255.0")
        self.__builder.set_forth_parameter("123.123.126.732")
        self.__builder.set_five_parameter("OnlyPotatos")
        self.__builder.set_six_parameter("80:80")
        self.__builder.set_seven_parameter("goDaddy2")
        self.__builder.set_eight_parameter("David Potato Acevedo")
        self.__builder.set_nine_parameter("dante_david4@potato.com")
        self.__builder.set_then_parameter("David Navoa Acevedo")
        return self.__builder.get_results()

def main():
    webpage_builder = PageBuilder()
    website_builder = WebsiteBuilder()
    
    print("\nwebpage builder\n")
    director = Director(webpage_builder)
    print(director.webPage())
    director.change_builder(website_builder)
    print("\nWebsite builder\n")
    print(director.website())
    

if __name__ == "__main__":
    main()

    