#8.3
def hacer_playera(tam, mensaje):
    print("el tamaño de la playera  "+ str(tam) + " y el mensaje " + mensaje)
hacer_playera(tam =  12,mensaje ='hola') #palabras clave y no importa el orden por la palabra
hacer_playera(14,'bb') #pocision

#8.4
def hacer_playera(tam="grande", mensaje="yo odio python"):
    print("el tamaño de la playera  "+ tam + " y el mensaje " + mensaje)
hacer_playera() 
hacer_playera("chica")
hacer_playera("mediana")
hacer_playera("chica", "holi")


#8.5
def city(ciudad, pais="Mexico"):
    print("Mi ciudad es " + ciudad + " y esta en el pais de " + pais)
city(ciudad="Monterrey")
city("Saltillo")
city("Berlin", "Rusia")