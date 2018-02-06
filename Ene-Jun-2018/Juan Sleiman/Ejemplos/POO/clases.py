class Guitarra():

    #el método __init__ es como el contructor
    def __init__(self, madera, color, orientacion):
        #self es como el this. de java
        self.madera = madera
        self.color = color
        self.orientacion = orientacion
        self.cuerdas = cuerdas

    def get_num_cuerdas(self):
        return self.cuerdas

    def imprime_atributos(self):
        print('Cuerdas: {}\nMadera: {}\nColor: {}\nOrientación: {}')

guitarra = Guitarra('maple', 'negro', 'diestro', 7)
guitarra.imprime_atributos()
