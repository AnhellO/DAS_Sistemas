class User():
    def __init__(self,first_name,last_name,username,email,number,age):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.number = number
        self.age = age
    
    def describe_user(self):
        print("  NAME:  ", self.first_name)
        print("  LAST NAME:  ", self.last_name)
        print("  USERNAME:  ", self.username)
        print("  EMAIL:  ", self.email)
        print("  NUMBER:  ", self.number)
        print("  AGE:  ", self.age)
        print("")
    
    def greet_user(self):
        print("Welcome ", self.username)
        
    

user1 = User("Anahi", "De la Cruz", "Elvanana", "elva960@hotmail.com", "8441234567", "16")
user1.greet_user()
user1.describe_user()


user2 = User("Jesus", "De la Cruz", "Jisus", "Jisus3680@hotmail.com", "8447894561", "22")
user2.greet_user()
user2.describe_user()


user3 = User("Josh", "Peck", "JoshPeck", "JoshPeck@hotmail.com", "8424569312", "34")
user3.greet_user()
user3.describe_user()


user4 = User("Drake", "Bell", "DrakeBell", "DrakeBell", "8449631483", "35")
user4.greet_user()
user4.describe_user()
