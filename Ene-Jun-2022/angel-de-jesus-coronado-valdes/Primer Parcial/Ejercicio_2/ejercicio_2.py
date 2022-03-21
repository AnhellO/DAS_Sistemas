#from abc import ABC, abstractmethod

# Builder interface
# nuestra interfa Builder con los set de nuestra paguina y de nuestra web
class Builder():
    def reset(self):
        pass
    #------page--------
    # url
    def set_url(self, url):
        pass
    # name
    def set_name(self, name):
        pass
    # hyperlinks
    def set_hyperlinks(self, hyperlinks):
        pass
    # text
    def set_text(self, text):
        pass
    #tittle
    def set_tittle(self, tittle):
        pass
    # format
    def set_format(self, format):
        pass
    #metadescription
    def set_metadescription(self, metadescription):
        pass
    #sound
    def set_sound(self, sound):
        pass
    #video
    def set_video(self,video):
        pass
    #image
    def set_image(self,image):
        pass
    #-------------web------------------
    # domain
    def set_domain(self, domain):
        pass
    # page
    def set_page(self, page):
        pass
    # administrator
    def set_administrator(self, administrator):
        pass
    # menu
    def set_menu(self, menu):
        pass
    # chat
    def set_chat(self, chat):
        pass
    # catalogue
    def set_catalogue(self, catalogue):
        pass
    # map
    def set_map(self, map):
        pass
    # result
    def get_result(self):
        pass



# ConcreteBuilder page
#hereda de la interface builder los metodos de la paguina
class PageBuilder(Builder):
    #constructor instanciamos la clase paguina para su cofiguracion
    def __init__(self) -> None:
        self.pages = Page()
    
    #metodo reset para resetear la configuracion de la paguina
    def reset(self):
        self.pages = Page()
    
    # metodos set que nos va a obtener la información necesaria de dichas paguinas
    # url
    def set_url(self, url):
        self.pages.set_url(url)
    # name
    def set_name(self, name):
        self.pages.set_name(name)
    # hyperlinks
    def set_hyperlinks(self, hyperlinks):
        self.pages.set_hyperlinks(hyperlinks)
    # text
    def set_text(self, text):
        self.pages.set_text(text)
    #tittle
    def set_tittle(self, tittle):
        self.pages.set_tittle(tittle)
    # format
    def set_format(self, format):
        self.pages.set_format(format)
    #metadescription
    def set_metadescription(self, metadescription):
        self.pages.set_metadescription(metadescription)
    #sound
    def set_sound(self, sound):
        self.pages.set_sound(sound)
    #video
    def set_video(self,video):
        self.pages.set_video(video)
    #image
    def set_image(self,image):
        self.pages.set_image(image)
    # metodo get que nos retorna la estructura de nuestra paguina
    # result
    def get_result(self):
        return self.pages

# ConcreteBuilder 2
#hereda de la interface builder los metodos de la website
class WebSiteBuilder(Builder):
    # el contructor instancia la clase website para sus configuraciónes
    def __init__(self) -> None:
        self.website = Website()
    
    #metodo reset para resetear el sitio web
    def reset(self):
        self.website = Website()
    
    # metodos set para obtener la información del sitio web
    # domain
    def set_domain(self, domain):
        self.website.set_domain(domain)
    # page
    def set_page(self, page):
        self.website.set_page(page)
    # administrator
    def set_administrator(self, administrator):
        self.website.set_administrator(administrator)
    # menu
    def set_menu(self, menu):
        self.website.set_menu(menu)
    # chat
    def set_chat(self, chat):
        self.website.set_chat(chat)
    # catalogue
    def set_catalogue(self, catalogue):
        self.website.set_catalogue(catalogue)
    # map
    def set_map(self, map):
        self.website.set_map(map)
    
    #metodpo get que nos retorna la structura de nuestra web
    def get_result(self):
        return self.website
    


