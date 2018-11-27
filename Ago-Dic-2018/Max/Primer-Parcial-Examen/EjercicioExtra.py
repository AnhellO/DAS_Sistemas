class Builder:
    def build(self):
        self.prepararPan()
        self.agregaCarne()
        self.agregaVerduras()
        self.agregaCondimentos()
        self.hazlaCombo()

    def prepararPan(self, tipo):
        self.tipo = tipo #pan para hotdog o par ahamburguesa
        print('Pan de {}'.format(self.tipo))
        pass

    def agregaCarne(self, tipo):
        self.tipo = tipo #carne para hotdog o hamburguesa
        print('Carne de {}'.format(self.tipo))
        pass

    def agregaVerduras(self, tipo):
        self.tipo = tipo #tipo de verdura
        print('Agregar verduras: {}'.format(self.tipo))
        pass

    def agregaCondimentos(self):
        print('Agregregale condimentos')
        pass

    def hazlaCombo(self):
        print('quiero que lo hagas combo ')
        pass

class HamburguessaVegetariana(Builder):
    HM = Builder()
    print('Quiero una hamburguesa vegetariana')
    HM.prepararPan('hamburguesa con cesamo')
    HM.agregaVerduras('Tomate, espinacas, champiñones y lechuga, sin cebolla plis')
    HM.agregaCondimentos()
    HM.hazlaCombo()
    print('\n')

class HamburguessaDobleCarne(Builder):
    HDC = Builder()
    print('Quiero una hamburgues de doble carne')
    HDC.prepararPan('Pan de cesamo ')
    HDC.agregaVerduras('Tomate, champiñones, lechuga y sincebolla plis')
    HDC.agregaCondimentos()
    HDC.hazlaCombo()
    print('\n')

class HoCho(Builder):
    HD = Builder()
    print('Quiero un Hocho con todo')
    HD.prepararPan('Pan extra grande ')
    HD.agregaVerduras('Tomate, champiñones, lechuga, cebolla cruda y cebolla caramelizada, chile jalapeño, toda la verdura que tengas alv')
    HD.agregaCondimentos()
    HD.hazlaCombo()


if __name__ == '__main__':
    HV = HamburguessaVegetariana()
    HDC = HamburguessaDobleCarne()
    HD = HoCho()
