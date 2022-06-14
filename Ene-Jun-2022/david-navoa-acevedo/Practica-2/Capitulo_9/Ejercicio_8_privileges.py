from Ejercicio_7_admin import admin,user

class privileges(admin):
    
    def __init__(self, privileges):
        self.privileges = privileges

privilege = ['add User', 'Delete User', 'Create User', 'Block User']

testPrivileges = privileges(privilege)
#the calls are commented to use this class for other things. If u want to check the uses uncomment the calls
#testPrivileges.show_privileges()