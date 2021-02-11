import pytest

from facade import SuitesFacade

@pytest.mark.parametrize("suites, expected", [
    (
        {
            'unit': True,
            'integration': True,
            'regression': True,
            'stress': True,
            'ab': True
        },
        "@@@@@ Suite de Tests Unitarios @@@@@\nInicializando...\nEjecutando tests...\nCleanup de objetos...\nTestsuite finalizada\n@@@@@ Suite de Tests de Integración @@@@@\nInicializando...\nEjecutando tests...\nCleanup de objetos...\nTestsuite finalizada\n@@@@@ Suite de Tests de Regresión @@@@@\nInicializando...\nEjecutando tests...\nCleanup de objetos...\nTestsuite finalizada\n@@@@@ Suite de Tests de Estrés @@@@@\nInicializando...\nEjecutando tests...\nCleanup de objetos...\nTestsuite finalizada\n@@@@@ Suite de Tests A/B @@@@@\nInicializando...\nEjecutando tests...\nCleanup de objetos...\nTestsuite finalizada\n"
    )
])
def test_run_all(capfd, suites, expected):
    SuitesFacade(suites).run_tests()
    out, _ = capfd.readouterr()
    assert out == expected

@pytest.mark.parametrize("suites, expected", [
    (
        {
            'unit': True,
            'integration': True,
            'regression': False,
            'stress': False,
            'ab': False
        },
        "@@@@@ Suite de Tests Unitarios @@@@@\nInicializando...\nEjecutando tests...\nCleanup de objetos...\nTestsuite finalizada\n@@@@@ Suite de Tests de Integración @@@@@\nInicializando...\nEjecutando tests...\nCleanup de objetos...\nTestsuite finalizada\nNo hay regression tests\nNo hay stress tests\nNo hay ab tests\n"
    ),
    (
        {
            'unit': False,
            'integration': False,
            'regression': True,
            'stress': True,
            'ab': False
        },
        "No hay unit tests\nNo hay integration tests\n@@@@@ Suite de Tests de Regresión @@@@@\nInicializando...\nEjecutando tests...\nCleanup de objetos...\nTestsuite finalizada\n@@@@@ Suite de Tests de Estrés @@@@@\nInicializando...\nEjecutando tests...\nCleanup de objetos...\nTestsuite finalizada\nNo hay ab tests\n"
    ),
    (
        {
            'unit': False,
            'integration': False,
            'regression': False,
            'stress': False,
            'ab': True
        },
        "No hay unit tests\nNo hay integration tests\nNo hay regression tests\nNo hay stress tests\n@@@@@ Suite de Tests A/B @@@@@\nInicializando...\nEjecutando tests...\nCleanup de objetos...\nTestsuite finalizada\n"
    )
])
def test_some(capfd, suites, expected):
    SuitesFacade(suites).run_tests()
    out, _ = capfd.readouterr()
    assert out == expected
    
@pytest.mark.parametrize("suites, expected", [
    (
        {
            'unit': False,
            'integration': False,
            'regression': False,
            'stress': False,
            'ab': False
        },
        "No hay unit tests\nNo hay integration tests\nNo hay regression tests\nNo hay stress tests\nNo hay ab tests\n"
    )
])
def test_none(capfd, suites, expected):
    SuitesFacade(suites).run_tests()
    out, _ = capfd.readouterr()
    assert out == expected