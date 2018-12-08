
#Clases donde cada clase es un test diferente
class TestUnitario:
    def run(self):
        print("--- Test Unitario ---")
        print("Realizando Test Unitario...")
        print("Resultados: -53,15\n")


class TestRegresion:
    def run(self):
        print("---- Test De Regresion ---")
        print("Realizando Test De Regresion...")
        print("Resultados: 20,20\n")


class TestIntegracion:
    def run(self):
        print("--- Test De Integracion ---")
        print("Realizando Test De Integracion...")
        print("Resultados: 0,-1\n")

#Implementando facade o fachada  la cual se encarga de ejecutar todas las pruebas en vez de realizar una por una por separado
class TestEjecutar:
    def __init__(self):
        self.testUnitario = TestUnitario()
        self.testRegresion = TestRegresion()
        self.testIntegracion = TestIntegracion()
        self.tests = [self.testUnitario, self.testRegresion, self.testIntegracion]
#La fachada manda llamar a la funcion All test el cual ejecutar todos os test
    def AllTest(self):
        print("--- Todos Los Test ---\n")
        [i.run() for i in self.tests]

#La fachada manda llamar a la funcion IntegracionAndRegresion el cual ejecutar solo dos test
    def IntegracionAndRegresion(self):
        print("--- Test De Integracion y Regresion ---\n")
        print("Realizando Test De Integracion y Regresion...")

        self.testRegresion.run()
        self.testIntegracion.run()

#La fachada manda llamar a la funcion UnitarioAndRegresion el cual ejecutar solo dos test
    def UnitarioAndRegresion(self):
        print("--- Test Unitario y de Regresion ---\n")
        print("Realizando Test Unitario y de Regresion...")

        self.testUnitario.run()
        self.testRegresion.run()

#La fachada manda llamar a la funcion UnitarioAndIntegracion el cual ejecutar solo dos test
    def UnitarioAndIntegracion(self):
        print("--- Test Unitario y de Integracion ---\n")
        print("Realizando Test Unitario y de Integracion...")

        self.testUnitario.run()
        self.testIntegracion.run()

# Esta es la parte del cliente el cual solo puede ejecutar los test ya sea todos a la vez o en ciertos conbinaciones
#El cliente no tiene acceso amodificar las clases de los test
if __name__ == '__main__':
    while True:
        seleccionado = int(input("Seleccione Test a realizar:\n"+"1.- Todos los test\n"+"2.Test De Integracion y Regresion\n"+"3.Test Unitario y Regresion\n"+"4.Test Unitario y De Integracion\n"+"5.-Salir\n"))

        if seleccionado==1:
            testEjecutados = TestEjecutar()
            testEjecutados.AllTest()
            pass
        if seleccionado==2:
            testJuntos=TestEjecutar()
            testJuntos.IntegracionAndRegresion()
        if seleccionado==3:
            testJuntos2=TestEjecutar()
            testJuntos2.UnitarioAndRegresion()
        if seleccionado==4:
            testJuntos3=TestEjecutar()
            testJuntos3.UnitarioAndIntegracion()
        if seleccionado==5:
            print("--- Gracias! ---\n")
            break
