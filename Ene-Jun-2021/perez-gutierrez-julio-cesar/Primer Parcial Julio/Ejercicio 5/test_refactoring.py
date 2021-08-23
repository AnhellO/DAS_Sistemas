import pytest

from refactoring import *

def test_serializar_string():
    user = Usuario(
        'Ramanujan',
        25,
        'Calle X, #Y Colonia Z')
    assert user.serializar_string() == 'Nombre: Ramanujan\nEdad: 25\nDireccion: Calle X, #Y Colonia Z'

def test_serializar_diccionario():
    user = Usuario(
        'Ramanujan',
        25,
        'Calle X, #Y Colonia Z')
    assert user.serializar_diccionario() == {'nombre': 'Ramanujan', 'edad': 25, 'direccion': 'Calle X, #Y Colonia Z'}

def test_serializar_json():
    user = Usuario(
        'Ramanujan',
        25,
        'Calle X, #Y Colonia Z')
    assert user.serializar_json() == '{"nombre": "Ramanujan", "edad": 25, "direccion": "Calle X, #Y Colonia Z"}'

def test_serializar_html():
    user = Usuario(
        'Ramanujan',
        25,
        'Calle X, #Y Colonia Z')
    assert user.serializar_html() ==('<table ''border="1"><tr><th>nombre</th><td>Ramanujan</td></tr><tr><th>edad</th><td>25</td></tr><tr><th>direccion</th><td>Calle ' 'X, #Y Colonia Z</td></tr></table>')