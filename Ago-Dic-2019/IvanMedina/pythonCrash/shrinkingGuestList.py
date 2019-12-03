''' 
Juan Ivan Medina Martinez
Exercise 3.7
'''
from changingGuestList import sorryICant
from guestList import inviteguests
from random import randint 
from moreGuests import inviteMoreGuests

list_newGuests=["newGuest1","newGuest2","newGuest3"]

def shrinkingGuestList(list_guests,guestCant,guestReplace,list_newGuests):
    inviteMoreGuests(list_guests,guestCant,guestReplace,list_newGuests)
    print("I'm sorry, there will be a change of plans, i can only invite 2 guests. ")
    while(len(list_guests)>2):
        print("Hello {}, i really sorry but i cant invite you to dinner. ".format(list_guests.pop()))
    for guest in list_guests:
        print("Hey {} you're still invited to dinner, see you tonight. ".format(guest))
    del list_guests
    try :
        print(list_guests)
    except:
        print("Error: list not foud")

if __name__ == "__main__":
    list_guests=["guest1","guest2","guest3","guest4","guest5"]
    guestCant=randint(0,len(list_guests)-1)
    guestReplace="guestReplace"
    list_newGuests=["newGuest1","newGuest2","newGuest3"]
    shrinkingGuestList(list_guests,guestCant,guestReplace,list_newGuests)