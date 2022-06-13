# clase page que recibe 10 atributos de una paguina web 
class Page:
    #constructor recivimos los parametros de los atributos de la paguina web
    def __init__(self,url:str,name:str,hipervinculos:str,texto:str,titulo:str,formato:str,metadescripcion:str,sonido:str,video:str,imagenes:str) -> None:
        self.url = url
        self.name = name
        self.hipervinculos = hipervinculos
        self.texto = texto
        self.titulo = titulo
        self.formato = formato
        self.metadescripcion = metadescripcion
        self.sonido = sonido
        self.video = video
        self.imagenes = imagenes
    
    # metodo que nos retorna una estructura de nuestra paguina web
    def __str__(self) -> str:
        return f"\nURL: {self.url}\nNAME: {self.name}\nHYPERLINKS: {self.hipervinculos}\nTEXT: {self.texto}\nTITLE: {self.titulo}\nFORMAT: {self.formato}\nMETADESCRIPTION: {self.metadescripcion}\nSOUND: {self.sonido}\nVIDEO: {self.video}\nIMAGE: {self.imagenes}\n"

# clase website que recibe 7 parametros minimo de atributos que contiene un sitio web
class Website:
    # constructor que recibe los parametros del sitio web "recibe un parametro de tipo 'Page' que nos imprime el contenido de la paguina"
    def __init__(self,dominio:str, page:Page, administrador:str, menu:str, chat:str, catalogo:str, mapa:str) -> None:
        self.dominio = dominio
        self.page = page
        self.administrador = administrador
        self.menu = menu
        self.chat = chat
        self.catalogo = catalogo
        self.mapa = mapa
        self.chosenpage = ""
        
    # metodo que me retorna mi sitio web y me muestra la paguina buscada
    def __str__(self) -> str:
        return f"My Web Site is\nDOMAIN: {self.dominio}\n\n[ PAGE WEB ]{self.chosenpage}\nADMIN: {self.administrador}\nMENU: {self.menu}\nCHAT: {self.chat}\nCATALOGUE: {self.catalogo}\nMAPA: {self.mapa}"


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
            if web.dominio == self.seekerwebsite:
                # si se encuentra el sitio web
                # comienza la busqueda de la paguina web si es que existe en el sitio web
                for i in range (len(self.pagelist)):
                    countpage += 1
                    pages = self.pagelist[i]
                    if web.page[i].name == self.seekerpage:
                        # si existe la paguina la posicion de la paguina seleccionada se pasa al parametro chosenpage
                        # se agrega al sitio web la paguina solicitada y la retornamos para imprimir la información del sitio y de la paguina
                        web.chosenpage = web.page[i]
                        return web
                    # si la paguina web no existe y si el contador de recorrido de la paguina es igual a la lista 
                    # ya recorridas entonces no existe la paguina
                    elif web.page[i].name != self.seekerpage and countpage == len(self.pagelist):
                        return "PAGE NOT FOUND"
            # si el sitio web no existe y si el contador de recorrido del sitio web es igual a la lista 
            # ya recorridas entonces no existe el sitio web
            elif web.dominio != self.seekerwebsite and countweb == len(self.websitelist):
                return "SITE NOT FOUND"

