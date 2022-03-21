from typing import List
from abc import ABC, abstractmethod

# Las clases.
class WebPage:
    def __init__( 
        self,
        file_name: str, 
        format: str,
        styles: str,
        scripts: str,
        url: str,
        is_dynamic: bool,
        name: str,
        language: str,
        icon: str,
        content: str
        ) -> None:
        self.file_name = file_name
        self.format = format
        self.styles = styles
        self.scripts = scripts
        self.url = url
        self.is_dynamic = is_dynamic
        self.name = name
        self.language = language
        self.icon = icon
        self.content = content

    def get_web_page(self):
        return self

class WebSite:
    def __init__(
        self,
        name: str,
        url: str,
        domain: str,
        subdomain: str,
        https: bool,
        type: str,
        web_pages: List[WebPage]
    ) -> None:
        self.name = name
        self.url = url
        self.domain = domain
        self.subdomain = subdomain
        self.https = https
        self.type = type
        self.web_pages = web_pages

    def get_web_site(self):
        return self


# Interface genérica que da lineamientos para crear builders referentes a las paginas y sitios web.
class Builder(ABC):
    @property
    @abstractmethod
    def web(self) -> None:
        pass

    @abstractmethod
    def set_url(self, url: str) -> None:
        pass

    @abstractmethod
    def set_name(self, name: str) -> None:
        pass

    @abstractmethod
    def set_file_name(self, file_name: str) -> None:
        pass

    @abstractmethod
    def set_format(self, format: str) -> None:
        pass

    @abstractmethod
    def set_styles(self, styles: str) -> None:
        pass

    @abstractmethod
    def set_scripts(self, scripts: str) -> None:
        pass

    @abstractmethod
    def set_is_dynamic(self, is_dynamic: str) -> None:
        pass

    @abstractmethod
    def set_name(self, name: str) -> None:
        pass

    @abstractmethod
    def set_language(self, language: str) -> None:
        pass

    @abstractmethod
    def set_icon(self, icon: str) -> None:
        pass
    
    @abstractmethod
    def set_content(self, content: str) -> None:
        pass

    @abstractmethod
    def set_domain(self, domain: str) -> None:
        pass

    @abstractmethod
    def set_subdomain(self, subdomain: str) -> None:
        pass

    @abstractmethod
    def set_https(self, https: bool) -> None:
        pass

    @abstractmethod
    def set_type(self, type: str) -> None:
        pass

    @abstractmethod
    def set_web_pages(self, web_pages: List[WebPage]) -> None:
        pass


# Clase creadora de sitios web.
class WebSiteBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._web = WebSite('','','','',False,'',[])

    @property
    def web(self) -> WebPage:
        web = self._web
        self.reset()
        return web

    def set_name(self, name: str) -> None:
        self._web.name = name

    def set_url(self, url: str) -> None:
        self._web.url = url

    def set_domain(self, domain: str) -> None:
        self._web.domain = domain

    def set_subdomain(self, subdomain: str) -> None:
        self._web.subdomain = subdomain

    def set_https(self, https: bool) -> None:
        self._web.https = https

    def set_type(self, type: str) -> None:
        self._web.type = type

    def set_web_pages(self, web_pages: List[WebPage]) -> None:
        self._web.web_pages = web_pages


# Clase creadora de paginas web.
class WebPageBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._web = WebPage('','','','','',False,'','','','')

    @property
    def web(self) -> WebPage:
        web = self._web
        self.reset()
        return web

    def set_file_name(self, file_name: str) -> None:
        self._web.file_name = file_name

    def set_format(self, format: str) -> None:
        self._web.format = format

    def set_styles(self, styles: str) -> None:
        self._web.styles = styles

    def set_scripts(self, scripts: str) -> None:
        self._web.scripts = scripts

    def set_url(self, url: str) -> None:
        self._web.url = url

    def set_is_dynamic(self, is_dynamic: str) -> None:
        self._web.is_dynamic = is_dynamic

    def set_name(self, name: str) -> None:
        self._web.name = name

    def set_language(self, language: str) -> None:
        self._web.language = language

    def set_icon(self, icon: str) -> None:
        self._web.icon = icon

    def set_content(self, content: str) -> None:
        self._web.content = content


class WebPageDirector:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    # Se crea una pagina web simple
    def build_simple_web_page(
        self,
        file_name: str, 
        format: str,
        styles: str,
        scripts: str,
        url: str,
        is_dynamic: bool,
        name: str,
        language: str,
        icon: str,
        content: str
    ) -> None:
        self.builder.set_file_name(file_name)
        self.builder.set_format(format)
        self.builder.set_styles(styles)
        self.builder.set_scripts(scripts)
        self.builder.set_url(url)
        self.builder.set_is_dynamic(is_dynamic)
        self.builder.set_name(name)
        self.builder.set_language(language)
        self.builder.set_icon(icon)
        self.builder.set_content(content)

    # Aquí irían más variantes para crear paginas web, sólo que no se me ocurrieron más. 
    # def build_blog_page(self, ...) -> None:

class WebSiteDirector:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_simple_web_site(
        self,
        name: str,
        url: str,
        domain: str,
        subdomain: str,
        https: bool,
        type: str,
        web_pages: List[WebPage]
    ) -> None:
        self.builder.set_name(name)
        self.builder.set_url(url)
        self.builder.set_domain(domain)
        self.builder.set_subdomain(subdomain)
        self.builder.set_https(https)
        self.builder.set_type(type)
        self.builder.set_web_pages(web_pages)

    # Aquí irían más variantes para crear paginas web, sólo que no se me ocurrieron más. 
    # def build_social_network(self, ...) -> None:

    

if __name__ == '__main__':
    director = WebPageDirector()
    builder = WebPageBuilder()
    director.builder = builder

    director.build_web_page()