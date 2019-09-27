from SimpleFactory import SimpleFactory

def main():
	instancia = SimpleFactory.makeConcreteClassPersonaje(
		tipo='Mago',
		nombre='Merlin',
		hab_especial='Transmutación'
	)

	print(instancia)

if __name__ == '__main__':
	main()