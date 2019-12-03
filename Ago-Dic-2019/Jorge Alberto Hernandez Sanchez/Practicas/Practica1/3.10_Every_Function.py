familia = ["Jose","Hugo","Jorge","Ramon","Ramiro","Adrian"]

print(familia[0])
print(familia[1])
print(familia[2])
print(familia[3])
print(familia[4])
print(familia[5])


print("Hola", familia[0], "¿Como estas?")
print("Hola", familia[1], "¿Como estas?")
print("Hola", familia[2], "¿Como estas?")
print("Hola", familia[3], "¿Como estas?")
print("Hola", familia[4], "¿Como estas?")
print("Hola", familia[5], "¿Como estas?")

familia[0] = "Elizabeth"
print(familia)

familia.append("Ricardo")
print(familia)

familia.insert(0, "Jorge Alberto")
print(familia)

del familia[0]
print(familia)

borrar = familia.pop()
print(familia)
print(borrar)

familia[0] = "Jorge Alberto"
borrar_primero = familia.pop(0)
print(familia)

familia.remove("Adrian")
print(familia)

familia.sort()
print(familia)

print(sorted(familia))

familia.reverse()
print(familia)

familia.sort(reverse=True)
print(familia)

print(len(familia))