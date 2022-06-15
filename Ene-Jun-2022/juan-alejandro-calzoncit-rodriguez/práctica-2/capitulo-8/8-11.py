def make_great(names):
    for i in range(len(names)):
        names[i] += ' the Great'    
    return names        


def show_magicians(names):
    for num, name in enumerate(names):
        print(f"{num+1}° magician is : {name}")


names = ['Juan', 'Luis', 'Arturo', 'Eduardo', 'Alan']

new_names = make_great(names[:])

print("List with the original names : ")
show_magicians(names)
print("\nList with the Great added in each name : ")
show_magicians(new_names)