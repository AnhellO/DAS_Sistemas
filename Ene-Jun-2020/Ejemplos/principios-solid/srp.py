import random
import json
import abc
from faker import Faker

class DBConexion(object):
	"""docstring for DBConexion"""
	def __init__(self, motor_db):
		self.motor_db = motor_db

	def inicia_conexion(self):
		if self.motor_db and self.test_conexion():
			print('Ya me conecté! :D')
			return True

		self.inicia_conexion()
		
	def test_conexion(self):
		return random.choice([True, False])


class DBFetcher(object):
	"""docstring for DBFetcher"""
	def __init__(self, conexion: DBConexion):
		self.conexion = conexion
		self.fake = Faker()

	def select_data(self, query: str):
		data = {
			'id': random.randrange(100),
			'name': self.fake.name(),
			'address': self.fake.address()
		} # Supongamos que esto fue nuestro queryto a la DB

		print(f'Ya saqué la data!\nQuery: {query}')
		return data

class DataConverter(metaclass=abc.ABCMeta):
	"""docstring for DataConverter"""

	def set_data(self, data):
		self.data = data
		return self

	@abc.abstractmethod
	def convierte_data(self):
		pass

class JsonConverter(DataConverter):
	"""docstring for JsonConverter"""
	def convierte_data(self):
		return json.dumps(self.data, indent=2)


conn = DBConexion('mysql')
resultado_conn = conn.inicia_conexion()

if resultado_conn == True:
	fetcher = DBFetcher(conn)
	data = fetcher.select_data('SELECT * FROM my_table;')
	convertidor = JsonConverter()
	data_convertida = convertidor.set_data(data).convierte_data()
	print(data_convertida)







