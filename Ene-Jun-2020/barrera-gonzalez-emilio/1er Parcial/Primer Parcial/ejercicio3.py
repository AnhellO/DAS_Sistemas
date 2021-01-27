from ejercicio1 import Page
import abc

class ResponseStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def response(self):
        pass

class xmlConcreteStrategy(ResponseStrategy,):
    def response(self,pagina):
        r="RESPONSE AS XML:"
        r+=f"\nType:{pagina.typo}"
        r+=f"\nContent:{pagina.pars}\n{pagina.links}"
        return r

class htmlConcreteStrategy(ResponseStrategy):
    def response(self,pagina):
        r="RESPONSE AS HTML"
        r+=f"\nType:{pagina.typo}"
        r+=f"\nContent:{pagina.pars}\n{pagina.links}"
        return r

class jsonConcreteStrategy(ResponseStrategy):
    def response(self,pagina):
        r="RESPONSE AS JSON:"
        r+=f"\nType:{pagina.typo}"
        r+=f"\nContent:{pagina.pars}\n{pagina.links}"
        return r

class ResponseContext(object):
    def __init__(self, pagina):
        self._pagina=pagina
    def responseContext(self):
        if self._pagina.typo=="xml":
            return xmlConcreteStrategy.response(self,self._pagina)
        elif self._pagina.typo=="html":
            return htmlConcreteStrategy.response(self,self._pagina)
        elif self._pagina.typo=="json":
            return jsonConcreteStrategy.response(self,self._pagina)
        else:
            return "NO HAY UNA ESTRATEGIA"
    def __str__(self):
        return f"Pagina:{self.pagina}"

    
def main():
     ##PRUEBA DE FUNCIONALIDAD DE LA CLASE "PAGE"##
    links=["www.facebook.com","www.twitter.com"]
    pars=["<p>Hola</p>",
          "<p>me</p>",  
          "<p>llamo así</p>"]
    pagina1=Page("github.com/emiliobg1997","/index.html",links,pars, "My repo","html")
    rescontext=ResponseContext(pagina1)
    print(rescontext.responseContext())
    links=["www.capcom.com","www.blizzard.com"]
    pars=["<p>Hola</p>",
          "<p>me</p>",  
          "<p>llamo así</p>"]
    pagina2=Page("github.com/heavyduty","/index.html",links,pars, "My repo","json")
    print("############################")
    rescontext=ResponseContext(pagina2)
    print(rescontext.responseContext())
    print("############################")
    links=["www.youtube.com","www.bnha.com"]
    pars=["<p>Hola</p>",
          "<p>me</p>",  
          "<p>llamo así</p>"]
    pagina3=Page("github.com/","/index.html",links,pars, "My repo","xml")
    rescontext=ResponseContext(pagina3)
    print(rescontext.responseContext())
    print("############################")
    links=["www.fmab.com","www.dbs.com"]
    pars=["<p>Hola</p>",
          "<p>me</p>",  
          "<p>llamo así</p>"]
    pagina3=Page("github.com/kof2002um","/index.html",links,pars, "My repo","php")
    rescontext=ResponseContext(pagina3)
    print(rescontext.responseContext())

    


    

if __name__=="__main__":
    main()