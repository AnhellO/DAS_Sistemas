# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 46),
# use len() to print a message indicating the number of people you are inviting to dinner.

guests = ['Antonio', 'Emanuel', 'Francisco']

message = "1.- Hello dear uncle " + guests[0] + ", I hope you can come this 16th for a mexican dinner in my house."
print(message)
message = "2.- Hi " + guests[1] + "! The next monday we'll have a dinner, you should come here to spend time with " \
                                   "friends for a while, also we will have some beers. "
print(message)
message = "3.- Hello grandpa " + guests[2] + "!, my mother told me that we will have a dinner next monday and we want" \
                                              " that you come here because we miss you. "
print(message)

print('\n')

print(len(guests))