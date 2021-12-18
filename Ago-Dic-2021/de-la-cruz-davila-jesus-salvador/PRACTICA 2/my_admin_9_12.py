from admin_9_12 import Admin

user1 = Admin("Anahi", "De la Cruz", "Elvanana", "elva960@hotmail.com", "8441234567", "16")
user1.describe_user()


user1_privilges = [
    'Puede agregar publicaciones',
    'Puede borrar publicaciones',
    'Puede eliminar a un usuario'
]

user1.privileges.priveleges = user1_privilges
user1.privileges.show_privileges()

user2 = Admin("Josh", "Peck", "JoshPeck", "JoshPeck@hotmail.com", "8424569312", "34")
user2.describe_user()

user2_privilges = [
    'Puede agregar publicaciones',
]

user2.privileges.priveleges = user2_privilges
user2.privileges.show_privileges()


user3 = Admin("Drake", "Bell", "DrakeBell", "DrakeBell@hotmail.com", "8425682391", "35")
user3.describe_user()

user3_privilges = [
    'Puede agregar publicaciones',
    'Puede eliminar a un usuario'
]

user3.privileges.priveleges = user3_privilges
user3.privileges.show_privileges()