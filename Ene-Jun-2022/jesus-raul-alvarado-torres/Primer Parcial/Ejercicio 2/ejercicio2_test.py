import unittest
from ejercicio2 import *

test_cases = [
    {
        'name': 'web page ok',
        'input': [
        'mywebpage.html', 
        'html'
        'styles.css',
        'script.js',
        'www.mysite.com',
        True,
        'MyWebPage',
        'EN',
        'myicon.ico',
        'content here!'
        ],
    },
    {
        'name': 'web site ok',
        'input': [
        'MyWebSite', 
        'www.mywebsite.com'
        'www.mywebsite.com',
        'www.home.mywebsite.com',
        True,
        'Blog',
        []
        ],
    },
]

class Test_Builder_Method(unittest.TestCase):
    def test_builder(self) -> None:
        for test in test_cases:
            if len(test['input']) == 10:
                director = WebPageDirector()
                builder = WebPageBuilder()
                director.builder = builder
                director.build_simple_web_page(*test['input'])
                self.assertEqual(builder.web, WebPage(*test['input']))
            elif len(test['input']) == 7:
                director = WebSiteDirector()
                builder = WebSiteBuilder()
                director.builder = builder
                director.build_simple_web_site(*test['input'])
                self.assertEqual(builder.web, WebPage(*test['input']))

if __name__ == '__main__':
    unittest.main()