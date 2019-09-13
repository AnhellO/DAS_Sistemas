favorite_languages={
'jen':'python',
'sarah':'c',
'edward':'ruby',
'phil':'python',
}

for nombre, lenguaje in favorite_languages.items():
    print("El lenguaje favorito de "+nombre.title()+" es "+lenguaje.title())


personas = ['Angel', 'Mario','Pedro','Karla','edward']

for persona in personas:
    if persona in favorite_languages.keys():
        print("Gracias por aceptar, "+persona.title())
    else:
        print(persona.title()+", Que lenguaje te gustaria?")

