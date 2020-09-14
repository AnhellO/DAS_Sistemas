class Banco():
	def __init__(self,numCta,nomCte,saldo):
		self.numCta=numCta
		self.nomCte=nomCte
		self.saldo=saldo
	def getNumCta(self):
		return self.numCta
	def setNumCta(self,numCta):
		self.numCta=numCta
	def getNomCte(self):
		return self.nomCte
	def setNomCte(self,nomCte):
		self.nomCte = nomCte
	def getSaldo(self):
		return self.saldo
	def setNumCta(self,saldo):
		self.saldo = saldo


class Cuenta(Banco):
	def _str_(self):
		print("Número de cuenta:",self.numCta,"\nNombre del cliente:",
		 self.nomCte,"\nSaldo:",self.saldo)

	def Depositar(self,deposito):
		nvoSaldo=self.saldo+deposito
		self.saldo=nvoSaldo
		print("El nuevo saldo es "+str(self.saldo))

	def Retirar(self,retiro):
		nuevoSaldo=self.saldo-retiro
		self.saldo=nuevoSaldo
		print("El nuevo saldo es "+str(self.saldo))

Cuenta1=Cuenta(5041,"Juan",500)
Cuenta1._str_()
Cuenta1.Depositar(100)
Cuenta1.Retirar(50)
