from abc import ABC, abstractmethod


class PageBuilder(ABC):
    @abstractmethod
    def set_cuerpo(self, cuerpo):
        pass

    @abstractmethod
    def add_imagen(self, imagen):
        pass

    @abstractmethod
    def add_folder(self, folder):
        pass

    @abstractmethod
    def add_link(self, link):
        pass

    @abstractmethod
    def add_cabezera(self, cabezera):
        pass

    @abstractmethod
    def add_script(self, script):
        pass

    @abstractmethod
    def add_CSS(self, css):
        pass

    @abstractmethod
    def add_url(self, url):
        pass
