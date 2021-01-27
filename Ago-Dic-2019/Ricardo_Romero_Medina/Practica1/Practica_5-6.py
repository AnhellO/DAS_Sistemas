edad = 22

if edad <= 2:
    print("Esta persona es un bebe")
elif edad > 2 and edad <= 4:
    print("Esta persona es un niño pequeño")
elif edad > 4 and edad <= 13:
     print("Esta persona es un niño")
elif edad > 13 and edad <= 20:
    print("Esta persona es un adolescente")
elif edad > 20 and edad <= 65:
    print("Esta persona es un adulto")
else:
    print("Esta persona es un anciano")