import yaml as Ym

class ManejandoYaml:
    def __init__(self,data) -> None:
        self.dic = data['people']

    def FiltroMultiplo3(self):
        '''Funcion que filtra a las personas por id multiplo de 3'''
        Lista_Personas_3 = []
        C3 = 0 #Contador personas
        for person in self.dic['person']:
            if int(person['id']) % 3 == 0:
                Lista_Personas_3.append([])
                Lista_Personas_3[C3].append(person)
                C3 +=1
        return Lista_Personas_3

    def Personas5Letras(self):
        '''Funcion que filtra por nombre o apellido con 5 letras exactas'''
        Lista_personas = []
        Cp = 0 #Contador personas
        for person in self.dic['person']:
            if len(person['first_name']) == 5 or len(person['last_name']) ==5:
                Lista_personas.append([])
                Lista_personas[Cp].append(person)
                Cp +=1
        return Lista_personas

    def ModificandoYaml(self):
        email = "---"
        dic_file = self.dic
        for person in dic_file['person']:
            person['email'] = email
        
        with open(r'updated.yml','w') as file:
            documents = Ym.dump(dic_file, file)

if __name__ == "__main__":
    with open('sample.yml') as file:
        data = Ym.load(file, Loader=Ym.FullLoader)

    InstanciaYaml = ManejandoYaml(data)

    print(f"Filtrando personas con id multiplo de 3: \n{InstanciaYaml.FiltroMultiplo3()}\n")
    print(f"Filtrando personas con 5 letras en nombre o apellido: \n{InstanciaYaml.Personas5Letras()}\n")
    InstanciaYaml.ModificandoYaml()