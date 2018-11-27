#Make a class called User. Create two attributes
#called first_name and last_name, and then create
#several other attributes that are typically stored
#in a user profile. Make a method called describe_user()
#that prints a summary of the user’s information. Make
#another method called greet_user() that prints a
#personalized greeting to the user.
#Create several instances representing different users,
#and call both methods for each user.

class user: #creo la clase usuario
    def __init__(self, first_name, last_name, age, sex, civil_status): #doy los atributos
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.civil_status = civil_status

    def describe_user(self): #creo la descripcion la cual nos dara todos los datos organizados
        Date_user = "Name: " + self.first_name + " " + self.last_name + "\nAge: " + self.age + "\nSex: " + self.sex + "\nCivil status: " + self.civil_status
        print(Date_user)

    def greet_user(self):
        print("Bienbenido " + self.first_name + " a un dia mas (°w°)/ !!! ")

User_1 = user('Max', 'Garcia', '22', 'Man', 'Single')
User_1.greet_user()
User_1.describe_user()
print("\n")
User_2 = user('Erika', 'Aleman', '25', 'Woman', 'Married')
User_2.greet_user()
User_2.describe_user()
print("\n")
User_3 = user('Kelpi', 'Kripsto', '22', 'Woman', 'Married')
User_3.greet_user()
User_3.describe_user()
print("\n")
User_4 = user('Victor', 'Monsivais', '23', 'Man', 'Single')
User_4.greet_user()
User_4.describe_user()
