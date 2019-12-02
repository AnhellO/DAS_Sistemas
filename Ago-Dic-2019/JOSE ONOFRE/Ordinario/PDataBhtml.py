import sqlite3
##Codigo Prueba NO HACERLE CASO
c = sqlite3.connect('Base.db')
cur = c.cursor()
cur.execute("SELECT id from characterp")
test = cur.fetchall()

print(test)

## Codigo de Prueba NO HACERLE CASO