Andrea = {"celular": 8662056906, "tiempo": 7, "numero":13}
Anita = {"celular": 8662556979, "tiempo": 5, "numero":17}
Onofre = {"celular": 8447678477, "tiempo": 3, "numero": 8}
Ricardi = {"celular": 8443558362, "tiempo": 3, "numero":170}

Agenda = {"Andrea":Andrea, "Anita": Anita, "Onofre": Onofre,"Ricardi": Ricardi}


for key, value in Agenda.items():
    print("Numeros favoritos de", key)
    print(value, "\n")

