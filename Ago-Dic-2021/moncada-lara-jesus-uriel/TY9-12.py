"""Try it yourself 9-12 """

from privAdm import Admin
#En la clase privAdm tenemos lo siguiente:  from usuariosmod import Usuarios

admin = Admin("Juanita","Ortiz",30,"Oficinista","chrysler")
admin.describe_users()

admon_priv = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
admin.privileges.privileges = admon_priv
admin.privileges.show_privileges() 