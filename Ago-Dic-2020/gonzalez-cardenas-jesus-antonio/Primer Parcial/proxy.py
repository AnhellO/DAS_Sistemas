from abc import ABCMeta, abstractmethod

class User():
    def __init__(self,name:str,access_level:int):
        self._name = name
        self._level = access_level
    
    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._level


class proxy(metaclass=ABCMeta):

    @abstractmethod
    def level_1_tasks(self):
        pass
    @abstractmethod
    def level_2_tasks(self):
        pass
    @abstractmethod
    def level_3_tasks(self):
        pass



class SystemAuthProxy(proxy):
    def __init__(self,usr:User,role:str):
        self.user = usr
        self._role = role
        pass

    def level_1_tasks(self):
        if (self.user.get_access_level() >= 1):
            return f"User '{self.user.get_name()}' is doing level-1 tasks on system ### {self._role} ###"
            
    
    def level_2_tasks(self):
        if (self.user.get_access_level() >= 2):
            return f"User '{self.user.get_name()}' is doing level-2 tasks on system ### {self._role} ###"
        else:
            return f"ERROR: User '{self.user.get_name()}' is not authorized to do level-2 tasks"
            

    def level_3_tasks(self):
        if (self.user.get_access_level() == 3):
            return f"User '{self.user.get_name()}' is doing level-3 tasks on system ### {self._role} ###"
        else:
            return f"ERROR: User '{self.user.get_name()}' is not authorized to do level-3 tasks"
            


def main():
    usr = User(name='foo', access_level=2)
    proxy = SystemAuthProxy(usr, 'IT')
    print(proxy.level_1_tasks())
    print(proxy.level_2_tasks())
    print(proxy.level_3_tasks())

if __name__ == "__main__":
    main()

