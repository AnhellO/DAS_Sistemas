from admin import Admin

maria = Admin('maria', 'torres', 'm_torres', 'maria@example.com')
maria.describe_user()

maria_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
maria.privileges.privileges = maria_privileges

print(f"\nEl administrador {maria.username} tiene estos privilegios: ")
maria.privileges.show_privileges()