#
class Comida(object):
    def __init__(self):
        self.tipopan = None
        self.tipocarne = None
        self.vegetales = None
        self.condimentos = None
        self.hazcombo = None

    def set_tipopan(self, pan):
        self.typeBread = pan

    def set_tipocarne(self, carne):
        self.typeMeat = carne

    def set_vegetales(self, vegetales):
        self.vegetales = vegetales

    def set_condimentos(self, flavoring):
        self.condiments = flavoring

    def set_hazCombo(self, combo):
        self.make_combo = combo

    def __str__(self):
        return "Salen jochos... \nPan: {}\nCarne: {}\nVerduras {}\nCondimientos: {}\n¿combo?: {}".format(self.tipopan.type, self.tipocarne.type, self.vegetales.include, self.condimentos.include, self.haz_combo.include).strip()


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

    def result(self):
        pass


class hamburguerBuilder(Builder):

    def preparaPan(self):
        pan = Bread()
        pan.type = 'Normal'
        return pan

    def agregaCarne(self):
        carne = Meat()
        carne.type = 'Pollo'
        return carne

    def agregaVerduras(self):
        verduras = Vegetables()
        verduras.include = 'Si'
        return verduras

    def agregaCondimentos(self):
        condimentos = Condiments()
        condimentos.include = 'Si'
        return condimentos

    def hazlaCombo(self):
        combo = Combo()
        combo.include = 'Si'
        return combo

class hotdogBuilder(Builder):

    def preparaPan(self):
        pan = Bread()
        pan.type = 'Normal'
        return pan

    def agregaCarne(self):
        carne = Meat()
        carne.type = 'Salchicha de Pavo'
        return carne

    def agregaVerduras(self):
        verduras = Vegetables()
        verduras.include = 'Si'
        return verduras

    def agregaCondimentos(self):
        condimentos = Condiments()
        condimentos.include = 'Si'
        return condimentos

    def hazlaCombo(self):
        combo = Combo()
        combo.include = 'Si'
        return combo

class foodBuilderDirector(object):

    __builder = None
    def setBuilder(self, builder):
        self.__builder = builder

    def construct(self):
        order = Comida()
        pan = self.__builder.preparaPan()
        order.set_tipopan(pan)
        carne = self.__builder.agregaCarne()
        order.set_tipocarne(carne)
        verduras = self.__builder.agregaVerduras()
        order.set_vegetales(verduras)
        condimentos = self.__builder.agregaCondimentos()
        order.set_condimentos(condimentos)
        combo = self.__builder.hazlaCombo()
        order.set_hazCombo(combo)
        return order

class Bread:
    type = None
class Meat:
    type = None
class Vegetables:
    include = None
class Condiments:
    include = None
class Combo:
    include = None

if __name__ == '__main__':
    hamburguesa = hamburguerBuilder()
    director = foodBuilderDirector()
    director.setBuilder(hamburguesa)
    hamburguesa = director.construct()
    print("Hamburguesa")
    print(hamburguesa)

    hotdog = hotdogBuilder()
    director = foodBuilderDirector()
    director.setBuilder(hotdog)
    hotdog = director.construct()
    print("\nHot dog")
    print(hotdog)


    # Si mire jefe, me va a dara para llevar, por favor:
    # Un hocho con todo en combo,
    # Y un hocho sin verduras en combo,
    # Y una burguer vegetariana en combo,
    # Y una burguer sin condimentos en combo,
    # Y una burguer con todo pero sin combo
    # :D