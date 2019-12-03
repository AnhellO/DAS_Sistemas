''' 
Juan Ivan Medina Martinez
Exercise 3.2
'''

def greetFriends(list_friends):
	for friend in list_friends:
		print("Hello {}!".format(friend))

list_friends=["friend1","friend2","freiend3","freiend4","freiend5"]

if __name__ == "__main__":
	greetFriends(list_friends)

