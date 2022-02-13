"""9-11. Imported Admin:

Start with your work from Exercise 9-8 (page 178) .
Store the classes User, Privileges, and Admin in one module . Create a sepa-
rate file, make an Admin instance, and call show_privileges() to show that
everything is working correctly."""

from Users import Admin

Alexa = Admin('Alexa', 'Cazarez', 'Alex', 'Alex@hotmail.com', '844631126')
Alexa.describe_user()

Alexa_privileges = [ 
    'can add post',
    'can delete post',
    'can ban user',
    ]
Alexa.privileges.privileges = Alexa_privileges

print(f"\n{Alexa.username} cuenta con estos privilegios: ")
Alexa.privileges.show_privileges()