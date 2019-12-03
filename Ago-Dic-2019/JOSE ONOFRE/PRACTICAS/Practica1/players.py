players = ['charles','martina','michael','florence','eli']
print(players[0:3])

print('Imprimir desde el segundo elemento hasta el cuarto')
print(players[1:4])
print()
print(players[:4])
print()
print(players[2:])
print('Muestra los ultimos 3 de la lista')
print(players[-3:])
print('////////////////////////')
print()
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())


