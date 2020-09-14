# Práctica 3

## Objetivo

* Aprender sobre el proceso de la refactorización
* Ser capaz de observar, analizar y mejorar código ajeno
* Mejorar habilidades de desarrollo y de POO

## Especificaciones

* Para el [ejemplo del patrón de diseño `Simple Factory`](https://github.com/AnhellO/DAS_Sistemas/tree/development/Ago-Dic-2020/Ejemplos/Patrones%20de∞20Diseño/simple_factory.py) expuesto durante la clase del `2020-09-10`, continua con el proceso de refactorización llevado a cabo en la clase de tal manera que tomes en cuenta los siguientes puntos:
  * Agrega una nueva función a la clase `SchoolMember`, pero en esta ocasión que la función sea abstracta
  * Sobreescribe el método `__str__` pero de manera más `D.R.Y.` y menos `W.E.T.`
  * Heredemos otra nueva clase desde `SchoolMember` y hagamos `T.D.D.` sobre ese nuevo caso
  * ¿Qué posibles casos nos faltan probar en la clase de `simple_factory_test.py`?
  * ¿Cómo podemos deshacernos del bloque try/catch?
  * ¿Hay algún otro valor que podamos regresar aparte de `"Error! tipo '{kind}' invalido!"`?

## Recursos

* <https://docs.pytest.org/en/stable/>
* <https://realpython.com/pytest-python-testing/>
* <https://refactoring.com/>
* <https://refactoring.guru/es/refactoring>
* <https://sourcemaking.com/refactoring>
* <https://docs.python.org/3/library/abc.html>

## Deadline

* `Jueves 24 de Septiembre a las 7:00pm`
