from user_9_11 import Admin

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
    'Puede agregar publicaciones'
]

user2.privileges.priveleges = user2_privilges
user2.privileges.show_privileges()