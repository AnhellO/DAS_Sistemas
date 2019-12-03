'''Try It Yourself'''
'''4-10. Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
• Print the message, The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.
• Print the message, Three items from the middle of the list are:. Use a slice
to print three items from the middle of the list.
• Print the message, The last three items in the list are:. Use a slice to print
the last three items in the list.'''
M3 = list(range(3,31,3))
print(M3[0:3])
print(M3[3:6])
print(M3[-3:])

'''4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
(page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message, My favorite
pizzas are:, and then use a for loop to print the first list. Print the message,
My friend’s favorite pizzas are:, and then use a for loop to print the second
list. Make sure each new pizza is stored in the appropriate list.'''

pizzas = ['Pepperoni', 'Carne', '3 Quesos', 'Champiñones', 'La que tiene los 4 ingredientes', 'Orilla rellena de queso con todo lo anterior']
friend_pizza = pizzas[:]
pizzas.append('Hawaina')
friend_pizza.append(('Anchoas'))

print("My favorite pizzas are:")
print(pizzas)
print("My friend’s favorite pizzas are:")
print(friend_pizza)

'''4-12. More Loops: All versions of foods.py in this section have avoided using
for loops when printing to save space. Choose a version of foods.py, and
write two for loops to print each list of foods.'''
print("My favorite pizzas are:")
for i in pizzas:
    print(i)

print("My friend’s favorite pizzas are:")
for i in friend_pizza:
    print(i)