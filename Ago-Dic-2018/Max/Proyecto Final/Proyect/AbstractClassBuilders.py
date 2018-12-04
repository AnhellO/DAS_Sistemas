from abc import ABC, abstractmethod
#Autor y programador - "Maximiliano García De Santiago"
class RecetaTaco():
    def __init__(self, Id, Nombre_Receta, Contribuidores, Sub_receta_1, Sub_receta_2, Sub_receta_3, Sub_receta_4):
        self.Id = Id
        self.Nombre_Receta = Nombre_Receta
        self.Contribuidores = Contribuidores
        self.Sub_receta_1 = Sub_receta_1
        self.Sub_receta_2 = Sub_receta_2
        self.Sub_receta_3 = Sub_receta_3
        self.Sub_receta_4 = Sub_receta_4

    def __str__(self):
        return str(self.Id) + ' - ' + str(self.Nombre_Receta) + ' - ' + str(self.Contribuidores) + ' - ' + str(self.Sub_receta_1) + ' - ' + str(self.Sub_receta_2) + ' - ' + str(self.Sub_receta_3) + ' - ' + str(self.Sub_receta_4)

class Cliente():
    def __init__(self, Id, Nombre, Genero, Email, Edad):
        self.Id = Id
        self.Nombre = Nombre
        self.Genero = Genero
        self.Email = Email
        self.Edad = Edad

    def __str__(self):
        return str(self.Id) + ' - ' + str(self.Nombre) + ' - ' + str(self.Genero) + ' - ' + str(self.Email) + ' - ' + str(self.Edad)

class Pedido():
    def __init__(self, Id, Nombre_Receta, Nombre_Cliente):
        self.Id = Id
        self.Nombre_Receta = Nombre_Receta
        self.Nombre_Cliente = Nombre_Cliente

    def __str__(self):
        return str(self.Id) + ' - ' + str(self.Nombre_Receta) + ' - ' + str(self.Nombre_Cliente)


class AbstractProyectReceta(ABC):

	@abstractmethod
	def CrearReceta(self, Id):
		#Toma como parámetro id y lo guarda en la BD con sus atributos.
		pass

	@abstractmethod
	def ConsultarReceta(self, Id):
        #regresa los datos que este guardado en la db al recivir una Id
		pass

	@abstractmethod
	def BorrarReceta(self, Id):
        #regresa los datos que este guardado en la db al recivir una Id
		pass

class AbstractProyectClient(ABC):

	@abstractmethod
	def CrearCliente(self, Cliente):
		#Toma como parámetro id y lo guarda en la BD con sus atributos.
		pass

	@abstractmethod
	def ConsultarCliente(self, Id):
        #regresa los datos que este guardado en la db al recivir una Id
		pass

	@abstractmethod
	def BorrarCliente(self, Id):
        #regresa los datos que este guardado en la db al recivir una Id
		pass

class AbstractProyectPedido(ABC):

	@abstractmethod
	def CrearPedido(self, Id):
		#Toma como parámetro id y lo guarda en la BD con sus atributos.
		pass

	@abstractmethod
	def ConsultarPedido(self, Id):
        #regresa los datos que este guardado en la db al recivir una Id
		pass

	@abstractmethod
	def BorrarPedido(self, Id):
        #regresa los datos que este guardado en la db al recivir una Id
		pass

	@abstractmethod
	def ConsultarCliente(self, Id):
        #regresa los datos que este guardado en la db al recivir una Id
		pass

	@abstractmethod
	def ConsultarReceta(self, Id):
        #regresa los datos que este guardado en la db al recivir una Id
		pass

class AbstractReceta(ABC):
	@abstractmethod
	def DatosReceta(self, url, Id):
		#esta clase toma una url y una id retorna un objeto de tipo Receta
		pass

class AbstractCliente(ABC):
	@abstractmethod
	def DatosCliente(self, url, Id):
		#esta clase toma una url retorna un objeto de tipo Cliente
		pass

class AbstractPedido(ABC):
	@abstractmethod
	def DatosPedido(self, IdPedido, IdReceta, IdCliente):
		#esta clase toma una url retorna un objeto de tipo Cliente
		pass
