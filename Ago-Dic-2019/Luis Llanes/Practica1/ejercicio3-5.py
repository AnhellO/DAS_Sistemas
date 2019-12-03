personas = ["Anita", "Andrea", "Ursula"]

print("un mensaje general")
print()

for i in range(0,len(personas)):
    print("me gustaria verte pronto", personas[i],"¿Que tal si salimos a cenar?")

print()
print("Ursula no podra asistir a la cena")
print()
personas[2]="Natalia"

for i in range(0,len(personas)):
    print("me gustaria verte pronto", personas[i],"¿Que tal si salimos a cenar?")

