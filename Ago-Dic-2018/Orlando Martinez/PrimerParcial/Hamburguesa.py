class Comida(object):
    def __init__(self, preparaPan='', agregaCarne='', agregaVerduras='',agregaCondimentos='',hazlaCombo=''):
        self.preparaPan=preparaPan
        self.agregaCarne=agregaCarne
        self.agregaVerduras=agregaVerduras
        self.agregaCondimentos=agregaCondimentos
        self.hazlaCombo=hazlaCombo
    def __str__(self):
        return ('{} \n{} \n{}\n{} \n{}'.format(self.preparaPan, self.agregaCarne, self.agregaVerduras,self.agregaCondimentos,self.hazlaCombo))



class Builder:
    #def build(self):
    #    self.preparaPan()
    #    self.agregaCarne()
    #    self.agregaVerduras()
    #    self.agregaCondimentos()
    #    self.hazlaCombo()


    def set_preparaPan(self,value):
        pass

    def set_agregaCarne(self,value):
        pass

    def set_agregaVerduras(self,value):
        pass

    def set_agregaCondimentos(self,value):
        pass

    def set_hazlaCombo(self,value):
        pass

    def get_resultado(self):
        pass

class ComidaBuilder(Builder):
    def __init__(self):
        self.comida=Comida()
    def set_preparaPan(self,value):
        self.comida.preparaPan=value

    def set_agregaCarne(self,value):
        self.comida.agregaCarne=value

    def set_agregaVerduras(self,value):
        self.comida.agregaVerduras=value

    def set_agregaCondimentos(self,value):
        self.comida.agregaCondimentos=value

    def set_hazlaCombo(self,value):
        self.comida.hazlaCombo=value

    def get_resultado(self):
        return self.comida

#if __name__ == '__main__':
class Director(object):
    def constructor():
        builder=ComidaBuilder()
        builder.set_preparaPan('Hambuerguesa')
        builder.set_agregaCarne('vegetariana')
        builder.set_agregaVerduras('Con verduras')
        builder.set_agregaCondimentos('sin condimentos')
        builder.set_hazlaCombo('en combo')
        return builder.get_resultado()
comida=Director.constructor()
print(comida)
    # Si mire jefe, me va a dara para llevar, por favor:
    # Un hocho con todo en combo,
    # Y un hocho sin verduras en combo,
    # Y una burguer vegetariana en combo,
    # Y una burguer sin condimentos en combo,
    # Y una burguer con todo pero sin combo
    # :D