# Product
# clase page 
class Page:
    #constructor recivimos los parametros de los atributos de la paguina web y defaul son None
    def __init__(self,url=None,name=None,hyperlinks=None,text=None,tittle=None,format=None,metadescription=None,sound=None,video=None,image=None) -> None:
        self.url = url
        self.name = name
        self.hyperlinks = hyperlinks
        self.text = text
        self.tittle = tittle
        self.format = format
        self.metadescription = metadescription
        self.sound = sound
        self.video = video
        self.image = image
    
    # se guardan los dados introduciodos  en cada metodo set
    # url
    def set_url(self, url):
        self.url = url

    # name
    def set_name(self, name):
        self.name = name

    # hyperlinks
    def set_hyperlinks(self, hyperlinks):
        self.hyperlinks = hyperlinks

    # text
    def set_text(self, text):
        self.text = text

    #tittle
    def set_tittle(self, tittle):
        self.tittle = tittle

    # format
    def set_format(self, format):
        self.format = format

    #metadescription
    def set_metadescription(self, metadescription):
        self.metadescription = metadescription

    #sound
    def set_sound(self, sound):
        self.sound = sound

    #video
    def set_video(self,video):
        self.video = video

    #image
    def set_image(self,image):
        self.image = image
    
    # retornamos en el metodo str la estructura de la paguina web
    def __str__(self) -> str:
        return f"\nURL: {self.url}\nNAME: {self.name}\nHYPERLINKS: {self.hyperlinks}\nTEXT: {self.text}\nTITLE: {self.tittle}\nFORMAT: {self.format}\nMETADESCRIPTION: {self.metadescription}\nSOUND: {self.sound}\nVIDEO: {self.video}\nIMAGE: {self.image}\n"

# Product
# sitio web 
class Website:
    # en el constructor resivimos los valores del sitio web y en un atributo su paguinas
    # por defaul los valores son None
    def __init__(self,domain=None, page=None, administrator=None, menu=None, chat=None, catalogue=None, map=None) -> None:
        self.domain = domain
        self.page = page
        self.administrator = administrator
        self.menu = menu
        self.chat = chat
        self.catalogue = catalogue
        self.map = map
        self.chosenpage = None
    
    # para cada metodo set se guardan la informacion que se obtuvo
    # domain
    def set_domain(self, domain):
        self.domain = domain
    # page
    def set_page(self, page):
        self.page = page
    # administrator
    def set_administrator(self, administrator):
        self.administrator = administrator
    # menu
    def set_menu(self, menu):
        self.menu = menu
    # chat
    def set_chat(self, chat):
        self.chat = chat
    # catalogue
    def set_catalogue(self, catalogue):
        self.catalogue = catalogue
    # map
    def set_map(self, map):
        self.map = map
    
    # metodo que me retorna mi sitio web y me muestra la paguina buscada
    def __str__(self) -> str:
        return f"My Web Site is\nDOMAIN: {self.domain}\n\n[ PAGE WEB ]{ self.chosenpage}\nADMIN: {self.administrator}\nMENU: {self.menu}\nCHAT: {self.chat}\nCATALOGUE: {self.catalogue}\nMAPA: {self.map}"



# Director
class Director:
    # resivimos en el contrucstor el builder para realizar cambios de builder etc
    def __init__(self, builder: Builder) -> None:
        self.builder = builder
    
    # metodo para cambiar el builder
    def changebuilder(self, builder: Builder):
        self.builder = builder
    
    # Configuración page
    def makePage(self,url:str,name:str,hyperlinks:str,text:str,title:str,format:str,metadescription:str,sound:str,video:str,image:str) -> str:
        # por medio de este metodo makePage se realiza a mandar la infromacion por los metodos set
        #utilizando el builder que se asigno en el constructor
        self.builder.set_url(url)
        self.builder.set_name(name)
        self.builder.set_hyperlinks(hyperlinks)
        self.builder.set_text(text)
        self.builder.set_tittle(title)
        self.builder.set_format(format)
        self.builder.set_metadescription(metadescription)
        self.builder.set_sound(sound)
        self.builder.set_video(video)
        self.builder.set_image(image)
        # retornamos el resultado
        return self.builder.get_result()

    # Configuración web
    def makeWeb(self,domain:str, page:Page, administrator:str, menu:str, chat:str, catalogue:str, map:str) -> str:
         # por medio de este metodo makeWeb se realiza a mandar la infromacion por los metodos set
        #utilizando el builder que se asigno en el constructor
        self.builder.set_domain(domain)
        self.builder.set_page(page)
        self.builder.set_administrator(administrator)
        self.builder.set_menu(menu)
        self.builder.set_chat(chat)
        self.builder.set_catalogue(catalogue)
        self.builder.set_map(map)
        #retornamos el resultado
        return self.builder.get_result()



