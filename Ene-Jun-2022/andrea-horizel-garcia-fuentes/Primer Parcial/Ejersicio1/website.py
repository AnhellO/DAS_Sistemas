

class Website:
    def __init__ (self, URL,dominio,subdominio,servidorweb,paginaweb,motordebusqueda,sitioweb):
        self.URL = URL
        self.dominio = dominio
        self.subdominio =subdominio
        self.servidorweb = servidorweb
        self.paginaweb = paginaweb
        self.motordebusqueda = motordebusqueda
        self.sitioweb = sitioweb
    
    #Metodo 
    def getURL(self):
        return self.URL
    
    def setURL(self,URL):
        self.URL = URL
        

    def getDominio(self):
        return self.dominio
    
    def setDominio(self,dominio):
        self.dominio = dominio

    def getSubdominio(self):
        return self.subdominio
    
    def setSubdominio(self,subdominio):
        self.subdominio = subdominio
    
    def getServidorweb(self):
        return self.servidorweb
    
    def setServidorweb(self,servidorweb):
        self.servidorweb = servidorweb
    
    def getPaginaweb(self):
        return self.paginaweb
    
    def setPaginaweb(self,paginaweb):
        self.paginaweb = paginaweb

    def getMotordebusqueda(self):
        return self.motordebusqueda
    
    def setMotordebusqueda(self,motordebusqueda):
        self.motordebusqueda = motordebusqueda
    
    def getSitioweb(self):
        return self.sitioweb

    def setSitioweb(self,sitioweb):
        self.sitioweb = sitioweb
    
    def __str__(self):
        mensaje  = "\n* URL: " + self.URL
        mensaje += "\n* dominio: " + self.dominio
        mensaje += "\n* subdominio: " + self.subdominio
        mensaje += "\n* servidorweb " + self.servidorweb
        mensaje += "\n* paginaweb: " + str(self.paginaweb)
        mensaje += "\n* motordebusqueda: " + self.motordebusqueda
        mensaje += "\n* sitioweb: " + self.sitioweb
        return mensaje 
    