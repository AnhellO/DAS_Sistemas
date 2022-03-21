
class Builder():
    def reset(self):
        pass
    
    def set_url(self, url):
        pass
    
    def set_name(self, name):
        pass
    
    def set_hyperlinks(self, hyperlinks):
        pass
    
    def set_text(self, text):
        pass
    
    def set_tittle(self, tittle):
        pass
    
    def set_format(self, format):
        pass
    
    def set_metadescription(self, metadescription):
        pass
    
    def set_sound(self, sound):
        pass
    
    def set_video(self,video):
        pass
    
    def set_image(self,image):
        pass
    
    def set_domain(self, domain):
        pass
    
    def set_page(self, page):
        pass
    
    def set_administrator(self, administrator):
        pass
    
    def set_menu(self, menu):
        pass
    
    def set_chat(self, chat):
        pass
    
    def set_catalogue(self, catalogue):
        pass
    
    def set_map(self, map):
        pass
    
    
    def get_result(self):
        pass




class PageBuilder(Builder):
    def __init__(self) -> None:
        self.pages = Page()

    def reset(self):
        self.pages = Page()
    
    def set_url(self, url):
        self.pages.set_url(url)
    
    def set_name(self, name):
        self.pages.set_name(name)
    
    def set_hyperlinks(self, hyperlinks):
        self.pages.set_hyperlinks(hyperlinks)
    
    def set_text(self, text):
        self.pages.set_text(text)
    
    def set_tittle(self, tittle):
        self.pages.set_tittle(tittle)
    
    def set_format(self, format):
        self.pages.set_format(format)
    
    def set_metadescription(self, metadescription):
        self.pages.set_metadescription(metadescription)
    
    def set_sound(self, sound):
        self.pages.set_sound(sound)
    
    def set_video(self,video):
        self.pages.set_video(video)
    
    def set_image(self,image):
        self.pages.set_image(image)
    
    def get_result(self):
        return self.pages


class WebSiteBuilder(Builder):
    def __init__(self) -> None:
        self.website = Website()

    def reset(self):
        self.website = Website()

    
    def set_domain(self, domain):
        self.website.set_domain(domain)
    
    def set_page(self, page):
        self.website.set_page(page)
    
    def set_administrator(self, administrator):
        self.website.set_administrator(administrator)
    
    def set_menu(self, menu):
        self.website.set_menu(menu)
    
    def set_chat(self, chat):
        self.website.set_chat(chat)
    
    def set_catalogue(self, catalogue):
        self.website.set_catalogue(catalogue)
    
    def set_map(self, map):
        self.website.set_map(map)

    def get_result(self):
        return self.website
    



class Page:
    
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
        
    
    def set_url(self, url):
        self.url = url

    
    def set_name(self, name):
        self.name = name

    
    def set_hyperlinks(self, hyperlinks):
        self.hyperlinks = hyperlinks

    
    def set_text(self, text):
        self.text = text

    
    def set_tittle(self, tittle):
        self.tittle = tittle

    
    def set_format(self, format):
        self.format = format

    
    def set_metadescription(self, metadescription):
        self.metadescription = metadescription

    
    def set_sound(self, sound):
        self.sound = sound

    
    def set_video(self,video):
        self.video = video

    
    def set_image(self,image):
        self.image = image
    
    def __str__(self) -> str:
        return f"URL: {self.url}\nNAME: {self.name}\nHYPERLINKS: {self.hyperlinks}\nTEXT: {self.text}\nTITLE: {self.tittle}\nFORMAT: {self.format}\nMETADESCRIPTION: {self.metadescription}\nSOUND: {self.sound}\nVIDEO: {self.video}\nIMAGE: {self.image}"

        
class Website:
    def __init__(self,domain=None, page=None, administrator=None, menu=None, chat=None, catalogue=None, map=None) -> None:
        self.domain = domain
        self.page = page
        self.administrator = administrator
        self.menu = menu
        self.chat = chat
        self.catalogue = catalogue
        self.map = map
        self.chosenpage = None
    
    
    def set_domain(self, domain):
        self.domain = domain
    
    def set_page(self, page):
        self.page = page
    
    def set_administrator(self, administrator):
        self.administrator = administrator
    
    def set_menu(self, menu):
        self.menu = menu
    
    def set_chat(self, chat):
        self.chat = chat
    
    def set_catalogue(self, catalogue):
        self.catalogue = catalogue
    
    def set_map(self, map):
        self.map = map
    
    
    def __str__(self) -> str:
        return f"My Web Site is\nDOMAIN: {self.domain}\n=============== PAGE WEB ===============\nPAGE: { self.chosenpage}\n========================================\nADMIN: {self.administrator}\nMENU: {self.menu}\nCHAT: {self.chat}\nCATALOGUE: {self.catalogue}\nMAPA: {self.map}"





