from ImportarAdmin9_11 import Admin

u1 = Admin('Erick', 'Days', 'erickgames', 'erickdiaz@uadec.edu.mx', 'Saltiyok')
u1.describe_user()
u1_priv = ['Puede añadir posts','Puede banear usuarios','Puede ver las ubicaciones','Puede borrar cosas',]
u1.priv.priv = u1_priv

print("\nPrivilegios de " + u1.username + ": \n")
u1.priv.show_priv()
