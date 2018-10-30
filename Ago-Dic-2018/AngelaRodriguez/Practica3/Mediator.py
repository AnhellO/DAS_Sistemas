import time 
class TC:  
	def __init__(self):
		self._tm = tm   
		self._bProblem = 0    
	def setup(self):   
		print ("Congigurando la Prueba")
		time.sleep(1)
		self._tm.prepareReporting() 
	def execute(self):	
		if not self._bProblem:    
			print ("Ejecutando la prueba")
			time.sleep(1)   
		else:    
			print ("Problema en la configuración. Prueba no ejecutada")    
	def tearDown(self):   
		if not self._bProblem:     
			print ("Derribando")    
			time.sleep(1)    
			self._tm.publishReport()   
		else:    
			print ("Prueba no ejecutada No se requiere derribar.")   
	def setTM(self,TM):   
		self._tm = tm    
	def setProblem(self, value):   
		self._bProblem = value     
class Reporter:   
	def __init__(self):   
		self._tm = None    
	def prepare(self):   
		print ("Reporter Class se está preparando para informar los resultados")  
		time.sleep(1)    
	def report(self):   
		print ("Informar los resultados de la Prueba")   
		time.sleep(1)    
	def setTM(self,TM):   
		self._tm = tm   
class DB:  
	def __init__(self):   
		self._tm = None    
	def insert(self):   
		print ("Al insertar la ejecución, comienza el estado en la Base de datos")   
		time.sleep(1)
		#El siguiente codigo es para simular una comunicacion de DB a TC   
		import random   
		if random.randrange(1,4) == 3:    
			return -1      
	def update(self):   
		print ("Actualización de los resultados de la prueba en la base de datos")   
		time.sleep(1)    
	def setTM(self,TM):   
		self._tm = tm   
class TestManager:  
	def __init__(self):   
		self._reporter = None   
		self._db = None   
		self._tc = None    
	def prepareReporting(self):   
		rvalue = self._db.insert()   
		if rvalue == -1:    
			self._tc.setProblem(1)    
			self._reporter.prepare()    
	def setReporter(self, reporter):   
		self._reporter = reporter    
	def setDB(self, db):   
		self._db = db    
	def publishReport(self):   
		self._db.update()    
		rvalue = self._reporter.report()    
	def setTC(self,tc):   
		self._tc = tc   
if __name__ == '__main__':  
	reporter = Reporter()  
	db = DB()  
	tm = TestManager()  
	tm.setReporter(reporter)  
	tm.setDB(db)    
	reporter.setTM(tm)  
	db.setTM(tm)   
	# Para simplificar, estamos haciendo un bucle en la misma prueba. 
	# Prácticamente, podría tratarse de varias clases de prueba únicas y sus objetos  
	while (1):   
		tc = TC()   
		tc.setTM(tm)   
		tm.setTC(tc)   
		tc.setup()   
		tc.execute()   
		tc.tearDown() 
