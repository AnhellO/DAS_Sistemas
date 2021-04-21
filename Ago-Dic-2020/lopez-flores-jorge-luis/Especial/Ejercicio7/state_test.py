import pytest

from state import *
    
@pytest.mark.parametrize("string, expected", [
    (
        "texto original",
        "texto original\n"
    )
])
def test_default_case(capfd, string, expected):
    state = DefaultCaseState()
    TextEditor(state).type_words(string)
    
    out, _ = capfd.readouterr()
    assert out == expected

@pytest.mark.parametrize("string, expected", [
    (
        "texto en mayúsculas",
        "TEXTO EN MAYÚSCULAS\n"
    )
])
def test_upper_case(capfd, string, expected):
    state = UpperCaseState()
    TextEditor(state).type_words(string)
    
    out, _ = capfd.readouterr()
    assert out == expected

@pytest.mark.parametrize("string, expected", [
    (
        "Texto en Minúsculas",
        "texto en minúsculas\n"
    )
])
def test_lower_case(capfd, string, expected):
    state = LowerCaseState()
    TextEditor(state).type_words(string)
    
    out, _ = capfd.readouterr()
    assert out == expected

@pytest.mark.parametrize("string, expected", [
    (
        "texto original",
        "Texto Original\n"
    )
])
def test_title_case(capfd, string, expected):
    state = TitleCaseState()
    TextEditor(state).type_words(string)
    
    out, _ = capfd.readouterr()
    assert out == expected

@pytest.mark.parametrize("string, expected", [
    (
        "Texto en Mayúsculas y Minúsculas",
        "TEXTO EN MAYÚSCULAS Y MINÚSCULAS\ntexto en mayúsculas y minúsculas\n"
    )
])
def test_multi_case(capfd, string, expected):
    state = UpperCaseState()
    te = TextEditor(state)
    te.type_words(string)

    new_state = LowerCaseState()
    te.set_state(new_state)
    te.type_words(string)
    
    out, _ = capfd.readouterr()
    assert out == expected