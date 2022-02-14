from faker import Faker
fake=Faker()
def Leer_archivo():
    document=open("README.md","r")
    lienas=document.readlines()
    new_document=""
    for linea in lienas:  
        palabras=linea.split(" ")
        for j in range(0,len(palabras),1):
            if palabras[j]=='python' or palabras[j]=='Python' :
                palabras[j]=fake.name()
            new_document +=palabras[j]+" "
    return new_document

def crear_fichero():
    aux=Leer_archivo()
    with open("README-ALTERADO.md","w+") as fichero:
        fichero.write(aux)
    

if __name__=="__main__":
    crear_fichero()
