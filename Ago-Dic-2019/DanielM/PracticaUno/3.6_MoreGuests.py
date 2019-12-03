# 3-6. More Guests: You just found a bigger dinner table, so now more space is available.
# Think of three more guests to invite to dinner.

# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print statement to the end of your
# program informing people that you found a bigger dinner table.

# • Use insert() to add one new guest to the beginning of your list.

# • Use insert() to add one new guest to the middle of your list.

# • Use append() to add one new guest to the end of your list.

# • Print a new set of invitation messages, one for each person in your list.

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

# Now we have more space, so I gonna invite more people xd

print("\nNow we have more space! xdxd \n")

guests.insert(0, 'Ariel')
guests.insert(3, 'Sergio')
guests.append('Norma')

message = "1.- Hi " + guests[0] + "!, hey nigga come here tonight to dinner, we gonna celebrate this day! :v"
print(message)

message = "2.- Uncle " + guests[1] + ", don't forget the dinner is today, see you later!."
print(message)

message = "3.- Hi " + guests[2] + "! Today we'll have dinner, please come here to spend time with us, " \
                                  "we will have a lot of meat and some beers. "
print(message)

message = "4.- Hey " + guests[3] + "!, how are you?, please come to my house tonight"
print(message)

message = "5.- Grandpa " + guests[4] + ", don't forget to come today to dinner."
print(message)

message = "6.- Hello " + guests[5] + "!, I was wondering if you would like to come here tonight to dinner?, " \
          "I hope you don't have things to do!"
print(message)