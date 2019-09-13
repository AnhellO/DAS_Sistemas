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

#La clase ProjectManagment es la que se puede extender
#por eso la dejamos asi, ya que cumple con el principio
#Abierto/Cerrado

#(no le entendi muy bien)
