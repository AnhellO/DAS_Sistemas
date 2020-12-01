from abc import ABC, abstractmethod

class interface_authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass

class BasicAuthConcreteStrategy(interface_authentication):
    
    def __init__(self,usr : str, passwd:str):
        self.user = usr
        self.password = passwd
    
    def authenticate(self):
        return f'### Authenticated with Basic Auth\n\tUser: {self.user}\n\tPass: {self.password}'


class OauthAuthConcreteStrategy(interface_authentication):
    
    defaultdict = {
        "access_token": "una cadena muy larga",
        "token_type": "Bearer",
        "expires_in": 3600,
        "refresh_token": "una cadena muy larga 2",
        "scope": "default"
    }
    def __init__(self,**kwargs):
        self.credentials = kwargs.get("credentials",self.defaultdict)

    def prepare_credentials(self,_credentials:dict):
        keylist = ["access_token","token_type","expires_in","refresh_token","scope"]
        token = _credentials.get(keylist[0])
        token_type = _credentials.get(keylist[1])
        expires_time = _credentials.get(keylist[2])
        token_for_refresh = _credentials.get(keylist[3])
        scope_value = _credentials.get(keylist[4])
        return f'### Authenticated with OAuth\n\tCredentials: {{"access_token":"{token}","token_type":"{token_type}","expires_in":{expires_time},"refresh_token":"{token_for_refresh}","scope":"{scope_value}"}}'

    def authenticate(self):
        return f"{self.prepare_credentials(self.credentials)}"
        
class ApiKeyConcreteStrategy(interface_authentication):
    
    def __init__(self, api_key: str):
        self.api_key = api_key

    def authenticate(self):
        return f"### Authenticated with API Key\n\tKey: {self.api_key}"
    pass

class AuthContext(interface_authentication):
    def __init__(self, _strategy:interface_authentication = OauthAuthConcreteStrategy()):
        self.strategy = _strategy
    
    def set_strategy(self, _strat_to_set:interface_authentication):
        self.strategy =  _strat_to_set
        
    def authenticate(self):
        return self.strategy.authenticate()

    pass    


def main():
    cred = {
            "access_token": "una cadena muy larga",
            "token_type": "Bearer",
            "expires_in": 3600,
            "refresh_token": "una cadena muy larga 2",
            "scope": "readAndWrite"
        }
    context2 = AuthContext(OauthAuthConcreteStrategy(credentials=cred))
    print(context2.authenticate())
    context = AuthContext()
    print(context.authenticate())
    

if __name__ == "__main__":
    main()



