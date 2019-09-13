import time

SLEEP = 1

# Parte Compleja
class TestSuiteUnitario:
    def run(self):
        print(u"@@@@@ Suite de Tests Unitarios @@@@@")
        time.sleep(SLEEP)
        print(u"Inicializando...")
        time.sleep(SLEEP)
        print(u"Ejecutando tests...")
        time.sleep(SLEEP)
        print(u"Cleanup de objetos...")
        time.sleep(SLEEP)
        print(u"Testsuite finalizada")

class TestSuiteDeRegresion:
    def run(self):
        print(u"@@@@@ Suite de Tests de Regresión @@@@@")
        time.sleep(SLEEP)
        print(u"Inicializando...")
        time.sleep(SLEEP)
        print(u"Ejecutando tests...")
        time.sleep(SLEEP)
        print(u"Cleanup de objetos...")
        time.sleep(SLEEP)
        print(u"Testsuite finalizada")

class TestSuiteDeIntegracion:
    def run(self):
        print(u"@@@@@ Suite de Tests de Integración @@@@@")
        time.sleep(SLEEP)
        print(u"Inicializando...")
        time.sleep(SLEEP)
        print(u"Ejecutando tests...")
        time.sleep(SLEEP)
        print(u"Cleanup de objetos...")
        time.sleep(SLEEP)
        print(u"Testsuite finalizada")

class TestSuiteDeEstres:
    def run(self):
        print(u"@@@@@ Suite de Tests de Estrés @@@@@")
        time.sleep(SLEEP)
        print(u"Inicializando...")
        time.sleep(SLEEP)
        print(u"Ejecutando tests...")
        time.sleep(SLEEP)
        print(u"Cleanup de objetos...")
        time.sleep(SLEEP)
        print(u"Testsuite finalizada")

class TestSuiteAB:
    def run(self):
        print(u"@@@@@ Suite de Tests A/B @@@@@")
        time.sleep(SLEEP)
        print(u"Inicializando...")
        time.sleep(SLEEP)
        print(u"Ejecutando tests...")
        time.sleep(SLEEP)
        print(u"Cleanup de objetos...")
        time.sleep(SLEEP)
        print(u"Testsuite finalizada")

class TestsFacade:

    def __init__(self, tests={}):
        self.unitarios = TestSuiteUnitario() if tests.get('unitarios') else None
        self.integracion = TestSuiteDeIntegracion() if tests.get('integracion') else None
        self.regresion = TestSuiteDeRegresion() if tests.get('regresion') else None
        self.estres = TestSuiteDeEstres() if tests.get('estres') else None
        self.ab = TestSuiteAB() if tests.get('ab') else None

    def runTests(self):
        self.unitarios.run() if self.unitarios else print('No hay tests unitarios')
        self.integracion.run() if self.integracion else print('No hay tests integracion')
        self.regresion.run() if self.regresion else print('No hay tests regresion')
        self.estres.run() if self.estres else print('No hay tests estres')
        self.ab.run() if self.ab else print('No hay tests ab')

test_suites = {
    'unitarios': True,
    'integracion': True,
    'regresion': True,
    'estres': True,
    'ab': True
}

fachada = TestsFacade(test_suites)
fachada.runTests()
# suite1 = TestSuiteUnitario()
# suite2 = TestSuiteDeIntegracion()
# suite3 = TestSuiteDeRegresion()
# suite4 = TestSuiteDeEstres()
# suite5 = TestSuiteAB()
#
# suite1.run()
# suite2.run()
# suite3.run()
# suite4.run()
# suite5.run()