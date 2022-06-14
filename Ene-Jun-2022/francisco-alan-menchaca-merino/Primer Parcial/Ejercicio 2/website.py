from website_builder import WebsiteBuilder


class Website:
    def __init__(self,
                 url):
        self._URL = url
        self._domain = ""
        self._subdomain = ""
        self._hosting = ""
        self._website_type = ""
        self._priv_policy = ""
        self._pages = {}           # dictionary of pages (page_name, page)

    # Attributes getters and setters
    @property
    def url(self):
        return self._URL

    @url.setter
    def url(self, value):
        self._URL = value

    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, value):
        self._domain = value

    @property
    def subdomain(self):
        return self._subdomain

    @url.setter
    def subdomain(self, value):
        self._subdomain = value

    @property
    def hosting(self):
        return self._hosting

    @hosting.setter
    def hosting(self, value):
        self._hosting = value

    @property
    def website_type(self):
        return self._website_type

    @website_type.setter
    def website_type(self, value):
        self._website_type = value

    @property
    def priv_policy(self):
        return self._priv_policy

    @priv_policy.setter
    def priv_policy(self, value):
        self._priv_policy = value

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        self._pages = value

    def __str__(self):
        msg = f"\t|| Website Information ||\n"
        msg += f"- URL: {self._URL}\n"
        msg += f"- Domain: {self._domain}\n"
        msg += f"- Subdomain: {self._subdomain}\n"
        msg += f"- Hosting: {self._hosting}\n"
        msg += f"- Website Type: {self._website_type}\n"
        msg += f"- Privacy Policy: {self._priv_policy}\n"
        return msg


class ConcreteWebsiteBuilder(WebsiteBuilder):
    def __init__(self, url):
        self._website = Website(url)

    def set_domain(self, domain):
        self._website.domain = domain
        return self

    def set_subdomain(self, subdomain):
        self._website.subdomain = subdomain
        return self

    def set_hosting(self, hosting):
        self._website.hosting = hosting
        return self

    def set_website_type(self, website_type):
        self._website.website_type = website_type
        return self

    def set_priv_policy(self, priv_policy):
        self._website.priv_policy = priv_policy
        return self

    def add_pages(self, page_name, page):
        self._website.pages[page_name] = page
        return self

    def build(self):
        return self._website
