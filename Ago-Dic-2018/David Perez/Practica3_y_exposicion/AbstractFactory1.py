#Aplicación para construir coches mediante
#el ensamblado de sus partes (motor, chasis, etc.)
class AbstractFactory(object):
    def crearCoche(self, **args):
        raise NotImplementedError("Requires derived factory class for implementation.")
    def crearMotor(self, **args):
        raise NotImplementedError("Requires derived factory class for implementation.")
    def crearChasis(self, **args):
        raise NotImplementedError("Requires derived factory class for implementation.")

class CocheFord(object):
    def do_somthing(self):
        print ("Nuevo coche Ford")
class MotorFord(object):
    def do_somthing(self):
        print ("Nuevo Motor Ford")
class ChasisFord(object):
    def do_somthing(self):
        print ("Nuevo Chasis Ford")

class ConcreteFactory(AbstractFactory):
    def crearCoche(self):
        return CocheFord()
    def crearMotor(self):
        return MotorFord()
    def crearChasis(self):
        return ChasisFord()
class Client(object):
    def __init__(self, factory):
        self.factory = factory
    def use_a_product(self):
        s=input('Tipo:')
        if(s=='ford'):
            CocheFord = self.factory.crearCoche()
            CocheFord.do_somthing()
            MotorFord = self.factory.crearMotor()
            MotorFord.do_somthing()
            ChasisFord = self.factory.crearChasis()
            ChasisFord.do_somthing()
def main():
    factory = ConcreteFactory()
    client = Client(factory)
    client.use_a_product()
if __name__ == "__main__":
    main()
