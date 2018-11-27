from abc import ABC, abstractmethod

class Cerveza():
    def __init__(self, id, name, descripcion, image, abv, ibu, ebc, food_pairing, first_brewed, ph, attenuation_level ):
        self.id = id
        self.name = name
        self.descripcion = descripcion
        self.image = image
        self.abv = abv
        self.ibu = ibu
        self.ebc = ebc
        self.food_pairing = food_pairing
        self.first_brewed = first_brewed
        self.ph = ph
        self.attenuation_level = attenuation_level

    def __str__(self):
        return str(self.id) + '-' + str(self.name) + '-' + str(self.descripcion) + '-' + str(self.image) + '-' + str(self.abv) + '-' + str(self.ibu) + '-' + str(self.ebc) + '-' + str(self.food_pairing) + '-' + str(self.first_brewed) + '-' + str(self.ph) + '-' + str(self.attenuation_level)

class AbstractPunk(ABC):

	@abstractmethod
	def CrearCerveza(self, id):
		#Toma como parámetro id y lo guarda en la BD.
		pass

	@abstractmethod
	def ConsultarCerveza(self, id):
        #regresa un id que este guardado en la db
		pass

class AbstractBeer(ABC):
	@abstractmethod
	def DatosBeer(self, url):
		#esta clase toma una url retorna un objeto de tipo Cerveza
		pass
