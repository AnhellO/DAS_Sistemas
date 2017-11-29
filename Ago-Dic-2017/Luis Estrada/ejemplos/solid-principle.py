class Circulo():
    def __init__(self,radio):
        self.radio=radio
    def getRadio(self):
        return self.radio

class Cuadrado:
    def __init__(self, radio):
        self.radio=radio
    def getLado(self):
        return self.lado

c=Circulo(1.5)
print(c.getRadio())
