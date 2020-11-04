from abc import ABC, abstractmethod

#################################################################################################
#										STRATEGY												#
#################################################################################################

class IAutenticaciones(ABC):
    
    @abstractmethod
    def auth(self):
        pass   

###
class BasicAuthConcreteStrategy(IAutenticaciones):

    def __init__(self, **kwargs):
        self.usuario = kwargs.get("usr", "Usuario")
        self.password = kwargs.get("passwd", "1")

    def auth(self):
        return f"### Authenticated with Basic Auth\n\tUser: {self.usuario}\n\tPass: {self.password}"

class OauthAuthConcreteStrategy(IAutenticaciones):

    default = {
               "access_token": "una cadena muy larga",
               "token_type": "Bearer",
               "expires_in": 3600,
               "refresh_token": "una cadena muy larga 2",
               "scope": "default"
               }

    def __init__(self, **kwargs):
        self.cred = kwargs.get("credentials", self.default)

    def cred_formatted(self, cred) -> str:
        items = []

        for k,v in cred.items():
            if not isinstance(v, int):
                items.append(f'"{k}":"{v}"')
            else:
                items.append(f'"{k}":{v}')

        return ",".join(items)

    def auth(self):
        return f"### Authenticated with OAuth\n\tCredentials: {{{self.cred_formatted(self.cred)}}}"

class ApiKeyConcreteStrategy(IAutenticaciones):

    def __init__(self, api_key: str):
        self.api_key = api_key

    def auth(self):
        return f"### Authenticated with API Key\n\tKey: {self.api_key}"

######
class AuthContext():
    
    def __init__(self, strategy: IAutenticaciones = OauthAuthConcreteStrategy()):
        self.strategy = strategy

    def set_strategy(self, new_strategy: IAutenticaciones):
        self.strategy = new_strategy

    def authenticate(self):
        return self.strategy.auth()


###
if __name__ == "__main__":
    context = AuthContext()
    print(context.authenticate())