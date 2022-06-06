import json
import requests
from requests.auth import HTTPBasicAuth
from db import app

class apiApp:
    def __init__(self,url,user,token):   
        self.url = url     
        self.user = user
        self.token = token
        self.response = None
        self.appDB = app()      # Objeto de tipo db, que nos ayudará a conectarnos a la DB

    # Hace la petición
    def getResponse(self):
        self.response = requests.get(url=self.url,auth=HTTPBasicAuth(self.user,self.token))

    # Crea y agurda en mongo una lista de todos los issues
    def listIssues(self):        
        self.appDB.setCollection('issues') 
        
        self.getResponse()  
        r = json.loads(self.response.content)        
        numIssues = r[0]['number']      # Número total de issues            
        form = {}
        self.appDB.eliminar()   # Se eliminan los registros de la colección

        for i in range(numIssues):
            self.url = f"https://api.github.com/repos/pallets/flask/issues/{i+1}"
            self.getResponse()
            r = json.loads(self.response.content)
            form['_id'] = (i+1)
            for key,value in r.items():
                if key == 'number':
                    continue
                form[key] = value
            self.appDB.insertar(form)    # Ahora se inserta el contenido del diccionario dentro de la DB           

        print(f"Registros agregados a la colección ")
    

        
#MAIN 
if __name__ == '__main__':    
    # URL de donde va a hacer la petición get
    url = 'https://api.github.com/repos/pallets/flask/issues'
    user = 'JuanAlejandroCR'
    token = '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'

        
    # Objeto de la api
    newApi = apiApp(url, user, token)

    newApi.listIssues()    