# Examen Damian Rafael Hernandez Saucedo
class Page:
    
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
    
   
    def __str__(self) -> str:
        return f"URL: {self.url}\nNAME: {self.name}\nHYPERLINKS: {self.hipervinculos}\nTEXT: {self.texto}\nTITLE: {self.titulo}\nFORMAT: {self.formato}\nMETADESCRIPTION: {self.metadescripcion}\nSOUND: {self.sonido}\nVIDEO: {self.video}\nIMAGE: {self.imagenes}"


class Website:
    
    def __init__(self,dominio:str, page:Page, administrador:str, menu:str, chat:str, catalogo:str, mapa:str) -> None:
        self.dominio = dominio
        self.page = page
        self.administrador = administrador
        self.menu = menu
        self.chat = chat
        self.catalogo = catalogo
        self.mapa = mapa
        self.chosenpage = ""
        
    
    def __str__(self) -> str:
        return f"My Web Site is\nDOMAIN: {self.dominio}\n== PAGE WEB ==\nPAGE: {self.chosenpage}\n============\nADMIN: {self.administrador}\nMENU: {self.menu}\nCHAT: {self.chat}\nCATALOGUE: {self.catalogo}\nMAPA: {self.mapa}"



class Seeker:
    
    def __init__(self, websitelist:Website, pagelist:Page, seekerwebsite:str, seekerpage:str) -> None:
        self.websitelist = websitelist
        self.pagelist = pagelist
        self.seekerwebsite = seekerwebsite
        self.seekerpage = seekerpage
    
    
    def seekerweb(self):
        countweb = 0 
        countpage = 0 
        
        for web in self.websitelist:
            countweb += 1
            if web.dominio == self.seekerwebsite:
                
                for i in range (len(self.pagelist)):
                    countpage += 1
                    pages = self.pagelist[i]
                    if web.page[i].name == self.seekerpage:
                        
                        web.chosenpage = web.page[i]
                        return web
                    
                    elif web.page[i].name != self.seekerpage and countpage == len(self.pagelist):
                        return "PAGE NOT FOUND"
            
            elif web.dominio != self.seekerwebsite and countweb == len(self.websitelist):
                return "SITE NOT FOUND"

       
def main():
    
    page = [
        [
            Page("https://www.damian.com/init","init","https://www.youtube.com","my first page web","world","html","my web site","en el rio-arcadia libre.mp3","hello.mp4","my.png"),
            Page("https://www.damian.com/logi","logi","https://www.facebook.com","this is facebook","hello","html","my web site","hello.mp3","hello.mp4","hoooo.png"),
            Page("https://www.damian.com/menu","menu","https://www.yahoo.com","this is yahoo","poom","html","my web site","nana pancha.mp3","my friends.mp4","hellsing.png"),
            Page("https://www.damian.com/catalog","catalogo","https://www.twitter.com","this is twitter","arcadia libre","html","my web site","menos yo-sekta core.mp3","hello.mp4","onepuchman.png"),
            Page("https://www.damian.com/maps","maps","https://www.python.com","this is python","world","php","my web site","experts.mp3","parkour.mp4","my.png"),
        ],
        [
            Page("https://www.anime.com/initanime","initanime","https://www.youtube.com","page web","world","html","my web site","sound.mp3","my animeworld.mp4","Lycosidae.png"),
            Page("https://www.anime.com/logianime","logianime","https://www.facebook.com","this is facebook","Json","javaScript","web site","mysound.mp3","documents.mp4","salticidae.png"),
            Page("https://www.anime.com/menuanime","menuanime","https://www.yahoo.com","this is yahoo","poom","php","anime menu","description.mp3","expert.mp4","salticidaess66.png"),
            Page("https://www.anime.com/catalogoanime","catalogoanime","https://www.twitter.com","this is twitter","catalogue","xml","cantalogue of anime","the world.mp3","hello.mp4","one.png"),
            Page("https://www.anime.com/mapsanime","mapsanime","https://www.animemuch.com","this is animemuch","animemuch it is the best page of anime","php","description","helloworld.mp3","animemuch.mp4","animemuch33.png"),
        ],
        [
            Page("https://www.netflix.com/initnetflix","initnetflix","https://www.youtube.com","this is video of netflix","netflix world","php","page of netflix","soundnetflix.mp3","evidents.mp4","netflix_in_my_house.png"),
            Page("https://www.netflix.com/loginetflix","loginetflix","https://www.facebook.com","this is we facebook page","netflixland","php","page of images","sound2.mp3","netflix.mp4","graveyard.png"),
            Page("https://www.netflix.com/menunetflix","menunetflix","https://www.yahoo.com","this is yahoo","description my web page","php","my web site of netflix","booh.mp3","netflix_in_graveyard.mp4","evil.png"),
            Page("https://www.netflix.com/catalogonetflix","catalogonetflix","https://www.twitter.com","this is twitter","animals","php","netflix and animal","animals.mp3","dogs.mp4","dog_with_netflix.png"),
            Page("https://www.netflix.com/mapsnetflix","mapsnetflix","https://www.netflixll33.com","this is netflixll33","netflixll33","php","my web site netflixll33","netflixll33.mp3","netflixll33.mp4","netflixll33.png"),
        ]
    ]
    
    
    website = [
        Website("https://www.damian.com",page[0],"damian","my option","wechat","catalogue of work","yourmaps"),
        Website("https://www.anime.com",page[1],"the anime","anime of world","anime-chat","catalogue of anime","anime-maps"),
        Website("https://www.netflix.com",page[2],"netflix","netflix","netflix-chat","catalogue of netflix","netflix-maps")
    ]
    
    
    seeker = Seeker(website, page, "https://www.netflix.com","loginetflix")
    
    webprint = seeker.seekerweb()
    print(webprint)
    print(type(page[0]))

if __name__ == "__main__":
    main()
    