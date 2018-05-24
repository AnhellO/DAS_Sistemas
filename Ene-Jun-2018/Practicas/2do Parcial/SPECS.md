# 2do. Examen Parcial

## Especificaciones y Requerimientos

- Para las partes teóricas, contesta sobre hojas en blanco
- Para las partes prácticas, desarrolla los ejemplos de código en tu computadora, y envíalos al repositorio de la materia, siguiendo los [lineamientos de contribución del repositorio](https://github.com/AnhellO/DAS_Sistemas#contributing). La carpeta de práctica en este caso tendría que llamarse `../Primer Parcial/..`
- Total Parte Teórica: 50%
- Total Parte Práctica: 50%

## Parte Teórica

1. ¿Qué son los SOLID principles?
2. ¿Cuál es el objetivo del `Single Responsibility Principle`?
3. ¿Cuál es el objetivo del `Open/Closed Principle`?
4. ¿Cuál es el objetivo del `Liskov Substitution Principle`?
5. ¿Cuál es el objetivo del `Interface Segregation Principle`?
6. ¿Cuál es el objetivo del `Dependency Inversion Principle`?
7. Menciona las características principales de la arquitectura monolítica. Anexe un pequeño diagrama que explique en rasgos generales como se distribuye este tipo de arquitectura.
7. Menciona las características principales de la arquitectura de micro-servicios. Anexe un pequeño diagrama que explique en rasgos generales como se distribuye este tipo de arquitectura.

## Parte Práctica

1. Para el siguiente ejemplo de código:

```python
import json

class Report:

    def getTitle(self):
        return 'Title!'

    def getDate(self):
        return '2018-05-23'

    def getContents(self):
        return {
        	'title': self.getTitle(),
        	'date': self.getDate()
        }

    def formatJson(self):
    	return json.dumps(self.getContents())

report = Report()
print(report.getContents())
```

* Refactoriza implementando el `Single Responsibility Principle`
* Explica el porqué de tus cambios

2. Para el siguiente ejemplo de código:

```python
class Programmer:

    def code(self):
        return 'I am Coding!'


class Tester:

    def test(self):
        return 'I am Testing!'


class ProjectManagement:

    def process(self, worker):
        if isinstance(worker, Programmer):
        	return worker.code()
        elif isinstance(worker, Tester):
        	return worker.test()
        else:
        	return 'Hey there!, Something went wrong :C'

programmer = Programmer()
tester = Tester()

project = ProjectManagement()

print(project.process(programmer))
print(project.process(tester))
```

* Refactoriza implementando el `Open-Closed Principle`
* Explica el porqué de tus cambios

## Puntos Extra

* Menos W.E.T. y más D.R.Y.
* Implementa un breve ejemplo del `Dependency Inversion Principle` utilizando el módulo de [python-dependency-injector](https://github.com/ets-labs/python-dependency-injector) utilizando instrumentos musicales como objetos