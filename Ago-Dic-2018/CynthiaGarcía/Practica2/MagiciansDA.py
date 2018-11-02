nombr=['Merlin','Houdini','Potter']
greatNombre=[]

def show_magicians(nombr ):
	print(nombr)
	#print(greatNombre)

def make_great(nombr):
	
	for mago in nombr:
		#magos=nombr.pop()
		mago+='The great'
		greatNombre.append(mago)
		#copy=nombr[:]

	#print (copy)

#Esta funcion es opcional para mostrar el 8-11, 
def copy(nombr, greatNombre):
	copy=nombr[:]
	print(greatNombre)
	print(copy)
	
show_magicians(nombr)
make_great(nombr)
copy(nombr, greatNombre)


	



		


