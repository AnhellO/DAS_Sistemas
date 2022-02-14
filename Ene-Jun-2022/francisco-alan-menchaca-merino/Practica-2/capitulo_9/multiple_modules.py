"""9-12. Multiple Modules: Store the User class in one module, and store the 
Privileges and Admin classes in a separate module. In a separate file, create 
an Admin instance and call show_privileges() to show that everything is still 
working correctly"""
from admin_privileges import Admin

admin_privileges = ["can add post", "can delete post", "can ban user",
                    "can add record", "can remove record", "can acess to server"]
user_admin = Admin("Alan", "Menchaca", "México",
                   "alanmenchaca@gmail.com")

user_admin.admin_privileges.privileges = admin_privileges
user_admin.admin_privileges.show_privileges()
# Admin privileges:
# - can add post
# - can delete post
# - can ban user
# - can add record
# - can remove record
# - can acess to server
