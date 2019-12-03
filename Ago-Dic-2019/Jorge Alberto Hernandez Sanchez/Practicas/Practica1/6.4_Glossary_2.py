glosario = {'listas' : "Se pueden identificar con []", 'tuplas' : "Se identifican con *()", 
'glosario' : "Se identifican con {}", 'if' : "Condicional", 'for' : "Ciclo", '#' : "Para crear un comentario", 
'str' : "Abreviacion de String", '==' : "usado para comparar elementos", "=!" : "Usado para verificar que dos elementos son diferentes",
'and' : "Usado en condicionales para comprar mas formas a los elementos"}

for clave in glosario.values():
    print(clave.title())