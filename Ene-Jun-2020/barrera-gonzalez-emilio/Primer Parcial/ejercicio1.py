class Page(object):
    def __init__(self, url: str, path: str, links: list, pars: list, title: str):
        self.url = url
        self.path = path
        self.links = links
        self.pars = pars
        self.title = title

    def set_url(self,url):
        self.url = url
    def set_path(self,path):
        self.path = path
    def add_link(self,link):
        self.links.append(link)
    def set_title(self,title):
        self.title = title
    def add_par(self,par):
        self.pars.append(par)
    
    def del_link(self,link):
        try:
            links.remove(link)   
        except:
            return f"No se puedo borrar {link}\n inexistente?"
        return f"{link} ha sido removido con exito"
    def del_par(self,par):
        try:
            pars.remove(par)
        except:
            return f"No se puedo borrar {par}\n parrafo inexistente?"
        return f"{par} ha sido removido con exito"

    def get_url(self):
        return self.url
    def get_path(self):
        return self.path
    def get_links(self):
        return self.link
    def get_title(self):
        return self.title
    def get_pars(self):
        return self.pars
    
    def __str__(self):
        r=f"path: {self.path}"
        r+=f"\nurl: {self.url}"
        r+=f"\ntitle: {self.title}"
        r+=f"\npars: {self.pars}"
        r+=f"\nlinks: {self.links}"
        return r

class Website(Page):
    def __init__(self, domain:str, subdomains: list, pages: list):
        self.domain=domain
        self.subdomains=subdomains
        self.pages=pages
    
    def rename_domain(self, dom):
        self.domain=dom
    def add_subdomain(self, sub):
        self.subdomains.append(sub)
    def add_page(self, page):
        self.pages.append(page)
    
    def del_sub(self,subs):
        try:
            self.subdomains.remove(subs)
        except:
            return f"{subs} ha sido eliminado"
        return f"{subs} no ha podido ser eliminado\n inexistente?"
    def del_page(self,page):
        try:
            self.pages.remove(page)
        except:
            return f"{page} ha sido eliminado"
        return f"{page} no ha podido ser eliminado\n inexistente?"

    def __str__(self):
        r=f"Domain:{self.domain}"
        r+=f"\nsubDomains:{self.subdomains}"
        r+="\nPAGINAS:\n"
        for i in self.pages:
            r+="############\n"
            r+=f"{i}"
            r+="\n"
        return r

def main():
    ##PRUEBA DE FUNCIONALIDAD DE LA CLASE "PAGE"##
    links=["www.facebook.com","www.twitter.com"]
    pars=["Hola",
          "me",  
          "llamo asi"]
    pagina1=Page("github.com/emiliobg1997","/index.html",links,pars, "My repo")


    links=["google.com","youtube.com"]
    pars=["Hola",
          "me",  
          "llamo asa"]
    pagina2=Page("github.com/lufergamo2502","/index.html",links,pars, "his repo")

    links=["xda-devs.com","linkedin.com"]
    pars=["Hola",
          "me",  
          "llamo ase"]
    pagina3=Page("github.com/asanchez","/index.html",links,pars, "her repo")

    ##PRUEBA DE FUNCIONALIDAD DE LA CLASE "websites"
    domain="github.com"
    subdomains=["subgit","sub2"]
    pags=[pagina1,pagina2,pagina3]
    web=Website(domain,subdomains,pags)
    print(web)
    ##

if __name__=="__main__":
    main()