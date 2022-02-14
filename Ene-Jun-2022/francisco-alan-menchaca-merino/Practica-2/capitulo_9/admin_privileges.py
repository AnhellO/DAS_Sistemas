from latest_user import User


class Admin(User):
    def __init__(self, first_name, last_name, country, email):
        super().__init__(first_name, last_name, country, email)
        self.admin_privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = []

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
