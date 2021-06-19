from Interface import IDcajero

class cajero20(IDcajero):
    #Da los billetes de 20 si es posible, si no, sigue con el siguiente en la cadena

    def __init__(self):
        self._successor = None
    
    #Coloca el siguiente succesor
    def next_successor(self, successor):
        self._successor = successor

    #metodo para manejar la entrega de billetes
    def handle(self, amount):
        if amount >= 20:
            num = amount // 20
            remainder = amount % 20
            print(f"Entregando {num} billetes de 20")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)