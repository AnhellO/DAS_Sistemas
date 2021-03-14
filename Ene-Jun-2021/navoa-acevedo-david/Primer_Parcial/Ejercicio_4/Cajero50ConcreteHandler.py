from Interface import IDcajero

class cajero10(IDcajero):
    #Da los billetes de 50 si es posible, si no, sigue con el siguiente en la cadena

    def __init__(self):
        self._successor = None
    
    #Coloca el siguiente succesor
    def next_successor(self, successor):
        self._successor = successor

    #metodo para manejar la entrega de billetes
    def handle(self, amount):
        if amount >= 50:
            num = amount // 50
            remainder = amount % 50
            print(f"Entregando {num} billetes de 50")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)