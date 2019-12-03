# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner,
# and you have space for only two guests.

# • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you
# can invite only two people for dinner.

# • Use pop() to remove guests from your list one at a time until only two names remain in your list.
# Each time you pop a name from your list, print a message to that person letting them know you’re sorry
# you can’t invite them to dinner.

# • Print a message to each of the two people still on your list, letting them know they’re still invited.

# • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure
# you actually have an empty list at the end of your program.


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

del (guests[1])
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

# Dammit! I'm so sorry but I  can invite only 2 people for dinner :(

print("\nI'm so sorry but I can invite only 2 people for dinner :( \n")

print("I'm so sorry " + guests.pop() + " but there is no room in my house :(")
print("I'm so sorry " + guests.pop() + " but there is no room in my house :(")
print("I'm so sorry " + guests.pop() + " but there is no room in my house :(")
print("I'm so sorry " + guests.pop() + " but there is no room in my house :(")

# Now we have 2 people that I can invite

print("\n")
message = "Hello " + guests[0] + " please don't forget to come tonight for dinner!"
print(message)
message = "Hello uncle " + guests[1] + " please don't forget to come tonight for dinner!"
print(message)

# Now I have to remove the last two names from my list

print("\n")
del(guests[1])
del(guests[0])

print(guests)