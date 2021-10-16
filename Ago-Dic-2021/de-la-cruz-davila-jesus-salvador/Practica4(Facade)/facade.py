prendas = {
    'camisa': 1,
    'pantalon': 2,
    'saco': 4
}

class Lavado:
    def lavando(self, prenda) -> str:
        return (f'Prendiendo Lavadora\nPreparando Lavadora\nLavando....\nTiempo de lavado: {prenda}')


class Enjuague:
    def enjuagando(self, prenda) -> str:
        return (f'Deteniendo Lavadora\nLavadora Detenida\nEnjuagando......\nTiempo de enjuague: {prenda}')


class Secar:
    def secando(self, prenda) -> str:
        return (f'Preparando modo Secado\nSecando....\nTiempo de secado: {prenda}')



class LavanderiaFachada:

    def __init__(self):
        self.lavado = Lavado()
        self.enjuague = Enjuague()
        self.secar = Secar()

    def empezarLavado(self) -> str:
        print(self.lavado.lavando(prendas['camisa']))
        print(self.enjuague.enjuagando(prendas['pantalon']))
        print(self.secar.secando(prendas['saco']))


if __name__ == '__main__':
    lavado = LavanderiaFachada()
    lavado.empezarLavado()
