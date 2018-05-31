class Programmer:

    def code(self,saludo):
        raise NotImplementedError()

class Tester:

    def test(self, mensaje):
        raise NotImplementedError()

class ProjectManagement(Programmer,Tester):

    def __init__(self):
        self._storage={}
    def put(self,saludo):
        self._storage=[saludo.mood_id]=saludo

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
