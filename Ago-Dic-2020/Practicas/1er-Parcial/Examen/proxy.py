import abc

class User:
    def __init__(self, **kwargs):
        self._name = kwargs.get('name', 'Anonymous')
        self._access_level = kwargs.get('access_level', 1)

    def get_name(self):
        return self._name
    
    def get_access_level(self):
        return self._access_level
    
    def __str__(self):
        return f"Name: {self._name}, Level: {self._access_level}"

class Subject:
    @abc.abstractmethod
    def level_1_tasks(self) -> str:
        pass
    
    @abc.abstractmethod
    def level_2_tasks(self) -> str:
        pass
    
    @abc.abstractmethod
    def level_3_tasks(self) -> str:
        pass

class SystemSubject(Subject):
    def __init__(self, name: str, user: User):
        self._name = name
        self._user = user

    def level_1_tasks(self) -> str:
        return f"User '{self._user.get_name()}' is doing level-1 tasks on system {self._name}"

    def level_2_tasks(self) -> str:
        return f"User '{self._user.get_name()}' is doing level-2 tasks on system {self._name}"

    def level_3_tasks(self) -> str:
        return f"User '{self._user.get_name()}' is doing level-3 tasks on system {self._name}"

class SystemAuthProxy(Subject):
    def __init__(self, user: User, system: str):
        self._user = user
        self._system = SystemSubject(f"### {system} ###", self._user)

    def level_1_tasks(self) -> str:
        if self._user.get_access_level() in [1, 2, 3]:
            return self._system.level_1_tasks()
        
        return self.__do_common_message(1)

    def level_2_tasks(self) -> str:
        if self._user.get_access_level() in [2, 3]:
            return self._system.level_2_tasks()

        return self.__do_common_message(2)

    def level_3_tasks(self) -> str:
        if self._user.get_access_level() == 3:
            return self._system.level_3_tasks()
        
        return self.__do_common_message(3)
    
    def __do_common_message(self, level: int):
        return f"ERROR: User '{self._user.get_name()}' is not authorized to do level-{level} tasks"