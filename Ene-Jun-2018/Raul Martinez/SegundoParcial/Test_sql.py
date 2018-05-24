import sqlite3

#Ya se actualizo y deleteo checate en los insert.
#lo unico que no comente fue la parte donde se muestra.


con = sqlite3.connect('C:/Users/Raul/DAS_Sistemas/Ene-Jun-2018/Raul Martinez/SegundoParcial/games.db')
cursor = con.cursor()
print("se hizo la coneccion")

#cursor.execute('''CREATE TABLE CONSOLAS
 #       (ID integer PRIMARY KEY,
  #      NOMBRE TEXT NOT NULL,
   #     MARCA TEXT NOT NULL)''')
#cursor.execute('''CREATE TABLE VIDEOJUEGOS
 #       (ID integer PRIMARY KEY,
  #      NOMBRE TEXT NOT NULL,
   #     CATEGORIA TEXT NOT NULL)''')

#cursor.execute("INSERT INTO VIDEOJUEGOS (ID, NOMBRE, CATEGORIA) \
#	VALUES (1, 'CALL OF DUTY', 'DISPAROS')")

#cursor.execute("INSERT INTO VIDEOJUEGOS (ID, NOMBRE, CATEGORIA) \
#	VALUES (2, 'FORNITE', 'BATTLE ROYAL')")

#cursor.execute("INSERT INTO VIDEOJUEGOS (ID, NOMBRE, CATEGORIA) \
#	VALUES (3, 'LEAGUE OF LEGENDS', 'ESTRATEGIA')")

#cursor.execute("INSERT INTO CONSOLAS (ID, NOMBRE, MARCA) \
#	VALUES (1, 'XBOX ONE', 'MICROSOFT')")

#cursor.execute("INSERT INTO CONSOLAS (ID, NOMBRE, MARCA) \
#	VALUES (2, 'PLAYSTATION 4', 'SONY')")

#cursor.execute("INSERT INTO CONSOLAS (ID, NOMBRE, MARCA) \
#	VALUES (3, 'SWITCH', 'NINTENDO')")

#con.commit()
#print('se guardo correctamente')
#con.close()

print("Tabla CONSOLAS")

cursor.execute("SELECT ID, NOMBRE, MARCA FROM CONSOLAS")
for i in cursor:
	print("ID = ", i[0])
	print("NOMBRE = ", i[1])
	print("MARCA = ", i[2], "\n")

print("Operacion Satisfactoria","\n")

print("Tabla VIDEOJUEGOS")

cursor.execute("SELECT ID, NOMBRE, CATEGORIA FROM VIDEOJUEGOS")
for i in cursor:
	print("ID = ", i[0])
	print("NOMBRE = ", i[1])
	print("CATEGORIA = ", i[2], "\n")

print("Operacion Satisfactoria")
con.close()

# cursor.execute("UPDATE CONSOLAS set NOMBRE = 'Wii U' where ID=3")
# con.commit()
# print("Actualizaciones totales: ", con.total_changes)

# cursor.execute("SELECT ID, NOMBRE, MARCA FROM CONSOLAS")

# for i in cursor:
# 	print("ID = ", i[0])
# 	print("NOMBRE = ", i[1])
# 	print("MARCA = ", i[2], "\n")

# print("Operacion Satisfactoria")
# #con.close()

# cursor.execute("UPDATE CONSOLAS set NOMBRE = 'Wii U' where ID=3")
# con.commit()
# print("Actualizaciones totales: ", con.total_changes)

# cursor.execute("SELECT ID, NOMBRE, MARCA FROM CONSOLAS")

# for i in cursor:
# 	print("ID = ", i[0])
# 	print("NOMBRE = ", i[1])
# 	print("MARCA = ", i[2], "\n")

# print("Operacion Satisfactoria")
# con.close()


# cursor.execute("UPDATE VIDEOJUEGOS set CATEGORIA = 'FANTASIA' where ID=3")
# con.commit()
# print("Actualizaciones totales: ", con.total_changes)

# cursor.execute("SELECT ID, NOMBRE, CATEGORIA FROM VIDEOJUEGOS")

# for i in cursor:
# 	print("ID = ", i[0])
# 	print("NOMBRE = ", i[1])
# 	print("CATEGORIA = ", i[2], "\n")

# print("Operacion Satisfactoria")
# con.close()


# cursor.execute("DELETE FROM CONSOLAS WHERE ID = 2")
# con.commit()
# print("registros Borrados: ", con.total_changes)

# cursor.execute("SELECT ID, NOMBRE, MARCA FROM CONSOLAS")

# for i in cursor:
# 	print("ID = ", i[0])
# 	print("NOMBRE = ", i[1])
# 	print("MARCA = ", i[2], "\n")

# print("Operacion Satisfactoria")
# con.close()


# cursor.execute("DELETE FROM VIDEOJUEGOS WHERE ID = 1")
# con.commit()
# print("registros Borrados: ", con.total_changes)

# cursor.execute("SELECT ID, NOMBRE, CATEGORIA FROM VIDEOJUEGOS")

# for i in cursor:
# 	print("ID = ", i[0])
# 	print("NOMBRE = ", i[1])
# 	print("CATEGORIA = ", i[2], "\n")

# print("Operacion Satisfactoria")
# con.close()


