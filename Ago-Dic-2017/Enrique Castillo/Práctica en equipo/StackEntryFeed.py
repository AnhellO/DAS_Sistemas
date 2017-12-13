from bs4 import BeautifulSoup
import requests
import feedparser
class  StackEntryFeed():
    #~ campos
    
    __pregunta = ''
    __usuario = ''
    __url = ''
    __idPregunta  = ''
    __entry = ''

#~ Constructor
    def __init__(self,entry):
        self.__entry = entry
        self.__pregunta = ''
        self.__usuario = ''
        self.__url = ''
        self.__idPregunta  = ''
    
    
    #~ Métodos
    def get_entry_link(self):
        return self.__entry.id
       
    def get_id(self):
        string = self.__entry.id
        identry = ''
        for i in string:
            if i.isnumeric():
                identry+=i
        return identry    
    
    def get_title(self):
        return self.__entry.title_detail.value
    
    #~ Bajo sospecha
    def get_summary_detail(self):
        sumary = BeautifulSoup(self.__entry.summary_detail.value,'lxml')
        return sumary.text
    
    def get_username(self):
        return self.__entry.author_detail.name
    
    def get_user_uri(self):
        return self.__entry.author_detail.href
    
    def get_user_id(self):
        string = self.__entry.author_detail.href
        idUsuario = ''
        for i in string:
            if i.isnumeric():
                idUsuario+=i
        return idUsuario

    def get_fecha_publicacion(self):
        return self.__entry.published
    
    
    
        
