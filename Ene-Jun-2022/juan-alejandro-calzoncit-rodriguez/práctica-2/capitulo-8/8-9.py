def show_magicians(names):
    for num, name in enumerate(names):
        print(f"{num+1}° magician is : {name}")


names = ['Juan', 'Luis', 'Arturo', 'Eduardo', 'Alan']

show_magicians(names)