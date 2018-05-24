class Programmer:

    def code(self):
        return 'I am Coding!'


class Tester():

    def test(self):
        return 'I am Testing!'


class ProjectManagement():

    def process(self, worker):
        if isinstance(worker, Programmer):
        	return worker.code()
        elif isinstance(worker, Tester):
        	return worker.test()
        else:
        	return 'Hey there!, Something went wrong :C'

project = ProjectManagement()

#print(project.process(programmer))
#print(project.process(tester))