class Director:
    def __init__(self, builder: Builder) -> None:
        self.builder = builder
    
    def changebuilder(self, builder: Builder):
        self.builder = builder
    
   
    def makePage(self,url:str,name:str,hyperlinks:str,text:str,title:str,format:str,metadescription:str,sound:str,video:str,image:str) -> str:
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
        return self.builder.get_result()

    
    def makeWeb(self,domain:str, page:Page, administrator:str, menu:str, chat:str, catalogue:str, map:str) -> str:
        self.builder.set_domain(domain)
        self.builder.set_page(page)
        self.builder.set_administrator(administrator)
        self.builder.set_menu(menu)
        self.builder.set_chat(chat)
        self.builder.set_catalogue(catalogue)
        self.builder.set_map(map)
        return self.builder.get_result()




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
            if web.domain == self.seekerwebsite:
                
                for pages in self.pagelist:
            
                    for i in range(len(pages)):
                        countpage += 1
                        if web.page[i].name == self.seekerpage:
                            
                            web.chosenpage = web.page[i]
                            return web
                        
                        elif web.page[i].name != self.seekerpage and countpage == len(pages):
                            return "PAGE NOT FOUND"
                    
                    
            
            elif web.domain != self.seekerwebsite and countweb == len(self.websitelist):
                return "SITE NOT FOUND"
   


def main():
    
    directorpage = []
    for i in range(15):
        pagebuilder = PageBuilder()
        directorpage.append(Director(pagebuilder))
    page = [
         [
            directorpage[0].makePage("https://www.damian.com/init","init","https://www.youtube.com","my first page web","world","html","my web site","en el rio-arcadia libre.mp3","hello.mp4","my.png"),
            directorpage[1].makePage("https://www.damian.com/logi","logi","https://www.facebook.com","this is facebook","hello","html","my web site","hello.mp3","hello.mp4","hoooo.png"),
            directorpage[2].makePage("https://www.damian.com/menu","menu","https://www.yahoo.com","this is yahoo","poom","html","my web site","nana pancha.mp3","my friends.mp4","hellsing.png"),
            directorpage[3].makePage("https://www.damian.com/catalog","catalogo","https://www.twitter.com","this is twitter","arcadia libre","html","my web site","menos yo-sekta core.mp3","hello.mp4","onepuchman.png"),
            directorpage[4].makePage("https://www.damian.com/maps","maps","https://www.python.com","this is python","world","php","my web site","experts.mp3","parkour.mp4","my.png"),
        ],
        [
            directorpage[5].makePage("https://www.anime.com/initanime","initanime","https://www.youtube.com","page web","world","html","my web site","sound.mp3","my animeworld.mp4","Lycosidae.png"),
            directorpage[6].makePage("https://www.anime.com/logianime","logianime","https://www.facebook.com","this is facebook","Json","javaScript","web site","mysound.mp3","documents.mp4","salticidae.png"),
            directorpage[7].makePage("https://www.anime.com/menuanime","menuanime","https://www.yahoo.com","this is yahoo","poom","php","anime menu","description.mp3","expert.mp4","salticidaess66.png"),
            directorpage[8].makePage("https://www.anime.com/catalogoanime","catalogoanime","https://www.twitter.com","this is twitter","catalogue","xml","cantalogue of anime","the world.mp3","hello.mp4","one.png"),
            directorpage[9].makePage("https://www.anime.com/mapsanime","mapsanime","https://www.animemuch.com","this is animemuch","animemuch it is the best page of anime","php","description","helloworld.mp3","animemuch.mp4","animemuch33.png"),
        ],
        [
            directorpage[10].makePage("https://www.netflix.com/initnetflix","initnetflix","https://www.youtube.com","this is video of netflix","netflix world","php","page of netflix","soundnetflix.mp3","evidents.mp4","netflix_in_my_house.png"),
            directorpage[11].makePage("https://www.netflix.com/loginetflix","loginetflix","https://www.facebook.com","this is we facebook page","netflixland","php","page of images","sound2.mp3","netflix.mp4","graveyard.png"),
            directorpage[12].makePage("https://www.netflix.com/menunetflix","menunetflix","https://www.yahoo.com","this is yahoo","description my web page","php","my web site of netflix","booh.mp3","netflix_in_graveyard.mp4","evil.png"),
            directorpage[13].makePage("https://www.netflix.com/catalogonetflix","catalogonetflix","https://www.twitter.com","this is twitter","animals","php","netflix and animal","animals.mp3","dogs.mp4","dog_with_netflix.png"),
            directorpage[14].makePage("https://www.netflix.com/mapsnetflix","mapsnetflix","https://www.netflixll33.com","this is netflixll33","netflixll33","php","my web site netflixll33","netflixll33.mp3","netflixll33.mp4","netflixll33.png"),
        ]
    ]
    
    directorweb = []
    for i in range(3):
        websitebuilder = WebSiteBuilder()
        directorweb.append(Director(websitebuilder))
        
    website = [
        directorweb[0].makeWeb("https://www.damian.com",page[0],"damian","my option","wechat","catalogue of work","yourmaps"),
        directorweb[1].makeWeb("https://www.anime.com",page[1],"the anime","anime of world","anime-chat","catalogue of anime","anime-maps"),
        directorweb[2].makeWeb("https://www.netflix.com",page[2],"netflix","netflix","netflix-chat","catalogue of netflix","netflix-maps")
    ]
    
    
    seeker = Seeker(website, page, "https://www.netflix.com","mapsnetflix")
    # el resultado esperado
    webprint = seeker.seekerweb()
    print(webprint)
    
    
if __name__ == "__main__":
    main()