from user import Admin

juanito = Admin('Juanito','Crack' ,'Juanito_56_lokote', 'juanito_de_maria@gmail.com', 'Paris')
juanito.describe_user()
juanito_privileges = ['puede borrar usuarios \n', 'puede comprar comida\n', 'puede casarse\n', 'puede ser lo que quiera ser\n']
juanito.privileges.privileges = juanito_privileges
print (f"\n El admin {juanito.username} tiene los siguientes privilegios:")
juanito.privileges.show_privileges()