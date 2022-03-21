class Page():
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

    def __str__(self):
        return (f"this page contains: {self.html}, {self.head}, {self.link}, {self.title}, {self.body}, {self.h1}, {self.h2}, {self.h3}, {self.p}, {self.button}, {self.xml}, {self.json}")


class Website():
    # solamente el dominio es obligatorio
    def __init__(self, dominio, subdominio="", contacto="", url="", tipo="", logotipo="", menu=""):
        self.dominio = dominio
        self.subdominio = subdominio
        self.contacto = contacto
        self.url = url
        self.tipo = tipo
        self.logotipo = logotipo
        self.menu = menu
        # coleccion de las paginas del sitioweb
        self.coleccion = []

        def __str__(self):
            return (f"this website contains: domain: {self.dominio}, subdomain: {self.subdominio}, contact_info: {self.contacto}, url: {self.url}, logo: {self.logotipo}, menu: {self.menu}")


def buscador(Website, Page):
    for i in range(len(Website.coleccion)):
        if Website.coleccion[i] == Page:
            return "this page is on this website"

def main():
    pagina = Page(html="<html>", head="<head>", link="<link>", title="<title>",
                  body="<body>", h1="<h1>", p="<p>", div="<div>", json="<script>")

    pagina_1 = Page(html="<html>", head="<head>", title="<title>",
                  body="<body>", h1="<h1>",h2="<h2>", p="<p>", div="<div>", xml="<?xml?>", json="<script>")

    sitio_web = Website("kevin code",subdominio="html",url="www.kevincode.com",contacto="kevin@gmail.com")
    sitio_web.coleccion.append(pagina)
    sitio_web.coleccion.append(pagina_1)

    print(buscador(sitio_web, pagina_1))

if __name__ == "__main__":
    main()
