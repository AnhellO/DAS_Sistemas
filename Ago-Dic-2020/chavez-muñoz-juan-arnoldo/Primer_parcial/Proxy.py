class User():
    def __init__(self, name, access_level):
        self.name = name                 #str
        self.access_level = access_level #int

class SystemAuthProxy():
    def __init__(self, user, system_name):
        self.user = user
        self.system_name = system_name                 

    def level_1_tasks(self):
        usr = User(name = 'foo', access_level = 1)
        proxy = SystemAuthProxy(usr, "Payments")
        if(self.user.access_level >= 1):
            return f"User '{usr.name}' is doing level-1 tasks on system ### {proxy.system_name} ###"
        # if(usr.access_level >= 2):
        #     return f"User '{usr.name}' is doing level-2 tasks on system ### {proxy.system_name} ###"
        # else:
        #     return f"ERROR: User '{usr.name}' is not authorized to do level-2 tasks"

    def level_2_tasks(self):
        usr = User(name = 'bar', access_level = 2)
        proxy = SystemAuthProxy(usr, "IT")
        if(self.user.access_level >= 2):
            return f"User '{usr.name}' is doing level-2 tasks on system ### {proxy.system_name} ###"
        return f"ERROR: User '{usr.name}' is not authorized to do level-2 tasks"

        # if(usr.access_level == 3):
        #     return f"User '{usr.name}' is doing level-3 tasks on system ### {proxy.system_name} ###"
        # else:
        #     return f"ERROR: User '{usr.name}' is not authorized to do level-3 tasks"

    def level_3_tasks(self):
        usr = User(name = 'baz', access_level = 3)
        proxy = SystemAuthProxy(usr, "Sales")
        if(self.user.access_level == 3):
            return f"User '{usr.name}' is doing level-3 tasks on system ### {proxy.system_name} ###"
        else:
            return f"ERROR: User '{usr.name}' is not authorized to do level-3 tasks"



if __name__ == "__main__":
    #user = User(name=)
    pass