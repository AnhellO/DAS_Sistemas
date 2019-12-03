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

print("\nAl parecer la mesa que queria no podra llegar a tiempo, asi que solo puedo invitar a dos personas\n")

while(len(personas)>2):
    i=len(personas)-1
    print("Perdona",personas[i],"pero ahora solo puedo invitar a 2 personas asi que tengo que eliminarte de la lista de invitados")
    personas.pop()
print()
for i in range(0,len(personas)):
    print("oye",personas[i], "he tenido que eliminar personas de la lista de invitados pero tu aun estas en ella")

print()
print("Aqui ya vacio la lista de invitados")
del personas[0]
del personas[0]

print(personas)