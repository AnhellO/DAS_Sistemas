import pytest
from webs import *

pagina_uno = PaginaWeb(url="www.georgeUadec.com", ruta="/index",
                     formato="HTML", contenido="<body> ¡¡This is Sparta!! </body> ",
                     titulo="<title> Live long and Prosper </title>", slug="Live-long-and-Prosper",
                     metatags=["<meta name="">", "<meta http-equiv="">", "<meta content="" ", "<meta charset=UTF-8>\n"])
 
#print(str(pagina_uno))

@pytest.mark.parametrize("expected", 
                ["""URL: www.georgeUadec.com\nRUTA: /index\nFORMATO: HTML\nCONTENIDO: <body> ¡¡This is Sparta!! </body>\nTITULO: <title> Live long and Prosper </title>\nSLUG: Live-long-and-Prosper\nMETA-TAGS: ['<meta name=>', '<meta http-equiv=>', '<meta content= ', '<meta charset=UTF-8>']\n"""])
def test_sitio_web( expected):
   
    assert str(pagina_uno) == expected
     