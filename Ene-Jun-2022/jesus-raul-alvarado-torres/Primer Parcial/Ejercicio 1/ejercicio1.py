from unicodedata import name


class Page(object):
    def __init__(
        self,
        file_name: str,
        url: str,
        format: str,
        link: str,
        script: str,
        favicon: str,
        keywords: list[str],
        description: str,
        content: str,
    ) -> None:
        self.file_name = file_name
        self.url = url
        self.format = format
        self.link = link
        self.script = script
        self.favicon = favicon
        self.keywords = keywords
        self.description = description
        self.content = content

class Website(object):
    def __init__(
        self, 
        title: str,
        url: str, 
        domain: str, 
        subdomain: str, 
        type: str, 
        https: bool, 
        web_pages: list[Page]
    ) -> None:
        self.title = title
        self.url = url
        self.domain = domain
        self.subdomain = subdomain
        self.type = type
        self.https = https
        self.web_pages = web_pages

def buscador(website: Website, page: Page) -> bool: 
    for web_page in website.web_pages:
        if web_page == page:
            return True 
    return False
