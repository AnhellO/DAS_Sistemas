import unittest
from ejercicio1 import buscador, Website, Page

test_cases = [
    {
        'name': 'website ok',
        'input': {
            'webiste': Website(
                    title='xd',
                    url='www.mywebsite.com/home.html',
                    domain='www.mywebsite.com',
                    subdomain='www.home.mywebsite.com',
                    type='Blog',
                    https=True,
                    web_pages = []
                ),
            'webpage':  [
                        Page(
                            file_name='home.html',
                            url='www.mywebsite.com/home.html',
                            format='html',
                            link='styles/styles.css',
                            script='main.js',
                            favicon='my_web_site.ico',
                            keywords=['mywebsite', 'WebPage', 'My'],
                            description='My awesome web site!',
                            content='The web site content is here!'
                        )
                    ],
        },
        'expected_output': True,
    },
]

class Test_ejercicio1(unittest.TestCase):
    def Test_buscador_func(self) -> None:
        for test in test_cases:
            website = test['input']['website']
            website['web_pages'] = test['input']['webpage']
            to_search = test['input']['webpage'][0]

            self.assertEqual(buscador(website, to_search), test['expected_output'])

if __name__ == '__main__':
    unittest.main()