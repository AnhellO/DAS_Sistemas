favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
gente = ["jen", "Anita", "edward", "Jorge"]

for i in range(0,len(gente)):
    if gente[i] in favorite_languages.keys():
        print(gente[i], "Gracias por contestar")
    else:
        print(gente[i], "Por favor contesta sobre cual es tu lenguaje de programacion favorito")
