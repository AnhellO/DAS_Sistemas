from abc import ABCMeta, abstractproperty

class Be(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def programmer(self):
        pass

    @abstractproperty
    def tester(self):
        pass

class Programmer(Be):

    @property
    def code(self):
        return 'I am Coding!'

class Tester(Be):

    @property
    def test(self):
        return 'I am Testing!'


class ProjectManagement(object):

    def __init__(self, worker):
        self.worker = worker

    @property
    def process(self, worker):
        if isinstance(worker, Programmer):
        	return worker.code()
        elif isinstance(worker, Tester):
        	return worker.test()
        else:
        	return 'Hey there!, Something went wrong :C'

def main():
    programmer = Programmer()
    tester = Tester()
    project = ProjectManagement(worker)
    print(project.process(programmer))
    print(project.process(tester))

if __name__ == '__main__':
    main()
