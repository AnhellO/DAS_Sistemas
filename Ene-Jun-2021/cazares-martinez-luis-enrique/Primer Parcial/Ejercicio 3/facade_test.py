import pytest

from facade import LavadoraFacade


@pytest.mark.parametrize("expected", [
    (
            "Lavando...\nEnjuagando...\nCentrifugando...\nFinalizado!\n"
    )
])
def test_ciclo_completo(capfd, expected):
    LavadoraFacade().ciclo_completo()
    out, _ = capfd.readouterr()
    assert out == expected


@pytest.mark.parametrize("expected", [
    (
            "Centrifugando...\nFinalizado!\n"
    )
])
def test_solo_centrifugado(capfd, expected):
    LavadoraFacade().solo_centrifugado()
    out, _ = capfd.readouterr()
    assert out == expected
