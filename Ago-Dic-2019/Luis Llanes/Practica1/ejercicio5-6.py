Age = int(input("Ingresa la Edad: "))

if (Age <= 0):
    print("no mames, pon una edad valida")
elif(Age > 0 and Age < 2):
    print("Es un recien nacido")
elif(Age >= 2 and Age < 4):
    print("You are a toddler") #No supe como traducir toddler asi que lo deje asi en ingles
elif(Age >= 4 and Age < 13):
    print("Eres un niño")
elif(Age >= 13 and Age < 20):
    print("Eres un adolescente")
elif(Age >= 20 and Age < 65):
    print("Eres un adulto")
else:
    print("Eres una persona de la tercera edad")