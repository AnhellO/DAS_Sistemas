import abc

class InterfaceStrategy(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def authenticate(self):
        pass
    
class BasicAuthConcreteStrategy(InterfaceStrategy):
    def __init__(self, usr, passwd):
        self.user = usr
        self.password = passwd
    
    def authenticate(self):
        return f'### Authenticated with Basic Auth\n\tUser: {self.user}\n\tPass: {self.password}'

class OauthAuthConcreteStrategy(InterfaceStrategy):
    credefault = {
            "access_token": "una cadena muy larga",
            "token_type": "Bearer",
            "expires_in": 3600,
            "refresh_token": "una cadena muy larga 2",
            "scope": "readAndWrite"
    }

    def __init__(self, **kargs):
        self.credentials = kargs.get("credentials", self.credefault)
    
    def authenticate(self):
        pass



class ApiKeyConcreteStrategy(InterfaceStrategy):
    def __init__(self, apoi_key):
        self.api_key = api_key
    
    def authenticate(self):
        return f'### Authenticated with API Key\n\tKey: {self.api}'

class AunthContext():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
