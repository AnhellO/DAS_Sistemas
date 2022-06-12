from abc import ABC, abstractmethod


class WebsiteBuilder(ABC):
    @abstractmethod
    def set_dominio(self, dominio):
        pass

    @abstractmethod
    def set_subdominio(self, subdominio):
        pass

    @abstractmethod
    def set_servidorweb(self, servidorweb):
        pass

    @abstractmethod
    def set_paginaweb(self, paginaweb):
        pass

    @abstractmethod
    def set_motordebusqueda(self, motordebusqueda):
        pass

    @abstractmethod
    def add_sitioweb(self, sitioweb):
        pass
