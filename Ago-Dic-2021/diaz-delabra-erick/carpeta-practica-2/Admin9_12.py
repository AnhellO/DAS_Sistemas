from MultiplesModulos9_12 import Usuario

class Admin(Usuario):
    def __init__(self, nombre, apellido, username, email, ubi):
        super().__init__(nombre, apellido, username, email, ubi)
        self.Privilegios = Privilegios([])
    
class Privilegios():
    def __init__(self, priv1):
        self.priv2 = priv1

    def privilegioss(self):
        for priv2 in self.priv1:
            print(priv2)