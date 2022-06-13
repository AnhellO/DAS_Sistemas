from website_builder import WebsiteBuilder


class Website:
    def __init__(self, URL):
        self.URL = URL
        self.dominio = ""
        self.subdominio = ""
        self.servidorweb= ""
        self.paginaweb = ""
        self.motordebusqueda = ""
        self.sitioweb = {}           

    
    @property
    def URL(self):
        return self._URL

    @URL.setter
    def URL(self, value):
        self._URL = value

    @property
    def dominio(self):
        return self._dominio

    @dominio.setter
    def domain(self, value):
        self._dominuo = value

    @property
    def subdominio(self):
        return self._subdominio

    @URL.setter
    def subdominio(self, value):
        self._subdominio= value

    @property
    def servidorweb(self):
        return self._servidorweb

    @servidorweb.setter
    def servidorweb(self, value):
        self._servidorweb = value

    @property
    def paginaweb(self):
        return self._paginaweb

    @paginaweb.setter
    def paginaweb(self, value):
        self.paginaweb = value

    @property
    def motordebusqueda(self):
        return self.motordebusqueda

    @motordebusqueda.setter
    def motordebusqueda(self, value):
        self.motordebusqueda= value

    @property
    def sitioweb(self):
        return self._sitioweb

    @sitioweb.setter
    def pages(self, value):
        self.sitioweb = value

    def __str__(self):
        mensaje  = "\n* URL: " + self.URL
        mensaje += "\n* dominio: " + self.dominio
        mensaje += "\n* subdominio: " + self.subdominio
        mensaje += "\n* servidorweb " + self.servidorweb
        mensaje += "\n* paginaweb: " + str(self.paginaweb)
        mensaje += "\n* motordebusqueda: " + self.motordebusqueda
        mensaje += "\n* sitioweb: " + self.sitioweb
        return mensaje 


class ConcreteWebsiteBuilder(WebsiteBuilder):
    def __init__(self, URL):
        self.URL = Website(URL)

    def set_dominio(self, dominio):
        self.Website_dominio = dominio
        return self

    def set_subdominio(self, subdominio):
        self.Website_subdominio = subdominio
        return self

    def set_servidorweb(self, servidorweb):
        self.Website_servidorweb = servidorweb
        return self

    def set_paginaweb(self,paginaweb):
        self.Website_paginaweb= paginaweb
        return self

    def set_motordebusqueda(self, motordebusqueda):
        self.Website_motrodebusqueda= motordebusqueda
        return self

    def add_sitioweb(self, sitioweb):
        self.Website_sitioweb = sitioweb
        return self

    def build(self):
        return self._website
