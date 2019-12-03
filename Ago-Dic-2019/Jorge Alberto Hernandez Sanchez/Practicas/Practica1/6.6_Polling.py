favorite_languages = {'jen': 'python', 'sarah': 'c', 
'edward': 'ruby', 'phil': 'python'}

poll = ['Eduardo', 'Jorge', 'Osvaldo', 'jen', 'sarah', 'ruby']

for i in poll:
    if i == favorite_languages.keys():
        print(i, "Gracias por tomar la encuesta")
    else:
        print(i, "Te invito a tomar la encuesta")