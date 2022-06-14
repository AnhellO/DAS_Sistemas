# Class which simulates a Website
class Website:
    def __init__(self,
                 url,
                 domain,
                 subdomain,
                 hosting,
                 website_type,
                 priv_policy,
                 pages):
        self._URL = url
        self._domain = domain
        self._subdomain = subdomain
        self._hosting = hosting
        self._website_type = website_type
        self._priv_policy = priv_policy
        # dictionary of pages (page_name, page)
        self._pages = pages

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

    @subdomain.setter
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

    # String representation of the object
    def __str__(self):
        msg = f"\t|| Website Information ||\n"
        msg += f"- URL: {self._URL}\n"
        msg += f"- Domain: {self._domain}\n"
        msg += f"- Subdomain: {self._subdomain}\n"
        msg += f"- Hosting: {self._hosting}\n"
        msg += f"- Website Type: {self._website_type}\n"
        msg += f"- Privacy Policy: {self._priv_policy}\n"
        msg += f"- pages: {self._pages}\n" 
        return msg
