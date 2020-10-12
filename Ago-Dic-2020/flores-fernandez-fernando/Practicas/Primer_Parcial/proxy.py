from abc import ABC, abstractmethod
class User():
    def __init__(self,name,access_level):
        self._name = name
        self._access_level = access_level 
    
    def get_name(self):
        return self._name
    
    def get_access_level(self):
        return self._access_level

class InterfaceProxy(ABC):
    @abstractmethod    
    def level_1_tasks(self):
        pass
   
    @abstractmethod    
    def level_2_tasks(self):
        pass
    
    @abstractmethod    
    def level_3_tasks(self):
        pass

class SystemAuthProxy(InterfaceProxy):
    def __init__(self,user,department):
        self._user = user
        self._department = department 
    
    def get_department(self):
        return self._department
    
    def level_1_tasks(self):
        if (self._user.get_access_level() > 0):
            return f"User '{self._user.get_name()}' is doing level-1 tasks on system ### {self.get_department()} ###" 
        return f"ERROR: User '{self._user.get_name()}' is not authorized to do level-1 tasks"

    def level_2_tasks(self):
        if (self._user.get_access_level() > 1):
            return f"User '{self._user.get_name()}' is doing level-2 tasks on system ### {self.get_department()} ###" 
        return f"ERROR: User '{self._user.get_name()}' is not authorized to do level-2 tasks"

   
    def level_3_tasks(self):
        if (self._user.get_access_level()  > 2):
            return f"User '{self._user.get_name()}' is doing level-3 tasks on system ### {self.get_department()} ###" 
        return f"ERROR: User '{self._user.get_name()}' is not authorized to do level-3 tasks"

    
def main():
    usr = User(name='bar', access_level=2)
    proxy = SystemAuthProxy(usr, "IT")

    stile =  proxy.level_1_tasks()
    print(stile)

if __name__ == "__main__":
    main()