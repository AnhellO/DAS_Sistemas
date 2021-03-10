class WebPage:
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
                \r  Title: {self._title}
                \r  URL: {self._url}
                \r  Slug: {self._slug}
                \r  Route: {self._route}
                \r  Format: {self._format}
                \r  Content: {self._content}
                \r  Meta tags: {self._meta_tags}
                \r  -----------------------------
                """

class WebSite:
    def __init__(self, domain, category, pages:list):
        self._domain: str = domain
        self._category: str = category
        self._pages: WebPage = pages

    def __str__(self) -> str:
        return f"""
                \rDomain: {self._domain}
                \rCategory: {self._category}
                \r\nWeb Pages: 
                \r{self.get_pages()}
                """

    def get_pages(self) -> WebPage:
        pages = ''
        for page in self._pages:
            pages += str(page)

        return pages

def main():
    webpage1 = WebPage('https://www.wp.com/home', 'https://www.wp.com/index.html', 'HTML', '<main></main>', 'Home', 'home', ['<meta>', '<meta>'])
    webpage2 = WebPage('https://www.wp.com/contact-me', 'https://www.wp.com/contact-me.html', 'HTML', '<main></main>', 'Contact Me', 'contact-me', ['<meta>', '<meta>'])
    webpage3 = WebPage('https://www.wp.com/faq', 'https://www.wp.com/faq.html', 'HTML', '<main></main>', 'FAQ', 'faq', ['<meta>', '<meta>'])
    
    pages = [webpage1, webpage2, webpage3]
    
    website = WebSite('wp', 'Educational', pages)
    print(website)

if __name__ == "__main__":     
    main()