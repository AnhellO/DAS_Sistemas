import pytest
from srp import Usuario

#Creamos un objeto "user" de la clase "Usuario"
#Para trabajar con los test
user = Usuario(nombre='Ramanujan',edad=25,direccion='Calle X, #Y Colonia Z')

 
#Parametrizamos las pruebas del metodo "serializar_str()"
#Este nos devuelve un objeto en forma de string,
#Y para probarlo le ponemos un string de la misma forma.
@pytest.mark.parametrize("expected", 
        ["Nombre: Ramanujan\nEdad: 25\nDireccion: Calle X, #Y Colonia Z"] )
def test_serializar_str(expected):
    user_str = user.serializar_str()
    assert user_str == expected

#Parametrizamos las pruebas del metodo "serializar_dict()"
#Este nos devuelve un objeto en forma de un diccionario,
#Y para probarlo le ponemos un diccionario de la misma forma.
@pytest.mark.parametrize("expected",
        [{"nombre": "Ramanujan", "edad": 25, "direccion": "Calle X, #Y Colonia Z"}] )
def test_serializar_dict(expected):
    user_dict = user.serializar_dict()  
    assert user_dict == expected

#Parametrizamos las pruebas del metodo "serializar_json()"
#Este nos devuelve un objeto de tipo json, pero dentro de un string,
#Y para probarlo le ponemos un diccionario dentro de un string de la forma del objeto
@pytest.mark.parametrize("expected",
            ["""{"nombre": "Ramanujan", "edad": 25, "direccion": "Calle X, #Y Colonia Z"}"""] )
def test_serializar_json(expected):
    user_json = user.serializar_json()
    assert user_json == expected
 
#Parametrizamos las pruebas del metodo "serializar_html()"
#Este nos devuelve un objeto de tipo html, pero dentro de un string,
#Y para probarlo le ponemos un string en forma de una eestructura HTML
@pytest.mark.parametrize("expected",
        ["""<table border="1"><tr><th>nombre</th><td>Ramanujan</td></tr><tr><th>edad</th><td>25</td></tr><tr><th>direccion</th><td>Calle X, #Y Colonia Z</td></tr></table>"""] )
def test_serializar_html(expected):
    user_html = user.serializar_html()  
    assert user_html == expected

 
#pytest -q test_srp.py


#¿Qué sucedería si quiero agregar otro formato de serialización más complejo como XML o Yaml?
    #Respuesta: 
        # El sistema de pruebas seria muy parecido, solo habria que ajustar el
        # "expected" de manera que se parezca a la salida del objeto de tipo xml o Yaml
    
    
#¿Qué sucedería si quiero soporte para serialización a otros objetos aparte de los instanciados por la clase Usuario?
    #Respuesta: 
        # Habria que crear las clases para los objetos requeridos, y su vez,
        # Ver si por consecuencia de la creacion de estas clases, haría falta alguna
        # Refactorizacion de código (por objetos mas complejos), para despues
        # Hacer las pruebas correspondientes. 