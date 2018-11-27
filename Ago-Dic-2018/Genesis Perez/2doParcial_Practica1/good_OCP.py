class Worker:
    def funcion(self):
        pass

class Programmer(Worker):

    def funcion(self):
        return 'I am Coding!'


class Tester(Worker):

    def funcion(self):
        return 'I am Testing!'


class ProjectManagement():

    # MI INTENCIÓN ES QUE ESTO COMENTADO FUNCIONARA PERO NO FUE ASI
    #def process(self, workers):
    #    self.workers = workers

    #def trabajo(self):
    #    for worker in self.workers:
    #        return worker.funcion()

    def process(self, worker):
        if isinstance(worker, Programmer):
        	return worker.funcion()
        elif isinstance(worker, Tester):
        	return worker.funcion()
        else:
        	return 'Hey there!, Something went wrong :C'

programmer = Programmer()
tester = Tester()

project = ProjectManagement()

print(project.process(programmer))
print(project.process(tester))


# EXPLICACION:
# En base a las referencias para consulta, mi intencion era que
# lo que está comentado en la clase ProjectManagement funcionara
# ya que entiendo que es parte de lo que maneja el principio Abierto/Cerrado
# porque lo vi en diferentes ejemplos que consulté, pero en vista del éxito
# no obtenido mejor dejé lo que ya estaba porque así si funciona.
# Los cambios que agregué son: crear una clase general llamada "Worker" para
# que de ella heredaran las otras clases que son más específicas (Programador y Tester)
# de tal forma que todo lo que las clases específicas tengan en común se encuentre en una
# sola clase, dejando abierto para añadir nuevas clases especificas y cerrado a que
# modifiquen la clase general (Worker).
