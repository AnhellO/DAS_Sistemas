from abc import ABC, abstractmethod


class WebsiteBuilder(ABC):
    @abstractmethod
    def set_domain(self, domain):
        pass

    @abstractmethod
    def set_subdomain(self, subdomain):
        pass

    @abstractmethod
    def set_hosting(self, hosting):
        pass

    @abstractmethod
    def set_website_type(self, website_type):
        pass

    @abstractmethod
    def set_priv_policy(self, priv_policy):
        pass

    @abstractmethod
    def add_pages(self, page_name, page):
        pass
