''' 
Juan Ivan Medina Martinez
Exercise 3.4
'''

def  inviteguests(list_guests):
	for guest in list_guests:
		print("Hey {}!, We haven't talked for a long time, do you want to go out to dinner with me today?".format(guest))
	return len(list_guests)#This is for exercise 3.9	


if __name__ == "__main__":
	list_guests=["guest1","guest2","guest3","guest4","guest5"]
	inviteguests(list_guests)

