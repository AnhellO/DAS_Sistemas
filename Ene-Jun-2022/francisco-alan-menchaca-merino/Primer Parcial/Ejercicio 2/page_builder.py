from abc import ABC, abstractmethod


class PageBuilder(ABC):
    @abstractmethod
    def set_title(self, title):
        pass

    @abstractmethod
    def add_header(self, header):
        pass

    @abstractmethod
    def add_paragraph(self, paragraph):
        pass

    @abstractmethod
    def add_hyperlink(self, hyperlink):
        pass

    @abstractmethod
    def add_list(self, list):
        pass

    @abstractmethod
    def add_script(self, script):
        pass

    @abstractmethod
    def add_CSS(self, css):
        pass

    @abstractmethod
    def add_images(self, image):
        pass
