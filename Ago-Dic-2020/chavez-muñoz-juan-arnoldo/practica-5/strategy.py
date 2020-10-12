from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def auth(self):
        pass

class OauthAuthConcreteStrategy(Authentication):
    credentials = {
            "access_token": "una cadena muy larga",
            "token_type": "Bearer",
            "expires_in": 3600,
            "refresh_token": "una cadena muy larga 2",
            "scope": "default"
        }

    def __init__(self, **kwargs):
        self.credentials = kwargs.get("credentials", self.credentials)

    def create_credentials(self,_credentials:dict):
        keylist = ["access_token","token_type","expires_in","refresh_token","scope"]
        token = _credentials.get(keylist[0])
        token_type = _credentials.get(keylist[1])
        expires_time = _credentials.get(keylist[2])
        token_for_refresh = _credentials.get(keylist[3])
        scope_value = _credentials.get(keylist[4])
        return f'### Authenticated with OAuth\n\tCredentials: {{"access_token":"{token}","token_type":"{token_type}","expires_in":{expires_time},"refresh_token":"{token_for_refresh}","scope":"{scope_value}"}}'

    def auth(self):
        return f"{self.create_credentials(self.credentials)}"

class AuthContext():
    def __init__(self, strategy: Authentication = OauthAuthConcreteStrategy()):
        self.strategy = strategy

    def set_strategy(self, new_strategy: Authentication):
        self.strategy = new_strategy

    def authenticate(self):
        return self.strategy.auth()

class BasicAuthConcreteStrategy(Authentication):
    def __init__(self, usr, passwd):
        self.usuario = usr
        self.password = passwd
    
    def auth(self):
        return f'### Authenticated with Basic Auth\n\tUser: {self.usuario}\n\tPass: {self.password}'

class ApiKeyConcreteStrategy(Authentication):
    def __init__(self, api_key: str):
        self.api_key = api_key
        
    def auth(self):
        return f"### Authenticated with API Key\n\tKey: {self.api_key}"


if __name__ == "__main__":
    context = AuthContext()
    print(context.authenticate()) 
