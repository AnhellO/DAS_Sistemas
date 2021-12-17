from usuarios import Usuario

class Admin(Usuario):
    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name, last_name, username, email)
        # self.priv = []
        self.privileges = privileges()

    # def show_privileges(self):
    #     print("\nPrivilegios:")
    #     for priv in self.priv:
    #         print(priv)

class privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivilegios:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("Este usuario no tiene privilegios.")