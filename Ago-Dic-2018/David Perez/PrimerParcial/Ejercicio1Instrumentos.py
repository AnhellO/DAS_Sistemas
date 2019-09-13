class Instrumento:
    def __init__(self, color, tamano, peso,cancionestocadas=0,dificultad=None):
        self.color = color
        self.tamano = tamano
        self.peso = peso
    def __str__(self):
        return 'Color: {} \nTamaño: {} \nPeso: {} \nCanciones Tocadas: {} \nDificultad: {}'.format(self.color,self.tamano,self.peso,self.cancionestocadas,self.dificultad)
    def setcancionestocadas(self,n):
        self.cancionestocadas = n
    def Incrementcanciones(self,n):
        self.cancionestocadas += n
    def setdificultad(self,d):
        self.dificultad = d
    def Dificultad(self,d):
        self.dificultad = d

class Guitarra(Instrumento):
    def __init__(self,color,tamano,peso,cuerdas,tipo,marca,cancionestocadas=0,dificultad=None,cuerdarota=None,npuntillas=0):
        "Constuctor de la Guitarra"
        Instrumento.__init__(self,color,tamano,peso,cancionestocadas=0,dificultad=None)
        self.cuerdas = cuerdas
        self.tipo = tipo
        self.marca = marca
    def setcuerdarota(self,cr):
        self.cuerdarota = cr
    def Cuerdarota(self,cr):
        self.cuerdarota = cr
    def setNPuntillas(self,n):
        self.npuntillas = n
    def NPuntillas(self,n):
        self.npuntillas += n
    def __str__(self):
        return 'Color: {} \nTamaño: {} \nPeso: {} \nCancionesTocadas: {} \nDificultad: {} \nNumero de cuerdas: {} \nTipo: {} \nMarca: {} \nCuerda rota?: {} \nNuevas Puntillas: {}'.format(self.color,self.tamano,self.peso,self.cancionestocadas,self.dificultad,self.cuerdas,self.tipo,self.marca,self.cuerdarota,self.npuntillas)

class Bateria(Instrumento):
    def __init__(self,color,tamano,peso,platillos,pedales,baquetas,cancionestocadas=0,dificultad=None,fallas=None,nbaquetasperdidas=0):
        "Constuctor de la Bateria"
        Instrumento.__init__(self,color,tamano,peso,cancionestocadas=0,dificultad=None)
        self.platillos = platillos
        self.pedales = pedales
        self.baquetas = baquetas
    def setfallas(self,f):
        self.fallas = f
    def Fallas(self,f):
        self.fallas = f
    def setnbaquetasperdidas(self,n):
        self.nbaquetasperdidas = n
    def NBaquetasperdidas(self,n):
        self.nbaquetasperdidas += n
    def __str__(self):
        return 'Color: {} \nTamaño: {} \nPeso: {} \nCancionesTocadas: {} \nDificultad: {} \nNumero de platillos: {} \nNumero de Pedales: {} \nNumero de Baquetas: {} \nFallas?: {} \nNumero de Baquetas Perdidas: {}'.format(self.color,self.tamano,self.peso,self.cancionestocadas,self.dificultad,self.platillos,self.pedales,self.baquetas,self.fallas,self.nbaquetasperdidas)

if __name__ == '__main__':
    guitarra_1 = Guitarra('Rojo','Mediana','5kg','6','Electrica','Guibson')
    guitarra_1.setcancionestocadas(1)
    guitarra_1.Incrementcanciones(2)
    guitarra_1.setdificultad(None)
    guitarra_1.Dificultad(' Bien Dificil ')
    guitarra_1.setcuerdarota(None)
    guitarra_1.Cuerdarota(' Si :c ')
    guitarra_1.setNPuntillas(1)
    guitarra_1.NPuntillas(2)
    print('\n {}'.format(guitarra_1))
    guitarra_2 = Guitarra('Rojo','Mediana','5kg','6','Electroacustica','Gibson')
    guitarra_2.setcancionestocadas(0)
    guitarra_2.setdificultad(None)
    guitarra_2.setcuerdarota(None)
    guitarra_2.setNPuntillas(0)
    print('\n {}'.format(guitarra_2))
    guitarra_3 = Guitarra('Verde','Grande','10kg','12','Acustica','Guitarhero')
    guitarra_3.setcancionestocadas(0)
    guitarra_3.setdificultad(None)
    guitarra_3.setcuerdarota(None)
    guitarra_3.setNPuntillas(1)
    guitarra_3.NPuntillas(3)
    print('\n {}'.format(guitarra_3))
    guitarra_4 = Guitarra('Morada','Mediana','5kg','12','Electrica','Lespaul')
    guitarra_4.setcancionestocadas(1)
    guitarra_4.setdificultad(None)
    guitarra_4.setcuerdarota(None)
    guitarra_4.setNPuntillas(1)
    guitarra_4.Incrementcanciones(1)
    guitarra_4.NPuntillas(3)
    print('\n {}'.format(guitarra_4))
    guitarra_5 = Guitarra('Morada','Chica','1kg','6','Electrica','Gibson')
    guitarra_5.setdificultad(None)
    guitarra_5.setNPuntillas(1)
    guitarra_5.NPuntillas(3)
    guitarra_5.setcancionestocadas(1)
    guitarra_5.Incrementcanciones(1)
    guitarra_5.setcuerdarota(1)
    guitarra_5.Cuerdarota(' seis rotas :c ')
    print('\n {}'.format(guitarra_5))

    bateria_1 = Bateria('Ocre','6 Piezas','30kg','2','1','2')
    bateria_1.setcancionestocadas(1)
    bateria_1.Incrementcanciones(2)
    bateria_1.setdificultad(None)
    bateria_1.Dificultad(' Bien Dificil ')
    bateria_1.setfallas(None)
    bateria_1.Fallas(' Se raspó un platillo :c ')
    bateria_1.setnbaquetasperdidas(1)
    bateria_1.NBaquetasperdidas(2)
    print('\n {}'.format(bateria_1))
    bateria_2 = Bateria('Cromo','8 Piezas','60kg','3','2','2')
    bateria_2.setcancionestocadas(0)
    bateria_2.setdificultad(None)
    bateria_2.setfallas(None)
    bateria_2.setnbaquetasperdidas(0)
    print('\n {}'.format(bateria_2))
    bateria_3 = Bateria('Ocre','12 Piezas','60kg','3','2','4')
    bateria_3.setcancionestocadas(0)
    bateria_3.setdificultad(None)
    bateria_3.setfallas(None)
    bateria_3.setnbaquetasperdidas(1)
    bateria_3.NBaquetasperdidas(3)
    print('\n {}'.format(bateria_3))
    bateria_4 = Bateria('Negro','6 Piezas','30kg','3','2','4')
    bateria_4.setcancionestocadas(1)
    bateria_4.setdificultad(None)
    bateria_4.setfallas(None)
    bateria_4.setnbaquetasperdidas(1)
    bateria_4.Incrementcanciones(1)
    bateria_4.NBaquetasperdidas(3)
    print('\n {}'.format(bateria_4))
    bateria_5 = Bateria('Custom','15 Piezas','70kg','4','2','6')
    bateria_5.setdificultad(None)
    bateria_5.setnbaquetasperdidas(1)
    bateria_5.NBaquetasperdidas(3)
    bateria_5.setcancionestocadas(1)
    bateria_5.Incrementcanciones(1)
    bateria_5.setfallas(1)
    bateria_5.Fallas(' Ya bailaron los pedales :c ')
    print('\n {}'.format(bateria_5))
