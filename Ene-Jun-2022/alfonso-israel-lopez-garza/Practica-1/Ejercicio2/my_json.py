import json

class ManejoJson:
    def __init__(self,Data) -> None:
        self.Dic = Data['people']

    def FiltroImpares(self):
        CI = 0
        PersonasImpares = []
        for persona in self.Dic['person']:
            if int(persona['id']) % 2 != 0:
                PersonasImpares.append([])
                PersonasImpares[CI].append(persona)
                CI += 1
        return PersonasImpares

    def FiltroLongitudCompañoa(self):
        Cc = 0
        PersonasCompañia = []
        for persona in self.Dic['person']:
            if len(persona['company']) >=4 and len(persona['company']) <=6:
                PersonasCompañia.append([])
                PersonasCompañia[Cc].append(persona)
                Cc += 1
        return PersonasCompañia

    def ModificarJson(self):
        file = self.Dic
        phone_number = "xx-xx-xxx"
        for person in file['person']:
            person['phone_number'] = phone_number
        
        with open('updated.json','w') as f:
            json.dump(file,f)

if __name__ == "__main__":
    with open('sample.json') as file:
        data = json.load(file)
        InstanciaJson = ManejoJson(data)
        print(f"Personas con id impar: \n{InstanciaJson.FiltroImpares()}\n")
        print(f"Personas en una compañia con nombre entre 4 y 6 letras: \n{InstanciaJson.FiltroLongitudCompañoa()}\n")
        InstanciaJson.ModificarJson()