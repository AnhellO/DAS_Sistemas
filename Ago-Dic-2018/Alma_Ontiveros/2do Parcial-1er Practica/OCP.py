class Worker:
	def code (self):
		pass
	def test (self):
		pass
	def jump (self):
		pass

class Programmer(Worker):
    def code(self):
        return "I am Coding!"
class Tester(Worker):
    def test(self):
        return "I am Testing!"
class Jumper(Worker):
	def jump(self):
		return "I am Jumping!"

class ProjectManagement():
    def process(self, worker):
	    if isinstance(worker, Programmer):
		    return worker.code()
	    elif isinstance(worker, Tester):
		    return worker.test()
	    elif isinstance(worker, Jumper):
		    return worker.jump()
	    else:
             return "Hey there!, Something went wrong :c"

programmer = Programmer()
tester = Tester()
jumper = Jumper()
project = ProjectManagement()
print(project.process(programmer))
print(project.process(tester))
print(project.process(jumper))

#EXPLICACIÓN
#No estuve presente en la última clase para la explicación de esta tarea
#pero basandome en lo que se pedía en las indicaciones y viendo tutoriales
#a cerca del tema, lo que entendí fue que en la clase Project Management es
#la base para que funcione el Open-Closed porque en los ejemplos que checaba
#en la mayoría me salían. Esa clase es para que nos regrese si es Tester
#o Programmer y también puede extenderse, siempre y cuando cumpla
#con los requisitos de Open-Closed. Cree una clase llamada Worker donde ahí coloque
#las funciones "code" y "test" para que las clases Programmer y el Tester las hereden.