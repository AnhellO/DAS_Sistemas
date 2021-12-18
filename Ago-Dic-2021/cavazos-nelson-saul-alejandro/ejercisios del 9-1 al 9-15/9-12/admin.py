from usuario import Usuario

class privilegios():
    def __init__(self) :
        self.privilegio=["puede agregar publicación", "puede eliminar publicación", "puede prohibir usuario","ser admin"]
    def show_privileges (self):
        print(' 1 '+self.privilegio[0]+'\n 2 '+self.privilegio[1] +'\n 3 '+self.privilegio[2] +'\n 4 '+self.privilegio[3])


class Admin(Usuario):
    def __init__(self, first_name, last_name, nacionalidad, edad, sexo):
        super().__init__(first_name, last_name, nacionalidad, edad, sexo)
        self.adimin=privilegios()
           