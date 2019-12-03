Num_fav={'Luis':[20,15,50,30],
         'Jose':[48,55,84,60,30],
         'Hector':[63,88,96,15],
         'Xavi':[5,51,33,15,2] , 'Diana':[30,52,60]}

for persona, numeros in Num_fav.items():
    print("\n")
    print("Los numeros favoritos de "+ persona.title()+ " son: ")

    for num_fav in numeros:
        print(num_fav)
