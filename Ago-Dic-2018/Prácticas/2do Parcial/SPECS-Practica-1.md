# Práctica 1

## Objetivo

Conocer y empaparse un poco de los principios `S.O.L.I.D.`

## Background

Concepto propuesto por **Michael Feathers** en su libro "_First Five Principles_". Los principios serían finalmente bautizados por **Robert C. Martin** (el famoso "_Uncle Bob_") más adelante, en su famoso libro "_Clean Code_". La palabra en sí es un acrónimo de las siguientes oraciones:

* **S**ingle Responsibility Principle (o _S.R.P._)
* **O**pen/Closed Principle (o _O.C.P._)
* **L**iskov Substitution Principle (o _L.S.P._)
* **I**nterface Segregation Principle (o _I.S.P._)
* **D**ependency Inversion Principle (o _D.I.P._)

Cada una de las anteriores frases es uno de los principios que forman parte del acrónimo `S.O.L.I.D.`, y estos proponen lo siguiente:

1. **S**ingle Responsibility Principle: Una clase, función y/o objeto debe de tener una única responsabilidad, y esta responsabilidad debe de ser su única razón para cambiar
2. **O**pen/Closed Principle: Cualquier entidad de software (clase, módulo, función, etc.) debe de estar abierta para su extensión, pero cerrada para su modificación. Esto quiere decir que no se debe de modificar el código fuente de la entidad al extender su comportamiento
3. **L**iskov Substitution Principle: Si `B` es un sub-tipo de `A`, entonces los objetos de tipo `A` pueden ser reemplazados por objetos del tipo `B` sin alterar ninguna propiedad del programa
4. **I**nterface Segregation Principle: Ninguna clase cliente debe de ser forzada a depender de métodos que no utiliza, por lo que hay que abstraer este tipo de lógica específica a interfaces más específicas
5. **D**ependency Inversion Principle: Las abstracciones no deben de depender de los detalles, sino los detalles deben de depender de las abstracciones

## Especificaciones

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

### Referencias

* [https://github.com/dboyliao/SOLID](https://github.com/dboyliao/SOLID)
* [https://medium.com/web-engineering-vox/how-to-write-solid-code-that-doesnt-suck-2a3416623d48](https://medium.com/web-engineering-vox/how-to-write-solid-code-that-doesnt-suck-2a3416623d48)