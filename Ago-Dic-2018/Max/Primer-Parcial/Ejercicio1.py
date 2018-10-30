class Instrument_music:
    def __init__(self, color, precio, tamano):
        self.color = color
        self.precio = precio
        self.tamano = tamano

    def material():
        pass


    def tipo_musica_de_uso():
        pass
#################################################################################################################

class Guitarra(Instrument_music): #heredo a la clase principal Instrument_music a esta clase
    def __init__(self, color, precio, tamano, Numcuerdas, Electrica, Creacion):
        super().__init__(color, precio, tamano) # super.__init__ me ahorra tener qe definir con self los atributos hererados
        self.Numcuerdas = Numcuerdas
        self.Electrica = Electrica
        self.Creacion = Creacion #me refiero a donde fue creada

    def cuerdas(): #tipo de cuerdas que tiene
        return self.cuerda

    def afinacion():
        pass

    def imprimir(self): #metodo para imprimir los dato en orden
        print('Color: {} \nPrecio: {} \nTamaño: {} 	\nNumero de cuerdas: {} \nEs electrica: {} \nDonde fue creada: {}'.format(self.color, self.precio, self.tamano, self.Numcuerdas, self.Electrica, self.Creacion))
#    return color, precio, tamano, Numcuerdas, Electrica, creacion
##############################################################################################################
print('\n')
#################################################################################3##############################
class Bateria(Instrument_music): #heredo al clase principal Instrument_music a esta clase
    def __init__(self, color, precio, tamano, NumTambores, Numdiscos, Creacion):
        super().__init__(color, precio, tamano)
        self.NumTambores = NumTambores
        self.Numdiscos = Numdiscos
        self.Creacion = Creacion

    def tambores():
        return self.Tambores

    def discos():
        return self.Discos

    def imprimir(self): #Metodo para imprimir los datos en orden
        print('\nColor: {} \nPrecio: {} \nTamaño: {} \nNumero de tambores: {} \nNumero de discos: {} \nDonde fue creada: {}'.format(self.color, self.precio, self.tamano, self.NumTambores, self.Numdiscos, self.Creacion))
#    return color, precio, tamano, NumTambores, Numdiscos, creacion
#################################################################################################################

if __name__ == '__main__': #Doy los datos de las distintas clases e imprimo para verificar
    guitarra = Guitarra('Negra', 800, 'mediana', 6, 'No es electrica', 'Mexico')
    guitarra.imprimir()
    bateria = Bateria('Blanca', 1200, 'Grande', 12, 4, 'España')
    bateria.imprimir()
