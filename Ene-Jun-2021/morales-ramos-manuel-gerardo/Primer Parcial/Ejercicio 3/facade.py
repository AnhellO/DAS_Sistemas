class CicloCompleto:
    def run(self):
        print('Lavando...')
        print('Enjuagando...')
        print('Centrifugando...')
        print('Finalizado!')

class SoloCentrifugado:
    def run(self):
        print('Centrifugando...')
        print('Finalizado!')

class LavadoraFacade:
    def __init__(self):
        self._ciclo_completo = CicloCompleto()
        self._solo_centrifugado = SoloCentrifugado()

    def ciclo_completo(self):
        self._ciclo_completo.run()

    def solo_centrifugado(self):
        self._solo_centrifugado.run()

def main():
    LavadoraFacade().ciclo_completo()
    LavadoraFacade().solo_centrifugado()

if __name__ == "__main__":
    main()