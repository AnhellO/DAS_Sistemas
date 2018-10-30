class Director:
    __builder = None
    def setBuilder(self, builder):
        self.__builder = builder
    def getOrden(self):
        orden = Orden()
        pan = self.__builder.preparaPan()
        orden.setPan(pan)
        carne = self.__builder.agregaCarne()
        orden.setCarne(carne)
        verduras = self.__builder.agregaVerduras()
        orden.setVerduras(verduras)
        condimentos = self.__builder.agregaCondimentos()
        orden.setCondimentos(condimentos)
        combo = self.__builder.hazlaCombo()
        orden.setCombo(combo)
        return orden
class Orden:
    def __init__(self):
        self.__pan = None
        self.__carne = None
        self.__verduras = None
        self.__condimentos = None
        self.__combo = None

    def setPan(self, pan):
        self.__pan = pan
    def setCarne(self, carne):
        self.__carne = carne
    def setVerduras(self, verduras):
        self.__verduras = verduras
    def setCondimentos(self, condimentos):
        self.__condimentos = condimentos
    def setCombo(self, combo):
        self.__combo = combo
    def caracteristicas(self):
        print ("Pan: %s" % self.__pan.tipo)
        print ("Carne: %s" % self.__carne.porciones)
        print ("Verduras: %s" % self.__verduras.si_no)
        print ("Condimentos: %s" % self.__condimentos.si_no)
        print ("Combo: %s" % self.__combo.si_no)

class Builder:
    def preparaPan(self):pass
    def agregaCarne(self):pass
    def agregaVerduras(self):pass
    def agregaCondimentos(self):pass
    def hazlaCombo(self):pass

class Hocho1Builder(Builder):
    def preparaPan(self):
        pan = Pan()
        pan.tipo = ' Normal '
        return pan

    def agregaCarne(self):
        carne = Carne()
        carne.porciones = ' Si '
        return carne

    def agregaVerduras(self):
        verduras = Verduras()
        verduras.si_no = " Si "
        return verduras

    def agregaCondimentos(self):
        condimentos = Condimentos()
        condimentos.si_no = " Si "
        return condimentos

    def hazlaCombo(self):
        combo = Combo()
        combo.si_no = " Si "
        return combo
class Hocho2Builder(Builder):
    def preparaPan(self):
        pan = Pan()
        pan.tipo = ' Normal '
        return pan

    def agregaCarne(self):
        carne = Carne()
        carne.porciones = ' Si '
        return carne

    def agregaVerduras(self):
        verduras = Verduras()
        verduras.si_no = " No "
        return verduras

    def agregaCondimentos(self):
        condimentos = Condimentos()
        condimentos.si_no = " Si "
        return condimentos

    def hazlaCombo(self):
        combo = Combo()
        combo.si_no = " Si "
        return combo
class Burguer1Builder(Builder):
    def preparaPan(self):
        pan = Pan()
        pan.tipo = ' Integral '
        return pan

    def agregaCarne(self):
        carne = Carne()
        carne.porciones = ' No '
        return carne

    def agregaVerduras(self):
        verduras = Verduras()
        verduras.si_no = " Si "
        return verduras

    def agregaCondimentos(self):
        condimentos = Condimentos()
        condimentos.si_no = " No "
        return condimentos

    def hazlaCombo(self):
        combo = Combo()
        combo.si_no = " Si "
        return combo
class Burguer2Builder(Builder):
    def preparaPan(self):
        pan = Pan()
        pan.tipo = ' Normal '
        return pan

    def agregaCarne(self):
        carne = Carne()
        carne.porciones = ' Si '
        return carne

    def agregaVerduras(self):
        verduras = Verduras()
        verduras.si_no = " Si "
        return verduras

    def agregaCondimentos(self):
        condimentos = Condimentos()
        condimentos.si_no = " No "
        return condimentos

    def hazlaCombo(self):
        combo = Combo()
        combo.si_no = " Si "
        return combo
class Burguer3Builder(Builder):
    def preparaPan(self):
        pan = Pan()
        pan.tipo = ' Normal '
        return pan

    def agregaCarne(self):
        carne = Carne()
        carne.porciones = ' Ninguna '
        return carne

    def agregaVerduras(self):
        verduras = Verduras()
        verduras.si_no = " Si "
        return verduras

    def agregaCondimentos(self):
        condimentos = Condimentos()
        condimentos.si_no = " Si "
        return condimentos

    def hazlaCombo(self):
        combo = Combo()
        combo.si_no = " No "
        return combo
class Pan:
    tipo = None
class Carne:
    porciones = None
class Verduras:
    si_no = None
class Condimentos:
    si_no = None
class Combo:
    si_no = None
def cliente():
    hocho1Builder = Hocho1Builder()
    hocho2Builder = Hocho2Builder()
    burguer1Builder = Burguer1Builder()
    burguer2Builder = Burguer2Builder()
    burguer3Builder = Burguer3Builder()

    director = Director()
    print ("Hocho1: ")
    director.setBuilder(hocho1Builder)
    hocho1 = director.getOrden()
    hocho1.caracteristicas()

    print ("\nHocho2: ")
    director.setBuilder(hocho2Builder)
    hocho2 = director.getOrden()
    hocho2.caracteristicas()

    print ("\nBurguer1: ")
    director.setBuilder(burguer1Builder)
    burguer1 = director.getOrden()
    burguer1.caracteristicas()

    print ("\nBurguer2: ")
    director.setBuilder(burguer2Builder)
    burguer2 = director.getOrden()
    burguer2.caracteristicas()

    print ("\nBurguer3: ")
    director.setBuilder(burguer3Builder)
    burguer3 = director.getOrden()
    burguer3.caracteristicas()

if __name__ == '__main__':
    cliente()
