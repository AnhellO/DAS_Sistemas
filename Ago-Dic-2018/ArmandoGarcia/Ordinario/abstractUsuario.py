from abc import ABC,abstractmethod
class Users():
    def __init__(self,name,email,phone,picture,location):
        self.name=name
        self.email=email
        self.phone=phone
        self.picture=picture
        self.location=location
class AbstracUsers(ABC):
    @abstractmethod
    def get_user(self,url):
        pass
