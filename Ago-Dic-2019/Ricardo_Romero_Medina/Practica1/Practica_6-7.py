personas={'first_name':'Diego','second_name':'Romero','age':18,'city':'Saltillo'}

personas2={'first_name':'Juan','second_name':'Rodriguez','age':25,'city':'Saltillo'}

personas3={'first_name':'Jose','second_name':'Perez','age':30,'city':'Saltillo'}

personas4=[personas,personas2,personas3]

for i in range(len(personas4)):
    print(personas4[i])