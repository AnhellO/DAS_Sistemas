import pytest
from srp import *

####### green - red tests################
@pytest.mark.parametrize("expected", [
    (
        "Nombre: Ramanujan\nEdad: 25\nDireccion: Calle X, #Y Colonia Z\n"
    )
])

def test_string(capfd, expected):
    user = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z'
    )
    
    print(user.serializar("string"))
    out, _ = capfd.readouterr()
    assert out == expected

@pytest.mark.parametrize("expected", [
    (
        "{'nombre': 'Ramanujan', 'edad': 25, 'direccion': 'Calle X, #Y Colonia Z'}\n"
    )
])

def test_dict(capfd, expected):
    user = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z'
    )
    
    print(user.serializar("diccionario"))
    out, _ = capfd.readouterr()
    assert out == expected
    
@pytest.mark.parametrize("expected", [
    (
        '{"nombre": "Ramanujan", "edad": 25, "direccion": "Calle X, #Y Colonia Z"}\n'
    )
])

def test_json(capfd, expected):
    user = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z'
    )
    
    print(user.serializar("json"))
    out, _ = capfd.readouterr()
    assert out == expected

    
@pytest.mark.parametrize("expected", [
    (
        '<table border="1"><tr><th>nombre</th><td>Ramanujan</td></tr><tr><th>edad</th><td>25</td></tr><tr><th>direccion</th><td>Calle X, #Y Colonia Z</td></tr></table>\n'
    )
])

def test_html(capfd, expected):
    user = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z'
    )
    
    print(user.serializar("html"))
    out, _ = capfd.readouterr()
    assert out == expected
    
##############Refactoring-single responsibility principle######################## 
@pytest.mark.parametrize("expected", [
    (
        "Nombre: Ramanujan\nEdad: 25\nDireccion: Calle X, #Y Colonia Z\n"
    )
])

def test_string_SRP(capfd, expected):
    user = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z'
    )
    
    serializar = user.serializar_string()
    print(serializar)
    out, _ = capfd.readouterr()
    assert out == expected

@pytest.mark.parametrize("expected", [
    (
        "{'nombre': 'Ramanujan', 'edad': 25, 'direccion': 'Calle X, #Y Colonia Z'}\n"
    )
])

def test_dict_SRP(capfd, expected):
    user = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z'
    )
    
    serializar = user.serializar_dict()
    print(serializar)
    out, _ = capfd.readouterr()
    assert out == expected
    
@pytest.mark.parametrize("expected", [
    (
        '{"nombre": "Ramanujan", "edad": 25, "direccion": "Calle X, #Y Colonia Z"}\n'
    )
])

def test_json_SRP(capfd, expected):
    user = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z'
    )
    
    serializar = user.serializar_json()
    print(serializar)
    out, _ = capfd.readouterr()
    assert out == expected

    
@pytest.mark.parametrize("expected", [
    (
        '<table border="1"><tr><th>nombre</th><td>Ramanujan</td></tr><tr><th>edad</th><td>25</td></tr><tr><th>direccion</th><td>Calle X, #Y Colonia Z</td></tr></table>\n'
    )
])

def test_html_SRP(capfd, expected):
    user = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z'
    )
    
    serializar = user.serializar_html()
    print(serializar)
    out, _ = capfd.readouterr()
    assert out == expected
    