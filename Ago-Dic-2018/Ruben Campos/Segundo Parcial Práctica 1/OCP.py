from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

class Programmer(Worker):
    def work(self):
        return 'I am Coding!'


class Tester(Worker):
    def work(self):
        return 'I am Testing!'

class Chef(Worker):
    def work(self):
        return 'I am Cooking!'


class ProjectManagement:
    def process(self, worker):
        if isinstance(worker, Worker):
        	return worker.work()
        else:
        	return 'Hey there!, Something went wrong :C'

programmer = Programmer()
tester = Tester()
chef = Chef()

project = ProjectManagement()

print(project.process(programmer))
print(project.process(tester))
print(project.process(chef))

'''
El problema principal del codigo inicial era que si se necesitaba en un futuro crear una clase nueva
de otro tipo de trabajador, se necesitaria agregar la funcionalidad a la clase ProjectManagement para que imprimiera
el nuevo metodo que se creó.
Para aplicar el OCP se necesito usar una Clase Abstracta que implementara un metodo general work,
para asi crear clases de trabajadores que implementaran ese metodo abstracto work,
despues se cambió la clase ProjectManagement para que evaluara si el objeto fuese instancia de trabajador
imprimiera ese metodo general work que todas las clases implementan.
'''
