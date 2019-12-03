''' 
Juan Ivan Medina Martinez
Exercise 3.5
'''
from guestList import inviteguests
from random import randint


def sorryICant(list_guests,guestCant,guestReplace):
	inviteguests(list_guests)
	print(list_guests[guestCant])
	list_guests[guestCant]=guestReplace
	inviteguests(list_guests)


if __name__ == "__main__":
    list_guests=["guest1","guest2","guest3","guest4","guest5"]
    guestCant=randint(0,len(list_guests)-1)
    guestReplace="guestReplace"
    sorryICant(list_guests,guestCant,guestReplace)