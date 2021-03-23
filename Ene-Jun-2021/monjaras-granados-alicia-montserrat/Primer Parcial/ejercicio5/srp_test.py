import pytest

from srp import *

def test_formato_string():
    user = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z'
    )
    assert 'Nombre: Ramanujan\nEdad: 25\nDireccion: Calle X, #Y Colonia Z' == user.formato_string() 

def test_formato_diccionario():
    user = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z'
    )
    assert {'nombre': 'Ramanujan', 'edad': 25, 'direccion': 'Calle X, #Y Colonia Z'} == user.formato_diccionario() 

def test_formato_json():
    user = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z'
    )
    assert '{"nombre": "Ramanujan", "edad": 25, "direccion": "Calle X, #Y Colonia Z"}' == user.formato_json()


def test_formato_html():
    user = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z'
    )
    assert ('<table border="1"><tr><th>nombre</th><td>Ramanujan</td></tr><tr><th>edad</th><td>25</td></tr><tr><th>direccion</th><td>Calle X, #Y Colonia Z</td></tr></table>')  == user.formato_html()  

def test_formato_xml():
    user = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z'
    )
    assert ('<?xmlversion="1.0"?><all><nombretype="str">Ramanujan</nombre><edadtype="int">25</edad><direcciontype="str">CalleX,#YColoniaZ</direccion></all>') == user.formato_xml()