# clase seeker, es un buscador de paguinas web de un sitio
class Seeker:
    # constructor que resive 4 parametros "uno de tipo 'website' o tro de tipo 'page'" y dos parametros más
    # uno que es el dominio de nuestro sitio web y el otro que es la paguina que seleccionamos
    def __init__(self, websitelist:Website, pagelist:Page, seekerwebsite:str, seekerpage:str) -> None:
        self.websitelist = websitelist
        self.pagelist = pagelist
        self.seekerwebsite = seekerwebsite
        self.seekerpage = seekerpage
    
    # metodo seeker, busca en una lista de sistios web y una lista de sistios
    def seekerweb(self):
        countweb = 0 # contador del sitio web
        countpage = 0 # contador de paguinas web
        # recorre una lista de sitios web y compara si ese sitio existe
        for web in self.websitelist:
            countweb += 1
            if web.domain == self.seekerwebsite:
                # si se encuentra el sitio web
                # comienza la busqueda de la paguina web si es que existe en el sitio web
                for pages in self.pagelist:
            
                    for i in range(len(pages)):
                        countpage += 1
                        if web.page[i].name == self.seekerpage:
                            # si existe la paguina la posicion de la paguina seleccionada se pasa al parametro chosenpage
                            # se agrega al sitio web la paguina solicitada y la retornamos para imprimir la información del sitio y de la paguina
                            web.chosenpage = web.page[i]
                            return web
                        # si la paguina web no existe y si el contador de recorrido de la paguina es igual a la lista 
                        # ya recorridas entonces no existe la paguina
                        elif web.page[i].name != self.seekerpage and countpage == len(pages):
                            return "PAGE NOT FOUND"
            # si el sitio web no existe y si el contador de recorrido del sitio web es igual a la lista 
            # ya recorridas entonces no existe el sitio web
            elif web.domain != self.seekerwebsite and countweb == len(self.websitelist):
                return "SITE NOT FOUND"
   


