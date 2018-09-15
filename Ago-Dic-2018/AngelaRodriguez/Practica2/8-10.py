def make_great(magician):
	for name in magician:
		msg='El Gran ' + name.title()
		print(msg)


magician_name = ['Merlin', 'Alberich', 'Gargamel', 'Harry Potter']
make_great(magician_name)
