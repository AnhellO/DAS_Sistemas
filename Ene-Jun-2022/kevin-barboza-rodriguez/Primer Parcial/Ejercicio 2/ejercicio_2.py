from abc import ABC, abstractmethod
import gc
class Builder(ABC):

    @abstractmethod
    def buildStep():
        pass

class ConcretPage(Builder):
    # los atributos pra crear una pagina son opcionales
    def __init__(self, html="", head="", link="", title="", body="", h1="", h2="", h3="",
                 p="", div="", button="", xml="", json=""):

        self.html = html
        self.head = head
        self.link = link
        self.title = title
        self.body = body
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3
        self.p = p
        self.div = div
        self.button = button
        self.xml = xml
        self.json = json

    def buildStep(self):
        return f"this page contains: {self.html}, {self.head}, {self.link}, {self.title}, {self.body}, {self.h1}, {self.h2}, {self.h3}, {self.p}, {self.button}, {self.xml}, {self.json}"


class ConcreteWebsite(Builder):
    # solamente el dominio es obligatorio
    def __init__(self, dominio, subdominio="", contacto="", url="", tipo="", logotipo="", menu=""):

        self.dominio = dominio
        self.subdominio = subdominio
        self.contacto = contacto
        self.url = url
        self.tipo = tipo
        self.logotipo = logotipo
        self.menu = menu

    def buildStep(self):
        return f"this website contains: domain: {self.dominio}, subdomain: {self.subdominio}, contact_info: {self.contacto}, url: {self.url}, logo: {self.logotipo}, menu: {self.menu}"


class Director(Builder):

    
    #def make(self):
    def buildStep(self):
        
        web_site = ConcreteWebsite("kevin code",subdominio="html",url="www.kevincode.com",contacto="kevin@gmail.com")
        
        page = ConcretPage(html="<html>", head="<head>", link="<link>", title="<title>",
                  body="<body>", h1="<h1>", p="<p>", div="<div>", json="<script>")
        
        page_1 = ConcretPage(html="<html>", head="<head>", link="<link>",
                  body="<body>", h1="<h1>", p="<p>", div="<div>", xml="<?xml?>")
        #ahora no se necesita un atributo en la clase concreta web site ya que en la clase director se crea el sitio web
        #  y las paginas que contiene       
        print(web_site.buildStep())
        print(page.buildStep())
        print(page_1.buildStep())

def main():

    director = Director()
    director.buildStep()
    #borramos un director 
    del director
    

if __name__ == "__main__":
    main()
