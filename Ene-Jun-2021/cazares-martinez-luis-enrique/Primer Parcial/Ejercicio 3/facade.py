# Se implementa el patron de diseño Facade el cuyo funcionamento separar de un sistema complejo a subsistemas.
# En este caso como la lavadora puede lavar, enjuagar, centrifugar, se crean sus respectivas clases
class Lavar:
    def __init__(self):
        pass
        # print('Iniciando Lavado...')

    def solo_lavado(self):
        return 'Lavando...\nFinalizado!\n'


class Enjuagar:
    def __init__(self):
        pass
        # print('Iniciando Enjuagado...')

    def solo_enjuagado(self):
        return 'Enjuagando...\nFinalizado!\n'


class Centrifugar:
    def __init__(self):
        pass
        # print('Iniciando Centrigugado...')

    def solo_centrifugado(self):
        return 'Centrifugando...\nFinalizado!\n'


# Se aplica el patron facade el cual implementa cada subsistema 
class LavadoraFacade:
    def __init__(self):
        pass
        # print('Lavadora Encendiendo...')

    def solo_lavar(self):
        return Lavar().solo_lavado()

    def solo_enjuagar(self):
        return Enjuagar().solo_enjuagado()

    def solo_centrifugado(self):
        return Centrifugar().solo_centrifugado()

    def ciclo_completo(self):
        return 'Lavando...\nEnjuagando...\nCentrifugando...\nFinalizado!\n'


if __name__ == '__main__':
    l = LavadoraFacade()
    print(l.solo_centrifugado())
