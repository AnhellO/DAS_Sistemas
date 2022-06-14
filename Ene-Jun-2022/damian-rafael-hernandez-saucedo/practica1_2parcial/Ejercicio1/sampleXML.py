import xml.etree.ElementTree as ET


class LeerArchivo:
	def __init__(self,path):
		self.path = path

	def Leer(self):
		tree = ET.parse(self.path)
		root = tree.getroot()
		return root

	def Tree(self):
		tree = ET.parse(self.path)
		return tree



class MostrarId:
	def __init__(self,par_impar,root):
		self.par_impar = par_impar
		self.root      = root

	def Mostrar_Id(self):
		for i in range(len(self.root)):
			if int(self.root[i][0].text)%self.par_impar == 0:
				for j in range(len(self.root[i])):
					print(self.root[i][j].text)
				print("====="*5)



class MostrarDominio:
	def __init__(self,dominios,root):
		self.dominios = dominios
		self.root     = root

	def Mostrar_Id(self):
		dominio = ''
		for i in range(len(self.root)):
			dom     = self.root[i][4].text
			dominio = dom[len(dom)-4] + dom[len(dom)-3] + dom[len(dom)-2] + dom[len(dom)-1]

			if dominio == self.dominios[0] or dominio == self.dominios[1]:
				for j in range(len(self.root[i])):
					print(self.root[i][j].text)
				print("====="*5)



class UpdateXml:
	def __init__(self,texto,tree):
		self.texto = texto
		self.tree  = tree
		self.root  = tree.getroot()

	def Update_Xml(self):
		for ip in self.root.iter(self.texto):
			ip.text = '127.0.0.1'

		self.tree.write('updated.xml')


	def Mostrar_Update_Xml(self):
		for i in range(len(self.root)):
			for j in range(len(self.root[i])):
				print(self.root[i][j].text)
			print("====="*5)




if __name__ == "__main__":
	
	xml  = LeerArchivo('sample.xml')
	root = xml.Leer()
	tree = xml.Tree()

	
	flag = True
	while flag == True:
		print('\n1.- Imprimir lista que sean par.')
		print('2.- Imprimir lista de dominio ".edu" y ".gov".')
		print('3.- Modificar el Archivo tag "ip_address".')
		op = int(input('opcion: '))

		print('')
		if   op == 1:
			usuario_id = MostrarId(2,root)
			usuario_id.Mostrar_Id()
		elif op == 2:
			mostrar_dominio = MostrarDominio(['.edu','.gov'],root)
			mostrar_dominio.Mostrar_Id()
		elif op == 3:
			update_xml = UpdateXml('ip_address',tree)
			update_xml.Update_Xml()
			update_xml.Mostrar_Update_Xml()
		else:
			print('Opcion Invalida')




