items = ['Ingles','Español','Ruso','Aleman','Japones','Frances','Coreano']
print(items)

print('Hola! Yo se hablar en '+items[0]+' y '+items[1])

items[2] = 'Portugues'

print('Se cambia Ruso por Portugues')
print(items)

print('Agregando nuevos idiomas a la lista')
items.insert(0,'Polaco')
items.insert(4,'Arabe')
items.insert(6,'Italiano')

print(items)

print('Eliminando el ultimo idioma de la lista')
popped_items= items.pop()

print(popped_items)

print('Eliminando el idioma de la posicion 3')
del items[3]

print(items)

print('Lista original')
print(items)
print('Lista ordenada alfabeticamente')
print(sorted(items))
print('Lista original')
print(items)
print('Lista ordenada y al reverso')
items.sort(reverse=True)
print(items)
print('Lista al reverso = a la original')
items.reverse()
print(items)
print('Lista ordenada permanentemente')
items.sort()
print(items)
print('Lista al reves permanente')
items.sort(reverse=True)
print(items)