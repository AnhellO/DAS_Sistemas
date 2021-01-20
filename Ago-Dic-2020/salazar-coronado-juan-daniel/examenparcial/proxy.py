class User:
    def __init__(self, name: str, access_level: int):
        self.name = name
        self.access_level = access_level

class SystemAuthProxy:
    def __init__(self, user, departamento):
        self.user = user
        self.departamento = departamento

    def level_1_tasks(self):
        if self.user.access_level >= 1 and self.user.access_level <= 3:
            return f"User '{self.user.name}' is doing level-1 tasks on system ### {self.departamento} ###"
        return f"ERROR: User '{self.user.name}' is not authorized to do level-1 tasks"
    
    def level_2_tasks(self):
        if self.user.access_level >= 2 and self.user.access_level <= 3:
            return f"User '{self.user.name}' is doing level-2 tasks on system ### {self.departamento} ###"
        return f"ERROR: User '{self.user.name}' is not authorized to do level-2 tasks"

    def level_3_tasks(self):
        if self.user.access_level == 3:
            return f"User '{self.user.name}' is doing level-3 tasks on system ### {self.departamento} ###"
        return f"ERROR: User '{self.user.name}' is not authorized to do level-3 tasks"

