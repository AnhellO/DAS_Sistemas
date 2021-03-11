class WebPage:
    def __init__(self, url, route, page_format, content, title, slug, meta_tags = []):
        self._url: str = url
        self._route: str = route
        self._format: str = page_format
        self._content: str = content
        self._title: str = title
        self._slug: str = slug
        self._meta_tags: list = meta_tags

    def __str__(self) -> str:
        return f'\nTitle: {self._title}\nURL: {self._url}\nSlug: {self._slug}\nRoute: {self._route}\nFormat: {self._format}\nContent: {self._content}\nMeta tags: {self.get_tags()}'
    
    def get_tags(self):
        tags = ''
        for tag in self._meta_tags:
            tags += str(tag)

        return tags

class WebSite:
    def __init__(self, domain, category, pages:list):
        self._domain: str = domain
        self._category: str = category
        self._pages: WebPage = pages

    def __str__(self) -> str:
        return f'\r\nCategory: {self._category}\n\rDomain: {self._domain}\r\n\nWeb Pages: \r\n{self.get_pages()}'

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