"""9-12. Multiple Modules:

Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly."""

from Admin import Admin

Alexa = Admin('Alexa', 'Cazarez', 'Alex', 'Alex@hotmail.com', '844631126')
Alexa.describe_user()

Alexa_privileges = [
    'can add post',
    'can delete post',
    'can ban user']
    
Alexa.privileges.privileges = Alexa_privileges

print(f"\n{Alexa.username} tiene estos privilegios: ")
Alexa.privileges.show_privileges()