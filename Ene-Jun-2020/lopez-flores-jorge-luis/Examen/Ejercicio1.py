class Page:
    def __init__(self, url, link, tittle, paginas):
        self.url= url
        self.link= link
        self.tittle= tittle

        paginas = [Inicio, Contacto, Servicios]

 Page1 = Page('direccion de la pagina', https://es.wikipedia.org/wiki/P%C3%A1gina_web, <h1>'Como hacer una pagina web?'</h1>)

class Website:
    def __init__(self,**args):
        self.dominio = args.get('dominio')
        self.subdominio = args.get('subdominio')
        self.paginas = args.get('paginas')

     def set_dominio(self, dominio):
        self.dominio=dominio

    def get_dominio(self):
        return self._dominio

    def set_subdominio(self, subdominio):
        self.subdominio=subdominio

    def get_subdominio(self):
        return self._subdominio

    def set_pagina(self, pagina):
        self.pagina=pagina

    def get_pagina(self):
        return self._pagina

    enlace = Page()
    print(enlace.link)

    paginas = Page()
    print(paginas.paginas)

############################################
#############Ejercicio 2 ###################
    @decorator



