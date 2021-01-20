import abc
import json

class AuthContext:
	def __init__(self, strategy = None):
		self.set_strategy(strategy)

	def authenticate(self):
		return self.__strategy.authenticate()

	def set_strategy(self, new_strategy):
		if new_strategy == None:
			self.__strategy = DefaultConcreteStrategy()
			return

		self.__strategy = new_strategy


class AuthStrategy(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def authenticate():
		pass

class BasicAuthConcreteStrategy(AuthStrategy):
	def __init__(self, **kargs):
		self.__usr = kargs.get("usr", "")
		self.__passwd = kargs.get("passwd", "")

	def authenticate(self):
		return f'### Authenticated with Basic Auth\n\tUser: {self.__usr}\n\tPass: {self.__passwd}'

class OauthAuthConcreteStrategy(AuthStrategy):
	def __init__(self, **kargs):
		self.__credentials = kargs.get("credentials", "")

	def authenticate(self):
		return f'### Authenticated with OAuth\n\tCredentials: {json.dumps(self.__credentials).replace(": ", ":").replace(", ", ",")}'

class ApiKeyConcreteStrategy(AuthStrategy):
	def __init__(self, **kargs):
		self.__api_key = kargs.get("api_key", "")

	def authenticate(self):
		return f'### Authenticated with API Key\n\tKey: {self.__api_key}'

class DefaultConcreteStrategy(AuthStrategy):
	def authenticate(self):
		return '### Authenticated with OAuth\n\tCredentials: {"access_token":"una cadena muy larga","token_type":"Bearer","expires_in":3600,"refresh_token":"una cadena muy larga 2","scope":"default"}'