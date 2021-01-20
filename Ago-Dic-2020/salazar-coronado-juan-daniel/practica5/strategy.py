import abc

# Interfaz estrategia
class SortStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def authenticate(self):
        pass

class BasicAuthConcreteStrategy(SortStrategy):
    def __init__(self, usr, passwd):
        self.usr = usr
        self.passwd = passwd

    def authenticate(self):
        return f'### Authenticated with Basic Auth\n\tUser: {self.usr}\n\tPass: {self.passwd}'

class OauthAuthConcreteStrategy(SortStrategy):
    default = {
               "access_token": "una cadena muy larga",
               "token_type": "Bearer",
               "expires_in": 3600,
               "refresh_token": "una cadena muy larga 2",
               "scope": "default"
               }

    def __init__(self, **kwargs):
        self.credenciales = kwargs.get("credentials", self.default)

    def formateo_credenciales(self, credenciales) -> str:
        items = []

        for i,j in credenciales.items():
            if not isinstance(j, int):
                items.append(f'"{i}":"{j}"')
            else:
                items.append(f'"{i}":{j}')
        
        return ",".join(items)
    
    def authenticate(self):
        return f'### Authenticated with OAuth\n\tCredentials: {{{self.formateo_credenciales(self.credenciales)}}}'

class ApiKeyConcreteStrategy(SortStrategy):
    def __init__(self, api_key):
        self.api_key = api_key

    def authenticate(self):
        return f'### Authenticated with API Key\n\tKey: {self.api_key}'

class AuthContext():
    def __init__(self, strategy: SortStrategy = OauthAuthConcreteStrategy()):
        self._strategy = strategy

    def authenticate(self):
        return self._strategy.authenticate()

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy