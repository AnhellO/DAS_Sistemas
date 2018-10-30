class User():

    def __init__(self, first_name, last_name, phone, email, twitter):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.twitter = twitter

    def describe_user(self):
        print("The user first name is: {} \nThe user last name is: {} \nThe user phone is: {} \nThe user email is: {} \nThe user Twitter is: {}".format(self.first_name,self.last_name,self.phone,self.email,self.twitter))

    def greet_user(self):
        print("Hey", self.first_name, "have a nice day!")

user_1 = User("Jonathan","Castillo", 5559864, "jonatillo@gmail.com", "@Jonatillo")
user_2 = User("Terry","Flores", 5552148, "Teero1@gmail.com", "@Ter_ser")
user_3 = User("Mary","Adams", 5559794, "maryni@gmail.com", "@mar_y")
user_4 = User("Hugo","Jacobo", 5556444, "HugeJA@gmail.com", "@Hugo_tarugo")

list = [user_1, user_2, user_3, user_4]

for i in list:
    i.describe_user()
    i.greet_user()
    print("")

"""
for i in range(len(list)):
    list[i].describe_user()
    list[i].greet_user()
    print("")
"""
"""
user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()
user_4.describe_user()
user_4.greet_user()
"""
