
text = "Ene-Jun-2022/david-navoa-acevedo/Practica-2/Capitulo_10/Ejercicio_10/raw_text.txt"

with open(text) as opened_text:
    current_text = opened_text.read()
    print(current_text.lower().count("years"))