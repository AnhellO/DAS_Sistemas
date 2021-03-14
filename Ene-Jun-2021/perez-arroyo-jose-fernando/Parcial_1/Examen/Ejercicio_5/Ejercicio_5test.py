import pytest

from Ejercicio_5 import *

def test_serializar_string():
    user = Usuario('Ramanujan',25,'Calle X, #Y Colonia Z')
    Compara= 'Nombre: Ramanujan\nEdad: 25\nDireccion: Calle X, #Y Colonia Z'
    assert user.serializar_string() == Compara

def test_serializar_diccionario():
    user = Usuario('Ramanujan',25,'Calle X, #Y Colonia Z')
    Compara= 'Nombre: Ramanujan\nEdad: 25\nDireccion: Calle X, #Y Colonia Z'
    assert user.serializar_diccionario() == {Compara}

def test_serializar_json():
    user = Usuario('Ramanujan',25,'Calle X, #Y Colonia Z')
    Compara= 'Nombre: Ramanujan\nEdad: 25\nDireccion: Calle X, #Y Colonia Z'
    assert user.serializar_json() == '{Compara}'