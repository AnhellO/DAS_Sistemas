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

suite1 = TestSuiteUnitario()
suite2 = TestSuiteDeIntegracion()
suite3 = TestSuiteDeRegresion()
suite4 = TestSuiteDeEstres()
suite5 = TestSuiteAB()

suite1.run()
suite2.run()
suite3.run()
suite4.run()
suite5.run()
