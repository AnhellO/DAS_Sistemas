from Page import Page
class Website(Page):
    def __init__(self, dominio, subdom, paginas: list):
        self.dominio = dominio
        self.subdom = subdom
        self.paginas = paginas
    
    #GET & SET
    def set_dominio(self, dominio):
        self.dominio = dominio
    def get_dominio(self):
        return self.dominio
    def set_subdom(self, subdom):
        self.subdom = subdom
    def get_subdom(self):
        return self.subdom
    #AGREGA PAGINAS A LA LISTA
    def add_paginas(self, Page):
        self.paginas.append(Page)
    def get_paginas(self):
        return self.paginas
    
      #FUNCION BUSCADOR VERIFICA SI LA PAGINA INDICADA SE ENCUENTRA EN LA LISTA DE LAS PAGINAS ALMACENADAS.
    def search(self, pagina=''):
        if pagina in self.paginas:
            print('--- Pagina Encontrada! :D ---')
            print(pagina)
        else:
            print('Pagina no Encontrada! :c')
            
            
                             