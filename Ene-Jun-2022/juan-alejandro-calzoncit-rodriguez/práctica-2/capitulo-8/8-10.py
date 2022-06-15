def make_great(names):
    for i in range(len(names)):
        names[i] += ' the Great'    


def show_magicians(names):
    for num, name in enumerate(names):
        print(f"{num+1}° magician is : {name}")


names = ['Juan', 'Luis', 'Arturo', 'Eduardo', 'Alan']

make_great(names)
show_magicians(names)