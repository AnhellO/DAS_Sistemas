class User():

    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
 

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
      

    def greet_user(self):
        print(f"\nBienvenid@, {self.username}!")

ana = User('ana', 'cas', 'a_cas', 'ana@example.com')
ana.describe_user()
ana.greet_user()

maria = User('maria', 'torres', 'maria_cas', 'maria@example.com')
maria.describe_user()
maria.greet_user()
    