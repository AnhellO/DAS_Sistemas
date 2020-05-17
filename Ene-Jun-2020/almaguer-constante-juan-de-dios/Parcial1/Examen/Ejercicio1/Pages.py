# creación del objeto Page
class Page(object):
    def __init__(self, **args):
        self.url = args.get("url")
        self.titulo = args.get("titulo")
        self.met_des = args.get("met_des")
        self.formato = args.get("formato")

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_met_des(self):
        return self.met_des

    def set_met_des(self, met_des):
        self.met_des = met_des

    def get_formato(self):
        return self.formato

    def set_formato(self, formato):
        self.formato = formato

    def __str__(self):
        return f'URL: {self.url}\nTitulo: {self.titulo}\n ' \
               f'Meta-Descripción: {self.met_des}\n Formato: {self.formato}'


# Creacion del objeto WebPage
class WebPage(Page):
    def __init__(self, **args):
        self.dominio = args.get("dominio")
        self.subdominio = args.get("subdominio")
        self.paginas = args.get("paginas")

    def get_dominio(self):
        return self.dominio

    def set_dominio(self, dominio):
        self.dominio = dominio

    def get_subdominio(self):
        return self.subdominio

    def set_subdominio(self, subdominio):
        self.subdominio = subdominio

    def get_paginas(self):
        return self.paginas

    def set_paginas(self, paginas):
        self.paginas = paginas

    def __str__(self):
        return f'Dominio: {self.dominio}\nSubdominio: {self.dominio}\n Paginas: {self.paginas}'

    def buscador(self, pagina):
        pagina_url = pagina.get_url()
        paginas_ = self.get_paginas()
        for page in paginas_:
            urls_ = page.get_url()
            if pagina_url in urls_:
                return "El url " + pagina_url + " SI existe en el sitio web"
            else:
                return "El url" + pagina_url + " NO existe en el sitio web"


if __name__ == '__main__':

    # Creacion de objetos de tipo Page
    child_page = Page(url="https://www.gotmilk.com/every-child-is-unique-special-different/",
                      titulo="Every Child is Unique, Special, Different - Got Milk",
                      met_des="", formato="HTML")

    calcium_page = Page(url="https://www.gotmilk.com/kids-calcium-and-kale/",
                        titulo="Kids, Calcium and…12 cups of Kale? - Got Milk",
                        met_des="", formato="HTML")

    fake_page = Page(url="https://www.gotmilk.com/calcium-for-adults/",
                     titulo="Adults and Calcium Together",
                     met_des="Importance for Calcium in Adults could be significant", formato="XML")

    # Creacion de instancia de WebPage
    milk_page = WebPage(dominio='gotmilk.com/', subdominio='https://www.gotmilk.com/',
                        paginas=[child_page, calcium_page])

    # Prueba de busqueda sobre urls en el sitio web
    busqueda_child = milk_page.buscador(child_page)
    busqueda_fake = milk_page.buscador(fake_page)

    # Resultado de busqueda
    print(busqueda_child)
    print(busqueda_fake)
