# 4-2. Animals: Think of at least three different animals that have a common characteristic.
# Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# • Modify your program to print a statement about each animal, such as a dog would make a great pet.
# • Add a line at the end of your program stating what these animals have in common. You could print a sentence
# such as Any of these animals would make a great pet!

animals = ['lion', 'tiger', 'leopard']

for animal in animals:
    print(animal)


print("\nThe " + animals[0] + " is a great hunter.")
print("The " + animals[1] + " has some beautiful colors.")
print("The " + animals[2] + " is a fast animal\n")

print("Any of these animals are felines.")