def main():
    directorpage = []# se crea una lista directorpage para almasenar diferentes paguinas web
    # agregamos en cada iteración del for en este caso son 15 la instancia de Page Builder
    # y se agrega esa instancia almacenada en una variable en la clase Director ya que requiere el builder como parametro
    for i in range(15): 
        pagebuilder = PageBuilder()
        directorpage.append(Director(pagebuilder))
    # en la lista page se almacenan las 15 paguinas web como en subarreglos para identificar que son 3 sitios web diferentes
    page = [
        [
            directorpage[0].makePage("https://www.angel.com/init","init","<a href= 'https://www.youtube.com' target='_blank'> YOUTUBE </a>","<p> my first page web </p>","<h3> world </h3>","<p> html </p>","<p> my web site </p>","<audio> en el rio-arcadia libre.mp3 </audio>","<video> hello.mp4 </video>","<img src= 'my.png'>"),
            directorpage[1].makePage("https://www.angel.com/logi","logi","<a href= 'https://www.facebook.com' target='_blank'> FACEBOOK </a>","<p> this is facebook </p>","<h3> hello </h3>","<p> html </p>","<p> my web site </p>","<audio> hello.mp3 </audio>","<video> hello.mp4 </video>","<img src='hoooo.png'>"),
            directorpage[2].makePage("https://www.angel.com/menu","menu","<a href= 'https://www.yahoo.com' target='_blank'> YAHOO </a>","<p> this is yahoo </p>","<h3> poom </h3>","<p> html </p>","<p> my web site </p>","<audio> nana pancha.mp3 </audio>","<video> my friends.mp4 </video>","<img src= 'hellsing.png'>"),
            directorpage[3].makePage("https://www.angel.com/catalog","catalogo","<a href= 'https://www.twitter.com' target='_blank'> TWTTER </a>","<p> this is twitter </p>","<h3> arcadia libre </h3>","<p> html </p>","<p> my web site </p>","<audio> menos yo-sekta core.mp3 </audio>","<video> hello.mp4 </video>","<img src= 'onepuchman.png'>"),
            directorpage[4].makePage("https://www.angel.com/maps","maps","<a href= 'https://www.python.com' target='_blank'> PYTHON </a>","<p> this is python </p>","<h3> world </h3>","<p> html </p>","<p> my web site </p>","<audio> experts.mp3 </audio>","<video> parkour.mp4 </video>","<img src= 'my.png'>"),
        ],
        [
            directorpage[5].makePage("https://www.spiders.com/initspider","initspider","<a href= 'https://www.youtube.com' target='_blank'> YOUTUBE </a>","<p> page web </p>","<h3> world </h3>","<p> html </p>","<p> my web site </p>","<audio> sound.mp3 </audio>","<video> my spiderworld.mp4 </video>","<img src= 'Lycosidae.png'>"),
            directorpage[6].makePage("https://www.spiders.com/logispider","logispider","<a href= 'https://www.facebook.com' target='_blank'> FACEBOOK </a>","<p> this is facebook </p>","<h3> Json </h3>","<p> javaScript </p>","<p> web site </p>","<audio> mysound.mp3 </audio>","<video> documents.mp4 </video>","<img src= 'salticidae.png'>"),
            directorpage[7].makePage("https://www.spiders.com/menuspider","menuspider","<a href= 'https://www.yahoo.com' target='_blank'> YAHOO </a>","<p> this is yahoo </p>","<h3> poom </h3>","<p> php </p>","<p> spider menu </p>","<audio> description.mp3 </audio>","<video> expert.mp4 </video>","<img src= 'salticidaess66.png'>"),
            directorpage[8].makePage("https://www.spiders.com/catalogospider","catalogospider","<a href= 'https://www.twitter.com' target='_blank'> TWITTER </a>","<p> this is twitter </p>","<h3> catalogue </h3>","<p> xml </p>","<audio> cantalogue of spider </p>","the world.mp3 </audio>","<video> hello.mp4 </video>","<img src= 'one.png'>"),
            directorpage[9].makePage("https://www.spiders.com/mapspider","mapspider","<a href= 'https://www.spidersmuch.com' target='_blank'> SPIDERSMUCH </a>","<p> this is spidersmuch </p>","<h3> spidersmuch it is the best page of spiders </h3>","<p> php </p>","<p> description </p>","<audio> helloworld.mp3 </audio>","<video> spidersmuch.mp4 </video>","<img src= 'spidersmuch33.png'>"),
        ],
        [
            directorpage[10].makePage("https://www.ghots.com/initghots","initghots","<a href= 'https://www.youtube.com' target='_blank'> YOUTUBE </a>","<p> this is video of ghots </p>","<h3> ghots world </h3>","<p> php </p>","<p> page of ghots </p>","<audio> soundghots.mp3 </audio>","<video> evidents.mp4 </video>","<img src= 'ghost_in_my_house.png'>"),
            directorpage[11].makePage("https://www.ghots.com/logighots","logighots","<a href= 'https://www.facebook.com' target='_blank'> FACEBOOK </a>","<p> this is we facebook page </p>","<h3> ghotsland </h3>","<p> php </p>","<p> page of images </p>","<audio> sound2.mp3 </audio>","<video> ghots.mp4 </video>","<img src= 'graveyard.png'>"),
            directorpage[12].makePage("https://www.ghots.com/menughots","menughots","<a href= 'https://www.yahoo.com' target='_blank'> YAHOO </a>","<p> this is yahoo </p>","<h3> description my web page </h3>","<p> php </p>","<p> my web site of ghots </p>","<audio> booh.mp3 </audio>","<video> ghots_in_graveyard.mp4 </video>","<img src= 'evil.png'>"),
            directorpage[13].makePage("https://www.ghots.com/catalogoghots","catalogoghots","<a href= 'https://www.twitter.com' target='_blank'> TWITTER </a>","<p> this is twitter </p>","<h3> animals </h3>","<p> php </p>","<p> ghots and animal </p>","<audio> animals.mp3 </audio>","<video> dogs.mp4 </video>","<img src= 'dog_with_ghots.png'>"),
            directorpage[14].makePage("https://www.ghots.com/mapsghots","mapsghots","<a href= 'https://www.ghotsll33.com' target='_blank'> GHOTSLL33 </a>","<p> this is ghotsll33 </p>","<h3> ghotsll33 </h3>","<p> php </p>","<p> my web site ghotsll33 </p>","<audio> ghotsll33.mp3 </audio>","<video> ghotsll33.mp4 </video>","<img src= 'ghotsll33.png'>"),
        ]
    ]
    
    directorweb = []# se crea una lista directorweb para almasenar diferentes sitios web
    # agregamos en cada iteración del for en este caso son 3 la instancia de WebsiteBuilder
    # y se agrega esa instancia almacenada en una variable en la clase Director ya que requiere el builder como parametro
    for i in range(3):
        websitebuilder = WebSiteBuilder()
        directorweb.append(Director(websitebuilder))
    # y alamcenamos en una lista website la instancia de nuestro directoer web
    website = [
        directorweb[0].makeWeb("https://www.angel.com",page[0],"angel","my option","wechat","catalogue of work","yourmaps"),
        directorweb[1].makeWeb("https://www.spiders.com",page[1],"the spiders","spiders of world","spider-chat","catalogue of spiders","spiders-maps"),
        directorweb[2].makeWeb("https://www.ghots.com",page[2],"ghots","ghots","ghots-chat","catalogue of ghots","ghots-maps")
    ]
    
    # instanciamos la clase Seeker y mandandole los parametros website, page, el dominio y el nombre de la paguina
    seeker = Seeker(website, page, "https://www.ghots.com","mapsghots")
    # imprimimos el resultado esperado
    webprint = seeker.seekerweb()
    print(webprint)
    
    
if __name__ == "__main__":
    main()