# funcion main         
def main():
    # lista de paguinas web 
    page = [
        [
            Page("https://www.angel.com/init","init","<a href= 'https://www.youtube.com' target='_blank'> YOUTUBE </a>","<p> my first page web </p>","<h3> world </h3>","<p> html </p>","<p> my web site </p>","<audio> en el rio-arcadia libre.mp3 </audio>","<video> hello.mp4 </video>","<img src= 'my.png'>"),
            Page("https://www.angel.com/logi","logi","<a href= 'https://www.facebook.com' target='_blank'> FACEBOOK </a>","<p> this is facebook </p>","<h3> hello </h3>","<p> html </p>","<p> my web site </p>","<audio> hello.mp3 </audio>","<video> hello.mp4 </video>","<img src='hoooo.png'>"),
            Page("https://www.angel.com/menu","menu","<a href= 'https://www.yahoo.com' target='_blank'> YAHOO </a>","<p> this is yahoo </p>","<h3> poom </h3>","<p> html </p>","<p> my web site </p>","<audio> nana pancha.mp3 </audio>","<video> my friends.mp4 </video>","<img src= 'hellsing.png'>"),
            Page("https://www.angel.com/catalog","catalogo","<a href= 'https://www.twitter.com' target='_blank'> TWTTER </a>","<p> this is twitter </p>","<h3> arcadia libre </h3>","<p> html </p>","<p> my web site </p>","<audio> menos yo-sekta core.mp3 </audio>","<video> hello.mp4 </video>","<img src= 'onepuchman.png'>"),
            Page("https://www.angel.com/maps","maps","<a href= 'https://www.python.com' target='_blank'> PYTHON </a>","<p> this is python </p>","<h3> world </h3>","<p> html </p>","<p> my web site </p>","<audio> experts.mp3 </audio>","<video> parkour.mp4 </video>","<img src= 'my.png'>"),
        ],
        [
            Page("https://www.spiders.com/initspider","initspider","<a href= 'https://www.youtube.com' target='_blank'> YOUTUBE </a>","<p> page web </p>","<h3> world </h3>","<p> html </p>","<p> my web site </p>","<audio> sound.mp3 </audio>","<video> my spiderworld.mp4 </video>","<img src= 'Lycosidae.png'>"),
            Page("https://www.spiders.com/logispider","logispider","<a href= 'https://www.facebook.com' target='_blank'> FACEBOOK </a>","<p> this is facebook </p>","<h3> Json </h3>","<p> javaScript </p>","<p> web site </p>","<audio> mysound.mp3 </audio>","<video> documents.mp4 </video>","<img src= 'salticidae.png'>"),
            Page("https://www.spiders.com/menuspider","menuspider","<a href= 'https://www.yahoo.com' target='_blank'> YAHOO </a>","<p> this is yahoo </p>","<h3> poom </h3>","<p> php </p>","<p> spider menu </p>","<audio> description.mp3 </audio>","<video> expert.mp4 </video>","<img src= 'salticidaess66.png'>"),
            Page("https://www.spiders.com/catalogospider","catalogospider","<a href= 'https://www.twitter.com' target='_blank'> TWITTER </a>","<p> this is twitter </p>","<h3> catalogue </h3>","<p> xml </p>","<audio> cantalogue of spider </p>","the world.mp3 </audio>","<video> hello.mp4 </video>","<img src= 'one.png'>"),
            Page("https://www.spiders.com/mapspider","mapspider","<a href= 'https://www.spidersmuch.com' target='_blank'> SPIDERSMUCH </a>","<p> this is spidersmuch </p>","<h3> spidersmuch it is the best page of spiders </h3>","<p> php </p>","<p> description </p>","<audio> helloworld.mp3 </audio>","<video> spidersmuch.mp4 </video>","<img src= 'spidersmuch33.png'>"),
        ],
        [
            Page("https://www.ghots.com/initghots","initghots","<a href= 'https://www.youtube.com' target='_blank'> YOUTUBE </a>","<p> this is video of ghots </p>","<h3> ghots world </h3>","<p> php </p>","<p> page of ghots </p>","<audio> soundghots.mp3 </audio>","<video> evidents.mp4 </video>","<img src= 'ghost_in_my_house.png'>"),
            Page("https://www.ghots.com/logighots","logighots","<a href= 'https://www.facebook.com' target='_blank'> FACEBOOK </a>","<p> this is we facebook page </p>","<h3> ghotsland </h3>","<p> php </p>","<p> page of images </p>","<audio> sound2.mp3 </audio>","<video> ghots.mp4 </video>","<img src= 'graveyard.png'>"),
            Page("https://www.ghots.com/menughots","menughots","<a href= 'https://www.yahoo.com' target='_blank'> YAHOO </a>","<p> this is yahoo </p>","<h3> description my web page </h3>","<p> php </p>","<p> my web site of ghots </p>","<audio> booh.mp3 </audio>","<video> ghots_in_graveyard.mp4 </video>","<img src= 'evil.png'>"),
            Page("https://www.ghots.com/catalogoghots","catalogoghots","<a href= 'https://www.twitter.com' target='_blank'> TWITTER </a>","<p> this is twitter </p>","<h3> animals </h3>","<p> php </p>","<p> ghots and animal </p>","<audio> animals.mp3 </audio>","<video> dogs.mp4 </video>","<img src= 'dog_with_ghots.png'>"),
            Page("https://www.ghots.com/mapsghots","mapsghots","<a href= 'https://www.ghotsll33.com' target='_blank'> GHOTSLL33 </a>","<p> this is ghotsll33 </p>","<h3> ghotsll33 </h3>","<p> php </p>","<p> my web site ghotsll33 </p>","<audio> ghotsll33.mp3 </audio>","<video> ghotsll33.mp4 </video>","<img src= 'ghotsll33.png'>"),
        ]
    ]
    
    # lista de sito web donde se le ingresa la lista de la paguina web correspondiente ejemplo page[0]
    website = [
        Website("https://www.angel.com",page[0],"angel","my option","wechat","catalogue of work","yourmaps"),
        Website("https://www.spiders.com",page[1],"the spiders","spiders of world","spider-chat","catalogue of spiders","spiders-maps"),
        Website("https://www.ghots.com",page[2],"ghots","ghots","ghots-chat","catalogue of ghots","ghots-maps")
    ]
    
    # instanciamos la clase Seeker y mandandole los parametros website, page, el dominio y el nombre de la paguina
    seeker = Seeker(website, page, "https://www.angel.com","init")
    # imprimimos el resultado esperado
    webprint = seeker.seekerweb()
    print(webprint)

if __name__ == "__main__":
    main()
    