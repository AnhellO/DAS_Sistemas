"""Try it yourself 9-11 """
from user import Admin

admin = Admin("Juanita","Ortiz",30,"Oficinista","chrysler")
admin.describe_users()

admon_priv = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
admin.privileges.privileges = admon_priv
admin.privileges.show_privileges()