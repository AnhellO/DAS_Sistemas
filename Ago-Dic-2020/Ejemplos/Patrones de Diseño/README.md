# Patrones de Diseño

Ejemplos de patrones de diseño con sus pruebas unitarias.

Para poder ejecutar los tests necesitas instalar [`pytest`](https://docs.pytest.org/en/stable/) por medio de `pip install pytest`. Una vez instalado puedes correr el siguiente comando con la clase de prueba que quieras ejecutar: `pytest -vvx file_test.py`, por ejemplo `pytest -vvx facade_test.py`.

En caso de querer generar el reporte de test-coverage, necesitas instalar [`pytest-cov`](https://pypi.org/project/pytest-cov/) utilizando `pip install pytest-cov`. Una vez instalado puedes generar el reporte general por medio del comando `pytest --cov-report=html --cov=.` (ejemplo en la carpeta de [htmlconv/](htmlconv/)).
