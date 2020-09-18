import time

SLEEP = 1

# Parte Compleja
class UnitSuite:
    def run(self):
        print("@@@@@ Suite de Tests Unitarios @@@@@")
        # time.sleep(SLEEP)
        print("Inicializando...")
        # time.sleep(SLEEP)
        print("Ejecutando tests...")
        # time.sleep(SLEEP)
        print("Cleanup de objetos...")
        # time.sleep(SLEEP)
        print("Testsuite finalizada")

class RegressionSuite:
    def run(self):
        print("@@@@@ Suite de Tests de Regresión @@@@@")
        # time.sleep(SLEEP)
        print("Inicializando...")
        # time.sleep(SLEEP)
        print("Ejecutando tests...")
        # time.sleep(SLEEP)
        print("Cleanup de objetos...")
        # time.sleep(SLEEP)
        print("Testsuite finalizada")

class IntegrationSuite:
    def run(self):
        print("@@@@@ Suite de Tests de Integración @@@@@")
        # time.sleep(SLEEP)
        print("Inicializando...")
        # time.sleep(SLEEP)
        print("Ejecutando tests...")
        # time.sleep(SLEEP)
        print("Cleanup de objetos...")
        # time.sleep(SLEEP)
        print("Testsuite finalizada")

class StressSuite:
    def run(self):
        print("@@@@@ Suite de Tests de Estrés @@@@@")
        # time.sleep(SLEEP)
        print("Inicializando...")
        # time.sleep(SLEEP)
        print("Ejecutando tests...")
        # time.sleep(SLEEP)
        print("Cleanup de objetos...")
        # time.sleep(SLEEP)
        print("Testsuite finalizada")

class ABSuite:
    def run(self):
        print("@@@@@ Suite de Tests A/B @@@@@")
        # time.sleep(SLEEP)
        print("Inicializando...")
        # time.sleep(SLEEP)
        print("Ejecutando tests...")
        # time.sleep(SLEEP)
        print("Cleanup de objetos...")
        # time.sleep(SLEEP)
        print("Testsuite finalizada")

# Fachada que el cliente consume
class SuitesFacade:
    def __init__(self, tests={}):
        self.unit = UnitSuite() if tests.get('unit') else None
        self.integration = IntegrationSuite() if tests.get('integration') else None
        self.regression = RegressionSuite() if tests.get('regression') else None
        self.stress = StressSuite() if tests.get('stress') else None
        self.ab = ABSuite() if tests.get('ab') else None

    def run_tests(self):
        self.unit.run() if self.unit else print('No hay unit tests')
        self.integration.run() if self.integration else print('No hay integration tests')
        self.regression.run() if self.regression else print('No hay regression tests')
        self.stress.run() if self.stress else print('No hay stress tests')
        self.ab.run() if self.ab else print('No hay ab tests')

def main():
    test_suites = {
        'unit': True,
        'integration': True,
        'regression': True,
        'stress': True,
        'ab': True
    }

    facade = SuitesFacade(test_suites)
    facade.run_tests()

    # suite1 = UnitSuite()
    # suite2 = IntegrationSuite()
    # suite3 = RegressionSuite()
    # suite4 = StressSuite()
    # suite5 = ABSuite()

    # suite1.run()
    # suite2.run()
    # suite3.run()
    # suite4.run()
    # suite5.run()

if __name__ == "__main__":
    main()