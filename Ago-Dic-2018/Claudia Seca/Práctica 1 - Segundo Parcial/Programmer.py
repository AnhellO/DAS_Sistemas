#clase programmer
class Programmer:


#Función del codester
    def code(self):
        return 'I am Coding!'

#clase tester
class Tester:

#Función del tester
    def test(self):
        return 'I am Testing!'

#Esta clase nos regresa si el trabajador es Tester o Programmer
#Esta clase es la que prevalece y puede ser extendida, cumpliendo el principio de Open/Closed Principle
class ProjectManagement:

    def process(self, worker):
        if isinstance(worker, Programmer):
        	return worker.code()
        elif isinstance(worker, Tester):
        	return worker.test()
        else:
        	return 'Hey there!, Something went wrong :C'

#objetos de la clase ProjectManagement
programmer = Programmer()
tester = Tester()

project = ProjectManagement()

print(project.process(programmer))
print(project.process(tester))
