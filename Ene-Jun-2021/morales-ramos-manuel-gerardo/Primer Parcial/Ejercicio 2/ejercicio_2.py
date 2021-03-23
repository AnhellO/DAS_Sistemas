import abc

#Structure
class Component(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def seeker(self):
        pass

# Object to wrap
class WebPage(Component):
    def __init__(self, url, route, page_format, content, title, slug, meta_tags: list):
        self._url: str = url
        self._route: str = route
        self._format: str = page_format
        self._content: str = content
        self._title: str = title
        self._slug: str = slug
        self._meta_tags: list = meta_tags

    def __str__(self) -> str:
        return f"""
                \r    Title: {self._title}
                \r    URL: {self._url}
                \r    Slug: {self._slug}
                \r    Route: {self._route}
                \r    Format: {self._format}
                \r    Content: {self._content}
                \r    Meta tags: {self._meta_tags}
                \r    -----------------------------
                """

    def seeker(self):
        return self.__str__()

""" 
    Base Decorator to put the similar code of 
    your Concrete Decorators thought inheritance 
"""
class BaseDecorator(Component):
    def __init__(self, page: WebPage):
        self._wrappee = page

    def seeker(self):
        return f"""
                \r  The following web page:
                \r  -----------------------------
                \r  {self._wrappee.seeker()}
                """

#The wrapper
class WebSite(BaseDecorator):
    def __init__(self, domain, category, pages:list, page):
        super().__init__(page)
        self._domain: str = domain
        self._category: str = category
        self._pages: WebPage = pages

    def __str__(self) -> str:
        return f"""
                \r  Domain: {self._domain}
                \r  Category: {self._category}
                \r\n  Web Pages: 
                \r  {self.get_pages()}
                """

    def get_pages(self) -> WebPage:
        pages = ''
        for page in self._pages:
            pages += str(page)

        return pages

    def seeker(self):
        return f'{super().seeker()}{self.do_more()}{self.__str__()}'

    def do_more(self):
        try:
            self._pages.index(self._wrappee)
            return f"""
                        \r  EXISTS in the following website:
                        \r  -----------------------------
                    """
        except ValueError:
            return f"""
                        \r  DOES NOT EXIST in the following website:
                        \r  -----------------------------
                    """

def main():
    page1 = WebPage('https://www.wp.com/home', 'https://www.wp.com/index.html', 'HTML', '<main></main>', 'Home', 'home', ['<meta>', '<meta>'])
    page2 = WebPage('https://www.wp.com/about', 'https://www.wp.com/about.html', 'HTML', '<main></main>', 'About', 'about', ['<meta>', '<meta>'])
    page3 = WebPage('https://www.wp.com/about', 'https://www.wp.com/about.html', 'HTML', '<main></main>', 'Aout', 'about', ['<meta>', '<meta>'])
    
    list_pages = [
        page1,
        page2
    ]

    website = WebSite('wp', 'Educational', list_pages, page3).seeker()
    print(website)
  

if __name__ == "__main__":     
    main()