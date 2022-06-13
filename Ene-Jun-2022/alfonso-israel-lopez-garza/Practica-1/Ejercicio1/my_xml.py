import xml.etree.ElementTree as ET

class ManejoXML:
    def __init__(self,people) -> None:
        self.people = people

    def ObtenerPorPares(self):
        '''Funcion que filtra los datos por id con valor par'''
        Lista_Pares = []
        Cp = 0 #Contador
    
        for person in self.people:
            if int(person[0].text) % 2 == 0:
                Lista_Pares.append([])
                for elements in person:
                    Lista_Pares[Cp].append(elements.tag)
                    Lista_Pares[Cp].append(elements.text)
                Cp += 1
        return Lista_Pares

    def ObtenerPorCorreo(self):
        '''Funcion que filtra las personas por correo con dominio .edu o .gov'''
        Lista_Correo = []
        Cc = 0 #Contador
    
        for person in self.people:
            correo = str(person[4].text)
            if correo.endswith('.edu') or correo.endswith('.gov'):
                Lista_Correo.append([])
                for elements in person:
                    Lista_Correo[Cc].append(elements.tag)
                    Lista_Correo[Cc].append(elements.text)
                Cc += 1
        return Lista_Correo

    def ModificandoMXL(self,xmltree):
        nuevaIP = "127.0.0.1"
        '''Que modifica la ip address y guarda los resultados en un nuevo XML'''
        for persona in xmltree.iter('ip_address'):
            persona.text = nuevaIP
        
        tree.write('updated.xml')
            


        

if __name__ == "__main__":
    tree = ET.parse('sample.xml')
    people = tree.getroot()
    InstanciaXml = ManejoXML(people)

    FiltroPersonasIdPar = InstanciaXml.ObtenerPorPares()
    FiltroPersonasCorreo = InstanciaXml.ObtenerPorCorreo()
    NuevoXml = InstanciaXml.ModificandoMXL(people)
    
    #Impresion de datos
    print(f"Filtrando personas por id par: \n{FiltroPersonasIdPar} \n")
    print(f"Filtrando personas con correo .edu o .gov: \n{FiltroPersonasCorreo}\n")