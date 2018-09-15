
def make_great2(magician):
	for name in magician:
		msg='El Gran ' + name.title()
		print(msg)


magician_name = ['Merlin' ,'Alberich' , 'Gargamel', 'Harry Potter']
make_great2(magician_name)

lista = magician_name[:]

print(lista)
