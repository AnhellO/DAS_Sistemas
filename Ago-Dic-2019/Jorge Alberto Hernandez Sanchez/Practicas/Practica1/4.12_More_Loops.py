my_foods = ["Pizza", "Falafel", "Carrot Cake"]
friend_foods = my_foods[:]

print("My favorite foods are:")
# print(my_foods) usado en el ejemplo de copiar listas

for i in my_foods:
    print(i)

print("\nMy friend's favorite foods are:")

for i in friend_foods:
    print(i)

my_foods.append("Cannoli")
friend_foods.append("Ice Cream")

print("My favorite foods are:")

for i in my_foods:
    print(i)

print("\nMy friend's favorite foods are:")
for i in friend_foods:
    print(i)
