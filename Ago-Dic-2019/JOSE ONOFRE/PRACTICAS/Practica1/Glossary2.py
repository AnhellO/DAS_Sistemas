glosario={
'If': "Condicion",
'While':'Ciclo mientras algo ocurre',
'For':"Ciclo",
'And': "Dos condiciones obligatorias",
'Or':"Una u otra condicion"
}

#for key,value in glosario.items():
 #   print(key+":",value)


glosario['print'] = 'Para imprimir'
glosario["\ n"] = 'Salto de linea'
glosario['int'] = 'Es un entero'
glosario['String'] = 'Una cadena de caracteres'
glosario['=='] = 'Para comparar'
for key,value in glosario.items():
    print(key+":",value)
