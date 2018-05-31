from bs4 import BeautifulSoup
import requests
                
class Usuario:
    
    #~ campos
    __username = ''
    __bio = ''
    __soup = ''
    __url = ''
    __lista_comunidades = []
    __userid = ''
    
    #~ constructor
    def __init__(self,url,username,userid):
        self.__username = username
        self.__soup = BeautifulSoup(requests.get(url).text,'lxml')
        self.__url = url
        self.__userid = userid

    #~ Métodos
    
    def get_userid(self):
        return self.__userid
        
    def get_username(self):
        return self.__username
    
    def get_bio(self):
        p = self.__soup.find(attrs = {'class': 'about'})
        self.__bio = p.contents[5].text
        return self.__bio
    
    def get_comunidades(self):
        r = requests.get(self.__url)
        texto = r.text
        x = BeautifulSoup(r.text, 'lxml')
        view_more = x.find(attrs = {'class':'view-more'})
        if view_more == None:
            comunidades = x.find_all(attrs = {'class':'community-name'})
            for i in comunidades:
                self.__lista_comunidades.append(i.text.strip())        
        elif view_more.text.find("View network profile") != -1:
            print(view_more.a['href'])
            r = requests.get(view_more.a['href'])
            texto = r.text
            x = BeautifulSoup(r.text,'lxml')
            comunidades = x.find_all(attrs = {'class':'account-site'})
            for i in comunidades:
                self.__lista_comunidades.append(i.a.text.strip())   
        else:
            comunidades = x.find_all(attrs = {'class':'community-name'})
            for i in comunidades:
                self.__lista_comunidades.append(i.text.strip())    
        return self.__lista_comunidades
    
    


            
    
    
        
    
    
