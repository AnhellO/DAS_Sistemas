import Factoria
if __name__ == '__main__':
	mi_factoria = Factoria.Factoria()

	#Factoria, crea a una persona!
persona = mi_factoria.get_persona('Jose Luis del Rio', 'M', 30)
persona1=mi_factoria.get_persona('Ana Maria Garcia','F', 25)

print(persona)
print(persona1)
	# print persona.get_nombre()
	# print persona.get_genero()