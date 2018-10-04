import cafe

myCoffee = cafe.CafeSimple()
print(myCoffee.tipo()+
   ' A solo : '+str(myCoffee.precio())+' pesitos!')

myCoffee = cafe.Vainilla(myCoffee)
print(myCoffee.tipo()+
   ' A solo : '+str(myCoffee.precio())+' pesitos!')

myCoffee = cafe.Leche(myCoffee)
print(myCoffee.tipo()+
   ' A solo : '+str(myCoffee.precio())+' pesitos!')

myCoffee = cafe.Canela(myCoffee)
print(myCoffee.tipo()+
   ' A solo : '+str(myCoffee.precio())+' pesitos!')

myCoffee = cafe.LecheCanela(myCoffee)
print(myCoffee.tipo()+
   ' A solo : '+str(myCoffee.precio())+' pesitos!')
