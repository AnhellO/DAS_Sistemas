import pytest
from Ejercicio_1 import * 
@pytest.mark.parametrize("expected", [
    (
        "El dominio del sitio es: www.youtube.com\nLa categoria del sitio es: Entretenimiento\nLas paginas del sitio son:\nEl url de la pagina es: https://www.youtube.com/watch?v=dQw4w9WgXcQ\nLa ruta del archivo es:C://User/practica\nEl formato del archivo es: HTML\nEl contenido de la pagina es: <body> <p> hola soy una practica </p></body>\nEl titulo de la pagina es: <h1>Practica 1</h1>\nEl slug de la pagina es: practica-1\nLos meta-tags de la pagina son: ['tags', 'tags']\n"
    )
])
# se testea el formato de la pagina HTML
def test_HTML_1_pagina(capfd, expected):
    pagina = PaginaWeb("https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                       "C://User/practica",
                       "HTML",
                       "<body> <p> hola soy una practica </p></body>",
                       "<h1>Practica 1</h1>",
                       "practica-1",
                       ["tags",
                        "tags"])  
    
    sitio = SitioWeb("www.youtube.com",
                     "Entretenimiento",
                     pagina)
    
    print(sitio)
    out, _ = capfd.readouterr()
    assert out == expected
# se testea el formato de la pagina PHP
@pytest.mark.parametrize("expected", [
    (
        "El dominio del sitio es: www.youtube.com\nLa categoria del sitio es: Entretenimiento\nLas paginas del sitio son:\nEl url de la pagina es: https://www.youtube.com/watch?v=dQw4w9WgXcQ\nLa ruta del archivo es:C://User/practica\nEl formato del archivo es: PHP\nEl contenido de la pagina es: <?php<body> <p> hola soy una practica </p></body>?>\nEl titulo de la pagina es: <h1>Practica 1</h1>\nEl slug de la pagina es: practica-1\nLos meta-tags de la pagina son: ['tags', 'tags']\n"
    )
])

def test_PHP_1_pagina(capfd, expected):
    pagina = PaginaWeb("https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                       "C://User/practica",
                       "PHP",
                       "<?php<body> <p> hola soy una practica </p></body>?>",
                       "<h1>Practica 1</h1>",
                       "practica-1",
                       ["tags",
                        "tags"])  

@pytest.mark.parametrize("expected", [
    (
        "El dominio del sitio es: www.youtube.com\nLa categoria del sitio es: Entretenimiento\nLas paginas del sitio son:\nEl url de la pagina es: https://www.youtube.com/watch?v=dQw4w9WgXcQ\nLa ruta del archivo es:C://User/practica\nEl formato del archivo es: JS\nEl contenido de la pagina es: function validate(){if(x>0){y=True}}\nEl titulo de la pagina es: <h1>Practica 1</h1>\nEl slug de la pagina es: practica-1\nLos meta-tags de la pagina son: ['tags', 'tags']\n"
    )
])
# se testea el formato de la pagina JS
def test_js_1_pagina(capfd, expected):
    pagina = PaginaWeb("https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                       "C://User/practica",
                       "JS",
                       "function validate(){if(x>0){y=True}}",
                       "<h1>Practica 1</h1>",
                       "practica-1",
                       ["tags",
                        "tags"])      

    sitio = SitioWeb("www.youtube.com",
                     "Entretenimiento",
                     pagina)
    
    print(sitio)
    out, _ = capfd.readouterr()
    assert out == expected