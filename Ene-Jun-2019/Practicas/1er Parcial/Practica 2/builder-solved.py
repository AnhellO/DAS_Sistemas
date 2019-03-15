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

    pan = 'Blanco'
    carne = ''
    verduras = ''
    condimentos = ''
    combo = False

    def preparaPan(self, pan):
        self.pan = pan

    def agregaCarne(self, carne):
        self.carne = carne

    def agregaVerduras(self, verduras):
        self.verduras = verduras

    def agregaCondimentos(self, condimentos):
        self.condimentos = condimentos

    def hazlaCombo(self, combo):
        self.combo = combo

    def __str__(self):
        return """
        Hamburguesa con ->\n
        Pan: {}\n
        Carne: {}\n
        Verduras: {}\n
        Condimentos: {}\n
        Combo: {}\n
        """.format(
            self.pan,
            self.carne,
            self.verduras,
            self.condimentos,
            self.combo
        ).strip()

def main():
    hamburguesa = HamburguesaBuilder()
    hamburguesa.preparaPan('7 granos')
    hamburguesa.agregaCarne('Angus')
    hamburguesa.hazlaCombo(True)
    # director = Director()
    # director.setBuilder(hamburguesa)
    # hamburguesa = director.constructor(type='7 granos')
    print(hamburguesa)

    # hotdog = HotDogBuilder()
    # director = Director()
    # director.setBuilder(hotdog)
    # hotdog = director.constructor()
    # print('\n--HotDog--\n', hotdog)

if __name__ == '__main__':
    main()

    # Si mire jefe, me va a dara para llevar, por favor:
    # Un hocho con todo en combo,
    # Y un hocho sin verduras en combo,
    # Y una burguer vegetariana en combo,
    # Y una burguer sin condimentos en combo,
    # Y una burguer con todo pero sin combo
    # :D
