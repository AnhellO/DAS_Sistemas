from abc import ABC, abstractmethod
from ejercicio_1 import *

# interface puerta 
class Door(ABC):
    @abstractmethod
    def request(self) -> None:
        pass

# clase usuario que hereda de la clase Door el método request
class User(Door):
    # el constructor resive como parametro el sitio web con su pagina web
    def __init__(self,website:str) -> None:
        self.website = website
    # el metodo request nos imprime la información del usuario al iniciar sessión en el sitio web
    def request(self) -> None:
        return f"USER: angel coronado\nAGE: 25 years old \nPROFESSION: student\nHOBBIES: program\n======================\n{self.website}"

# clasee Proxy
class Proxy(Door):
    # el constructor resive 3 parametros uno de tipo User de la Clase User
    # los otros dos de tipo strting usuario y contraseña
    def __init__(self, user: User,username:str,password:str) -> None:
        self._user = user
        self.username = username
        self.password = password

    def request(self) -> None:
        # el método requeste evaluar si lo que recibe del método autenticar el falso o verdadero
        # y retorna la información del usuario y la pagina web o falso si en este caso la contraseña o el usuario no son autenticos
        if self.authentication():
            self.access()
            return self._user.request()
        else:
            return False
    #nos permite autenticar validar el usuario y contraseña
    def authentication(self) -> bool:
        if self.username == "angel@gmail.com" and self.password == "spider123":
            return True
        else:
            print("USER OR PASSWORD INCORRECT")
            return False
    #nos imprime un mensaje de acceso correcto
    def access(self) -> None:
        print("=====================")
        print("|  Successful login |")
        print("=====================")

# clase cliente 
class Client:
    # el constructor recibe como parametro la petición del usuario
    def __init__(self,user:User) -> None:
        self.user = user
    # nos retorna la información de la petición del usuario 
    def client_code(self) -> None:
        return self.user.request()

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
    
    # instanciamos la clase User
    user = User(webprint)
    # se pasan lo valores a la clase Proxy de la clase User y las credenciales 
    proxy = Proxy(user,"angel@gmail.com","spider123")
    # pasamos como parametro a la Clase Cliente lo que retorne la claseProxy
    login = Client(proxy)
    # imprimir resultado
    print(login.client_code())

if __name__ == "__main__":
    main()