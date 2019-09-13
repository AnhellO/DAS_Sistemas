class Programmer:

    def code(self):
        return 'I am Coding!'


class Tester:

    def test(self):
        return 'I am Testing!'

#Principio de Open/Closed Principle
#La clase ProjectManagement es la que prevalece y puede ser extendida,
class ProjectManagement:

    def process(self, worker):
        if isinstance(worker, Programmer):
        	return worker.code()
        elif isinstance(worker, Tester):
        	return worker.test()
        else:
        	return 'Hey there!, Something went wrong D:'

programmer = Programmer()
tester = Tester()

project = ProjectManagement()

print(project.process(programmer))
print(project.process(tester))
