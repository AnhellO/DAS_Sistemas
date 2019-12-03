'''

Juan Ivan Medina Martinez
exercise 3.9

'''
from guestList import inviteguests


if __name__ == "__main__":
	list_guests=["guest1","guest2","guest3","guest4","guest5"]
	nGuests= inviteguests(list_guests)
	print("You have {} guests".format(nGuests))

