import abc 

class Subject(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def level_1_tasks(self, command):
        pass
    def level_2_tasks(self, command):
        pass
    def level_3_tasks(self, command):
        pass

class SystemAuthProxy(Subject): 
    def __init__(self, user, system):
        self.user = user
        self.system = system

    def level_1_tasks(self):
        if self.user.authorized_level['level_1']:
            return f"User '{self.user.name}' is doing level-1 tasks on system ### {self.system} ###"
        return self.not_authorized(1)

    def level_2_tasks(self):
        if self.user.authorized_level['level_2']:
            return f"User '{self.user.name}' is doing level-2 tasks on system ### {self.system} ###"
        return self.not_authorized(2)

    def level_3_tasks(self):
        if self.user.authorized_level['level_3']:
            return f"User '{self.user.name}' is doing level-3 tasks on system ### {self.system} ###"
        return self.not_authorized(3)

    def not_authorized(self, num):
        return f"ERROR: User '{self.user.name}' is not authorized to do level-{num} tasks"

class User():    
    def __init__(self, name, access_level = 0):
        self.name = name
        self.access_level = access_level
        self.authorized_level = { f"level_{i}": False if self.access_level < i else True for i in range(1,4)}
