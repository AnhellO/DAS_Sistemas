''' 
Juan Ivan Medina Martinez
Exercise 3.6
'''
from changingGuestList import sorryICant
from guestList import inviteguests
from random import randint 

def inviteMoreGuests(list_guests,guestCant,guestReplace,list_newGuests):

	sorryICant(list_guests,guestCant,guestReplace)
	print("Hi everyone, just now I just found a bigger dinner table")
	list_guests.insert(0,list_newGuests[0])
	list_guests.insert((int)(len(list_guests)/2),list_newGuests[1])
	list_guests.append(list_newGuests[2])
	inviteguests(list_guests)


if __name__ == "__main__":
    list_guests=["guest1","guest2","guest3","guest4","guest5"]
    guestCant=randint(0,len(list_guests)-1)
    guestReplace="guestReplace"
    list_newGuests=["newGuest1","newGuest2","newGuest3"]
    inviteMoreGuests(list_guests,guestCant,guestReplace,list_newGuests)
