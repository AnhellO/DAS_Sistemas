prompt= "\nPor favor escriba un ingrediente: "
prompt+= "\nEscriba 'quit' cuando haya terminado"

while True:
    ingrediente= input(prompt)

    if ingrediente == 'quit':
        break
    else:
        print("Se agregara " +ingrediente.title()+ " a la pizza")
