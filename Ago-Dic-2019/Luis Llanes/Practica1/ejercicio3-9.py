personas = ["Anita", "Andrea", "Ursula"]

print("un mensaje general")
print()

for i in range(0,len(personas)):
    print("Me gustaria verte pronto", personas[i],"¿Que tal si salimos a cenar?")

print()
print("Ursula no podra asistir a la cena")
print()
personas[2]="Natalia"

for i in range(0,len(personas)):
    print("Me gustaria verte pronto", personas[i],"¿Que tal si salimos a cenar?")


print("\nHe encontrado una mesa mas grande asi que podre invitar a mas\n")

personas.insert(0,"Onofre")
personas.insert(3,"Ricardi")
personas.append("Melissa")

for i in range(0,len(personas)):
    print("Me gustaria verte pronto", personas[i],"¿Que tal si salimos a cenar?")

print()
#Mostrar el numero de invitados para la cena
print("La cantidad de invitados a la cena es:",len(personas))