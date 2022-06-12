'''Clase que muestra los privilegios de admin'''
class privileges():
    def __init__(self):
        self.privileges = {'Can add post','Can delete post','Can ban user'}

            
    def show_privileges(self):
        print('Privilegios del Admin:')
        for privilegio in self.privileges:
            print('- '+privilegio)
