from abc import ABC, abstractmethod

class ITasks(ABC):

    @abstractmethod
    def level_1_tasks(self):
        pass

    @abstractmethod
    def level_2_tasks(self):
        pass

    @abstractmethod
    def level_3_tasks(self):
        pass

##############

class SystemAuthProxy(ITasks):
    
    def __init__(self, user, sistema):
        self.user = user
        self.sistema = sistema

    def level_1_tasks(self):

        if self.user.access_level >= 1:
            self.user.level_1_tasks()
            return f"User '{self.user.name}' is doing level-1 tasks on system ### {self.sistema} ###"

        return f"ERROR: User '{self.user.name}' is not authorized to do level-1 tasks"

    def level_2_tasks(self):
        
        if self.user.access_level >= 2:
            self.user.level_2_tasks()
            return f"User '{self.user.name}' is doing level-2 tasks on system ### {self.sistema} ###"

        return f"ERROR: User '{self.user.name}' is not authorized to do level-2 tasks"

    def level_3_tasks(self):
        
        if self.user.access_level >= 3:
            self.user.level_1_tasks()
            return f"User '{self.user.name}' is doing level-3 tasks on system ### {self.sistema} ###"

        return f"ERROR: User '{self.user.name}' is not authorized to do level-3 tasks"

class User(ITasks):
    
    def __init__(self, name, access_level):
        self.name = name
        self.access_level = access_level

    def level_1_tasks(self):
        return f"{self.name} hace cosas publicas"

    def level_2_tasks(self):
        return f"{self.name} hace cosas importantes"

    def level_3_tasks(self):
        return f"{self.name} es parte de la elite que controla el mundo"


#######
if __name__ == "__main__":
    usr = User(name='foo', access_level=1)
    proxy = SystemAuthProxy(usr, "Payments")
    print(proxy.level_1_tasks())
    print(proxy.level_2_tasks())
    print(proxy.level_3_tasks())