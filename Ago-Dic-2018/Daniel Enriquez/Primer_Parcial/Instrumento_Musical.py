class Instrumento:

  def __init__(self,Instrumento_marca='',instrumento_type='',instrumento_dificultad=''):
      self.instrumento_marca=instrumento_marca
      self.instrumento_type=instrumento_type
      self.instrumento_dificultad=instrumento_dificultad

  def limpiando_instrumento(self):
     print("Limpiando instrumento")

  def afinar(self):
      print("Afinando instrumento")

  def __str__(self):
     return 'Marca: {}\ntipo: {}\ndificultad:'.format(self.instrumento_marca,self.instrumento_type,self.instrumento_dificultad)

class guitarra(Instrumento):

 def __init__(self,Instrumento_marca='',instrumento_type='',instrumento_dificultad='',color='',precio='',marca=''):
     super().__init__(Instrumento_marca,instrumento_type,instrumento_dificultad)
     self.color=color
     self.preico=precio
     self.marca=marca


 def tocar_acorde(self):
     print("estoy tocando")

 def limpiar_maquinaria(self):
     print("estoy limpiando")

 def __str__(self):
    return 'color: {}\nprecio: {}\nmarca: {}'.format(self.color,self.precio,self.marca)
class bateria(Instrumento):

 def __init__(self,Instrumento_marca='',instrumento_type='',instrumento_dificultad='',tamanio='',numeroPlatillos='',bombos=''):
     super().__init__(Instrumento_marca,instrumento_type,instrumento_dificultad)
     self.tamanio=tamanio
     self.numeroPLatillos=numeroPlatillos
     self.bombos=bombos


 def tocar_tarola(self):
     print("estoy tocando tarola")

 def sonar_platillo(self):
     print("estoy sonando platillo")

 def __str__(self):
    return 'tamanio: {}\nnumeroPlatillos: {}\nbombos: {}'.format(self.tamanio,self.numeroPlatillos,self.bombos)


if __name__ == '__main__': #Doy los datos de las distintas clases e imprimo para verificar
    guit = guitarra('Gibson', 'cuerdas', 'dificil', 'azul', '1200', 'fender')
    print(git)
    bat = Bateria('Tama', 'percusion', 'medio', 'mediana', 5, 2)
    print(bat)
