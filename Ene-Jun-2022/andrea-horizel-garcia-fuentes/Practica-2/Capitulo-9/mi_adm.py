from admiprivi import Admin

Andrea = Admin('Andrea', 'garcia', 'a_garcia', 'a_garcia@example.com', 'Saltillo')
Andrea.describe_Usuario()
Andrea.greet_usuario()

Andrea.privileges.privileges= [
    'can delet user',
    'can add post',
    'can reset passwords',
    ]

Andrea.privileges.show_privileges()