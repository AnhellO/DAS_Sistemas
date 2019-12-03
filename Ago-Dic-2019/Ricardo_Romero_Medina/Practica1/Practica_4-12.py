my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]

print("Mi comida favorita es: ")

for i in range(len(my_foods)):
    print(my_foods[i])

print("La comida favorita de mi amigo es: ")

for j in range(len(friend_foods)):
    print(friend_foods[j])
