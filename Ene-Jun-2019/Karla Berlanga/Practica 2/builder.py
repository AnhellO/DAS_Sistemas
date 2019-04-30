#Producto: Objeto que se ha construido tras el proceso definido por el patron
class Food(object):
    def __init__(self):
        self.typeBread = None
        self.typeMeat = None
        self.vegetables = None
        self.condiments = None
        self.make_combo = None

    def set_typeBread(self, bread):
        self.typeBread = bread

    def set_typeMeat(self, meat):
        self.typeMeat = meat

    def set_vegetables(self, veggies):
        self.vegetables = veggies

    def set_condiments(self, flavoring):
        self.condiments = flavoring

    def set_makeCombo(self, combo):
        self.make_combo = combo

    def __str__(self):
        return "Orden lista... \nPan: {}\nCarne: {}\nVerduras {}\nCondimientos: {}\n¿En combo?: {}".format(self.typeBread.type, self.typeMeat.type, self.vegetables.include, self.condiments.include, self.make_combo.include).strip()


#Builder: Interfaz que permite la creacion del objeto
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

#Concrete builder: Implementacion concreta del builder definida para cada uno de los tipos
#Esta clase construye una hamburguesa vegetariana en combo
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

#Director: Se encarga de construir un objeto utilizando el constructor
class foodBuilderDirector(object):

    __builder = None
    def setBuilder(self, builder):
        self.__builder = builder

    def construct(self):
        order = Food()
        pan = self.__builder.preparaPan()
        order.set_typeBread(pan)
        carne = self.__builder.agregaCarne()
        order.set_typeMeat(carne)
        verduras = self.__builder.agregaVerduras()
        order.set_vegetables(verduras)
        condimentos = self.__builder.agregaCondimentos()
        order.set_condiments(condimentos)
        combo = self.__builder.hazlaCombo()
        order.set_makeCombo(combo)
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
