class Director():
    """Director"""
    def __init__(self, builder):
        self._builder = builder

    def construct_hamburguer_hotdog(self, comida, carne, verduras, condimentos, combo):
        """Métodos ejecutados al llamar el construct_hamburguer_hotdog, si el comensal
        quiere cierto ingrediente en su hamburguesa/hot dog, ingresa el 1, si no, cero"""
        if comida == 'hamburguer':  # Si queremos preparar una hamburguesa
            self._builder.create_new_hamburguer()
        elif comida == 'hotdog':
            self._builder.create_new_hotdog()  # Si queremos preparar un hot dog
        self._builder.preparaPan()  # todas las hamburguesas y hot dogs llevan pan
        if carne == 1:
            self._builder.agregaCarne()
        if verduras == 1:
            self._builder.agregaVerduras()
        if condimentos == 1:
            self._builder.agregaCondimentos()
        if combo == 1:
            self._builder.hazlaCombo()

    def get_food(self):
        """Regresa todos los ingredientes que llevará el hotdog/hamburguesa"""
        return self._builder.food

class Builder():
    def __init__(self):
        """Creamos variable food"""
        self.food = None

    def create_new_hamburguer(self):
        """Escogemos la clase Food"""
        self.food = Food()

    def create_new_hotdog(self):
        """Escogemos la clase Food"""
        self.food = Food()

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


class Hamburguesa(Builder):
    def preparaPan(self):
        self.food.pan = " - Preparamamos el pan!"

    def agregaCarne(self):
        self.food.carne = " - Agregamos la carne!"

    def agregaVerduras(self):
        self.food.verduras = " - Agregamos las verduras!"

    def agregaCondimentos(self):
        self.food.condimentos = " - Agregamos los condimentos!"

    def hazlaCombo(self):
        self.food.combo = " - La hacemos combo!"

class HotDog(Builder):
    def preparaPan(self):
        self.food.pan = " - Preparamamos el pan!"

    def agregaCarne(self):
        self.food.carne = " - Agregamos la carne!"

    def agregaVerduras(self):
        self.food.verduras = " - Agregamos las verduras!"

    def agregaCondimentos(self):
        self.food.condimentos = " - Agregamos los condimentos!"

    def hazlaCombo(self):
        self.food.combo = " - La hacemos combo!"

class Food():
    """Product"""
    def __init__(self):
        """Inicializamos los ingredientes"""
        self.carne = " - Sin carne"
        self.verduras = " - Sin verduras"
        self.condimentos = " - Sin condimentos"
        self.combo = " - Sin combo"

    def __str__(self):
        """Regresamos los ingredientes"""
        return '{}\n{}\n{}\n{}\n{}'.format(self.pan, self.carne, self.verduras, self.condimentos, self.combo)

# El patrón builder es utilizado para crear una variedad de objetos complejos desde un objeto fuente

if __name__ == '__main__':
    print("HOTDOG CON TODO EN COMBO")  # Un hocho con todo en combo
    builder1 = HotDog()
    director1 = Director(builder1)
    director1.construct_hamburguer_hotdog('hotdog',1,1,1,1)
    hotdogCompletoCombo = director1.get_food()
    print(hotdogCompletoCombo)

    print("\nHOTDOG SIN VERDURAS EN COMBO")  # Y un hocho sin verduras en combo
    builder2 = HotDog()
    director2 = Director(builder2)
    director2.construct_hamburguer_hotdog('hotdog',1,0,1,1)
    hotdogSinVerdurasCombo = director2.get_food()
    print(hotdogSinVerdurasCombo)

    print("\nHAMBURGUESA VEGETARIANA EN COMBO")  # Y una burguer vegetariana en combo
    builder3 = Hamburguesa()
    director3 = Director(builder3)
    director3.construct_hamburguer_hotdog('hamburguer',0,1,1,1)
    hamburguesaVegetarianaCombo = director3.get_food()
    print(hamburguesaVegetarianaCombo)

    print("\nHAMBURGUESA SIN CONDIMENTOS EN COMBO")  # Y una burguer sin condimentos en combo
    builder4 = Hamburguesa()
    director4 = Director(builder4)
    director4.construct_hamburguer_hotdog('hamburguer',1,1,0,1)
    hamburguesaSinCondimentosCombo = director4.get_food()
    print(hamburguesaSinCondimentosCombo)

    print("\nHAMBURGUESA CON TODO PERO SIN COMBO")  # Y una burguer con todo pero sin combo
    builder5 = Hamburguesa()
    director5 = Director(builder5)
    director5.construct_hamburguer_hotdog('hamburguer',1,1,1,0)
    hamburguesaConTodoSinCombo = director5.get_food()
    print(hamburguesaConTodoSinCombo)
