# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send
# out a new set of invitations. You’ll have to think of someone else to invite.

# • Start with your program from Exercise 3-4. Add a print statement at the end of your program stating
# the name of the guest who can’t make it.

# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person
# you are inviting.

# • Print a second set of invitation messages, one for each person who is still in your list.

guests = ['Antonio', 'Emanuel', 'Francisco']

message = "1.- Hello dear uncle " + guests[0] + ", I hope you can come this 16th for a mexican dinner in my house."
print(message)
message = "2.- Hi " + guests[1] + "! The next monday we'll have a dinner, you should come here to spend time with " \
                                  " the family and friends for a while, also we will have some beers. "
print(message)
message = "3.- Hello grandpa " + guests[2] + "!, my mother told me that we will have a dinner next monday and we want" \
                                             " that you come here because we miss you. "
print(message)

print("\n My friend " + guests[1] + " can't make it to dinner.\n")

# My friend Emanuel can't make it, so I'll invite my friend Luis.

del(guests[1])
guests.insert(1, 'Luis')

message = "1.- Uncle " + guests[0] + ", don't forget the dinner is today, see you later!."
print(message)

message = "2.- Hi " + guests[1] + "! Today we'll have a dinner, please come here to spend time with us, " \
                                  "we will have meat and some beers. "
print(message)

message = "3.- Grandpa " + guests[2] + ", don't forget to come today to the dinner."
print(message)