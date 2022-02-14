"""9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178).
Store the classes User, Privileges, and Admin in one module. Create a separate
file, make an Admin instance, and call show_privileges() to show that everything
is working correctly."""

from privileges_user_admin import Admin

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
