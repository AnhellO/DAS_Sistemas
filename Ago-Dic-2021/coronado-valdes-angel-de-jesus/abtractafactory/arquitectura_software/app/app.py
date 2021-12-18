import json
import random
import mysql.connector

class appDB:
	def __init__(self,user1,pass1,host1,db1,port1):
		self.user1 = user1
		self.pass1 = pass1
		self.host1=host1
		self.db1=db1
		self.port1=port1
		#connection a server mysql


	def register(self):
		#cur = conexion()
		con = mysql.connector.connect(user=self.user1,password=self.pass1,host=self.host1,database=self.db1,port=self.port1)
		print(con)
		cur = con.cursor()
		#extraemos los usuario de un Json
		varOpen = open("user.json", "r")
		varRead = varOpen.read()
		varJson = json.loads(varRead)
		print(len(varJson))
	
		print("*******************************************************************************")
		cont = 0
		#elegimos cuantos usuarios se agregaran
		user = int(input("cuantos usuarios: "))
		print()
		for i in range(user):
			ranName = random.randint(0, 49)
			ranLastName = random.randint(0, 49)
			ranPhoto = random.randint(0, 49)
	
			names = varJson[ranName]["first_name"]
			lastName = varJson[ranLastName]["last_name"]
			image = varJson[ranPhoto]["image"]
			cont += 1
			print("***** [ Usuario "+str(cont)+" ] *****")
			print("Nombre: "+names+"\nApellido: "+lastName+"\nFoto: "+image+"\n")
	
			#insertamos los usuarios a la base de datos
			sql = "INSERT INTO user(nombre,paterno,foto) VALUES (%s,%s, %s)"
			val = (f'{names}',f'{lastName}',f'{image}')
			#cur.execute(sql, val)
			con.commit()
			print(cur.rowcount, "registro insertado")
		print("*******************************************************************************")
	
	def imprimir(self):
		#cur = conexion()
		con = mysql.connector.connect(user=self.user1,password=self.pass1,host=self.host1,database=self.db1,port=self.port1)
		print(con)
		cur = con.cursor()
		#consultamos los usuarios de la base de datos
		cur.execute( "SELECT * FROM user")
		aux = cur.fetchall() 
		print(len(aux))
		for i in range(len(aux)):
			print(aux[i])

if __name__ == "__main__":
	apk = appDB('user','pass1234','localhost','prueba','3306')
	apk.imprimir()
