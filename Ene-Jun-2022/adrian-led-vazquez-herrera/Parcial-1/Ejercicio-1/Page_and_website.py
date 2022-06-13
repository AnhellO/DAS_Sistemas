#DAS 8vo semestre
#Parcial 1, E: 1 
#Page & Website classes

from __future__ import annotations
from abc import ABC, abstractmethod

class Component(ABC):
    #Clase componente para el método composite
    
    @abstractmethod
    def __init__(self, name, adress):
        self.Name=name
        self.Adress=adress
    
    def add(self, component: Component)->None:
        pass
    
    def remove(self, component: Component)->None:
        pass
    
    def is_composite(self)->bool:
        return False
    
    @abstractmethod
    def show(self):
        pass
    
class page(Component):
    
    def __init__(self, title, url, page_format, page_name):
        self.Name= title
        self.URL= url
        self.Format= page_format
        
        Header=self.set_header(page_name)
        Content=[]
        Footer=self.set_footer()
        Index={}
        
        self.Body={
            "header":Header,
            "content":Content,
            "index":Index,
            "footer":Footer}
        
    def add_content(self, title, text, image):
        #   Cada sección del contenido de una página será definido por estos valores
        #   Cada valor está designado con su etiqueta de HTML
        section={
            "<h1>":title,
            "<p>":text,
            "<img>":image}
        
        self.Body["content"].append(section)
        #   El índice será con el título de la sección
        # y el índice de la sección en la lista de contenido
        self.Body["index"][title]=(len(self.Body["content"])-1)
        
    def set_header(self, pag_name):
        
        #   Añadimos "CTA's" en el menú de navegación
        nav_menu=["home", "sections", "contact", "search bar"]
        #   La parte de "Login" es más como donde nos gustaría que estuviera
        # en la página, la parte de login está en otra sección del código
        head={
            "Page name":pag_name,
            "Nav menu": nav_menu,
            "Login": "login Button"}
        return head
        
    def set_footer(self):
        
        #   Añadimos links a las redes sociales
        redes=["Twitter", "Facebook"]
        foot={
            "Contact info":"dinosaurs@mails.com",
            "Redes": redes}
        return foot
    
    def show(self):
        page={
            "url":self.URL,
            "title":self.Name,
            "format":self.Format,
            "body":self.Body            
            }
        return (page)

    def get_name(self):
        return str(self.Name+" [page]")

    def is_composite(self)->bool:
        return False
        
class website(Component):

    def __init__(self, name, domain, subdomain, tipo)->None:
        self.Name=name
        self.Domain=domain
        self.Subdomain=subdomain
        self.Type=tipo
        self.HomePage=None
        self.children: List[Component]=[]
        self.homepage_flag=False

    def get_name(self):
        return self.show()

    #Método para obtener toda la colección de componentes del composite
    def get_collection(self):
        coll=[]
        for child in self.children:
            coll.append(child)
        return coll

    #Método que devuelve los hijos en string
    def get_collection_str(self):
        coll=[]
        for child in self.children:
            coll.append(child.get_name())
        return coll

    #Método para añadir componentes al composite
    def add(self, component: Component)->None:
        self.children.append(component)
    
    #Método para remover componentes del composite
    def remove(self, component: Component)->None:
        self.cildren.remove(component)
    
    #Método para saber si el objeto es composite u hoja
    def is_composite(self)->bool:
        return True

    #Seteamos una página de inicio (La página debe existir previamente)
    def set_homepage(self, component:Component)->None:
        if not self.homepage_flag:
            self.HomePage=component
            if component not in self.children:
                self.add(component)
            self.homepage_flag=True

        else:
            print("Home page already established")

    #Método de búsqueda interno que nos muestra la página en el sitio (Si existe)
    def search(self, name):
        for child in self.children:
            if child.get_name()==name:
                return child.show()
            else:
                return "Error 404: Page not found"

    #Muestra todos los datos del sitio
    def show(self):
        site={
            "name":self.Name,
            "domain":self.Domain,
            "subdomain":self.Subdomain,
            "content":self.get_collection_str()
            }
        if self.HomePage is None:
            site["homepage"]="None"
        else:
            site["homepage"]=self.HomePage.get_name()
        return (site)

#Método buscador que revisa si la página existe en el sitio
def searcher(site, targ):
    coll=site.get_collection()
    for thing in coll:
        if thing.is_composite():
            return(searcher(thing, targ))
        elif thing.get_name()[0:-7] == targ:
            return True
            
def search_start(wbsite, targ):
    if searcher(wbsite, targ):
        msg= "The page {fpage}, was found in the website {fsite}".format(fpage=targ, fsite=wbsite.Name)
        print(msg)
    else:
        msg="The page {fpage} does not exist in the website {fsite}.".format(fpage=targ, fsite=wbsite.Name)
        print(msg)  