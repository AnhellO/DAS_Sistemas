import abc


class Combo(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getDescripcion(self):
        return self.descripcion

class ComboBasico(Combo):
    def getDescripcion(self):
        print('Combo Basico \n' + "Porcion de Papas Fritas, " +
   "salsa, queso amarillo, hamburguesa sencilla, refresco rellenable" )
        print('='*80)

class DecoratorCombo(Combo):
    def __init__(self,combo):
        self.combo = combo

    def getDescripcion(self):
        self.combo.getDescripcion()


class ComboFamiliar(DecoratorCombo):
    def __init__(self,combo):
        super(ComboFamiliar,self).__init__(combo)

    def getDescripcion(self):
        super(ComboFamiliar,self).getDescripcion()
        print('Combo Familiar \n' + 'Piezas de pollo frito, salsa, catchup, gaseosa de naranja,navaja(juguete) ')
        print('='*80)

class ComboEspecial(DecoratorCombo):
    def __init__(self,combo):
        super(ComboEspecial,self).__init__(combo)

    def getDescripcion(self):
        super(ComboEspecial,self).getDescripcion()
        print('Combo Especial \n' + 'Porcion de "Te quiero,siempre estaremos juntos <3" ;-;  ,lechuga,pizzas jawaianas,escopeta,clorox')
        print('='*80)

if __name__ == '__main__':
    combo_familiar_especial = ComboEspecial(ComboFamiliar(ComboBasico() ) )
    combo_familiar_especial.getDescripcion()
    print("-----------------------------------------------------------------")
    combo_familiar_especial = ComboFamiliar(ComboEspecial(ComboBasico() ) )
    combo_familiar_especial.getDescripcion()
