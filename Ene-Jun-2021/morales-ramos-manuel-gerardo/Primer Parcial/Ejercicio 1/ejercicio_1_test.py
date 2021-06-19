import unittest

from ejercicio_1 import *

class Ejercicio1(unittest.TestCase):
    def test_website_1(self):
        page1 = WebPage('https://www.wp.com/home', 'https://www.wp.com/index.html', 'HTML', '<main></main>', 'Home', 'home', ['<meta>', '<meta>'])
    
        list_pages = [
            page1,
            
        ]

        website = WebSite('wp', 'Educational', list_pages)

        self.assertEqual('\r\nCategory: Educational\n\rDomain: wp\r\n\nWeb Pages: \r\n\nTitle: Home\nURL: https://www.wp.com/home\nSlug: home\nRoute: https://www.wp.com/index.html\nFormat: HTML\nContent: <main></main>\nMeta tags: <meta><meta>', 
        str(website))
    
    def test_website_2(self):
        page2 = WebPage('https://www.wp.com/about', 'https://www.wp.com/about.html', 'HTML', '<main></main>', 'About', 'about', ['<meta>', '<meta>'])

        list_pages = [
            page2,
            
        ]

        website = WebSite('wp', 'Educational', list_pages)

        self.assertEqual('\r\nCategory: Educational\n\rDomain: wp\r\n\nWeb Pages: \r\n\nTitle: About\nURL: https://www.wp.com/about\nSlug: about\nRoute: https://www.wp.com/about.html\nFormat: HTML\nContent: <main></main>\nMeta tags: <meta><meta>', 
        str(website))

    def test_website_3(self):
        page1 = WebPage('https://www.wp.com/about', 'https://www.wp.com/about.html', 'HTML', '<main></main>', 'About', 'about', ['<meta>', '<meta>'])
        page2 = WebPage('https://www.wp.com/faq', 'https://www.wp.com/faq.xml', 'XML', '<main></main>', 'FAQ', 'faq', ['<meta>', '<meta>'])

        list_pages = [
            page1,
            page2
        ]

        website = WebSite('wp', 'Educational', list_pages)

        output = '\r\nCategory: Educational\n\rDomain: wp\r\n\nWeb Pages: \r\n\nTitle: About\nURL: https://www.wp.com/about\nSlug: about\nRoute: https://www.wp.com/about.html\nFormat: HTML\nContent: <main></main>\nMeta tags: <meta><meta>'
        output += '\nTitle: FAQ\nURL: https://www.wp.com/faq\nSlug: faq\nRoute: https://www.wp.com/faq.xml\nFormat: XML\nContent: <main></main>\nMeta tags: <meta><meta>'

        self.assertEqual(output, str(website))
if __name__ == "__main__":
    unittest.main()