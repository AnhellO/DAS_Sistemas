class Comida(object):
    def __init__(self):
        self.preparaPan = None
        self.agregaCarne = None
        self.agregaVerduras = None
        self.agregaCondimentos = None
        self.hazlaCombo = None

    def set_preparaPan(self, pan):
        self.preparaPan = pan

    def set_agregaCarne(self, carne):
        self.agregaCarne = carne

    def set_agregaVerduras(self, verduras):
        self.agregaVerduras = verduras

    def set_agregaCondimentos(self, condimentos):
        self.agregaCondimentos = condimentos

    def set_hazlaCombo(self, combo):
        self.hazlaCombo = combo

    def __str__(self):
        return 'Preparamos el Pan: {}\nAgregamos la Carne de: {}\nAgregamos las Verduras: {}\nAgregamos los Condimientos: {}\n¿Lo hacemos Combo?: {}'.format(self.preparaPan.type, self.agregaCarne.type, self.agregaVerduras.include, self.agregaCondimentos.include,self.hazlaCombo.include).strip()

class Builder:
    def build(self):
        self.preparaPan()
        self.agregaCarne()
        self.agregaVerduras()
        self.agregaCondimentos()
        self.hazlaCombo()

    def preparaPan(self):
        pass

    def agregaCarne(self):
        pass

    def agregaVerduras(self):
        pass

    def agregaCondimentos(self):
        pass

    def hazlaCombo(self):
        pass

    def resultado(self):
        pass

class HamburguesaBuilder(Builder):
    def preparaPan(self):
        pan = Pan()
        pan.type = 'Blanco'
        return pan

    def agregaCarne(self):
        carne = Carne()
        carne.type = 'Res'
        return carne

    def agregaVerduras(self):
        verduras = Verduras()
        verduras.include = 'Lechuga, Tomate, Cebolla'
        return verduras

    def agregaCondimentos(self):
        condimentos = Condimentos()
        condimentos.include = 'Mayonesa, Mostaza, Catsup'
        return condimentos

    def hazlaCombo(self):
        combo = Combo()
        combo.include = 'Si'
        return combo

class HotDogBuilder(Builder):
    def preparaPan(self):
        pan = Pan()
        pan.type = 'Integral'
        return pan

    def agregaCarne(self):
        carne = Carne()
        carne.type = 'Cerdo'
        return carne

    def agregaVerduras(self):
        verduras = Verduras()
        verduras.include = 'Tomate, Cebolla'
        return verduras

    def agregaCondimentos(self):
        condimentos = Condimentos()
        condimentos.include = 'Mayonesa, Mostaza, Catsup, Queso'
        return condimentos

    def hazlaCombo(self):
        combo = Combo()
        combo.include = 'Si'
        return combo

class Director(object):

    __builder = None
    def setBuilder(self, builder):
        self.__builder = builder

    def constructor(self):
        orden = Comida()
        pan = self.__builder.preparaPan()
        orden.set_preparaPan(pan)
        carne = self.__builder.agregaCarne()
        orden.set_agregaCarne(carne)
        verduras = self.__builder.agregaVerduras()
        orden.set_agregaVerduras(verduras)
        condimentos = self.__builder.agregaCondimentos()
        orden.set_agregaCondimentos(condimentos)
        combo = self.__builder.hazlaCombo()
        orden.set_hazlaCombo(combo)
        return orden
class Pan:
    type = None
class Carne:
    type = None
class Verduras:
    include = None
class Condimentos:
    include = None
class Combo:
    include = None

def main():
    hamburguesa = HamburguesaBuilder()
    director = Director()
    director.setBuilder(hamburguesa)
    hamburguesa = director.constructor()
    print('--Hamburguesa--\n', hamburguesa)

    hotdog = HotDogBuilder()
    director = Director()
    director.setBuilder(hotdog)
    hotdog = director.constructor()
    print('\n--HotDog--\n', hotdog)

if __name__ == '__main__':
    main()

    # Si mire jefe, me va a dara para llevar, por favor:
    # Un hocho con todo en combo,
    # Y un hocho sin verduras en combo,
    # Y una burguer vegetariana en combo,
    # Y una burguer sin condimentos en combo,
    # Y una burguer con todo pero sin combo
    # :D