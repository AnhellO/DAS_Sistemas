class Page(object):
    def __init__(self, **args):
        self.url = args.get('url')
        self.folder = args.get('folder')
        self.link = args.get('link')
        self.titulo = args.get('titulo')
        self.desc =args.get('desc')
        self.formato = args.get('formato')
                
    #GET & SET 
    def set_url(self, url):
        self.url=url
    def get_url(self):
        return self.url
    def set_folder(self, folder):
        self.folder = folder
    def get_folder(self):
        return self.folder
    def set_link(self, link):
        self.link = link
    def get_link(self):
        return self.link
    def set_titulo(self, titulo):
        self.titulo = titulo
    def get_titulo(self):
        return self.titulo
    def set_desc(self, desc):
        self.desc = desc
    def get_desc(self):
        return self.desc
    def set_formato(self, formato):
        self.formato = formato
    def get_formato(self):
        return self.formato
        
     #STRING
    def __str__(self):
        return f'URL: {self.url}\nFolder: {self.folder}\nLink: {self.link}\nTitulo: {self.titulo}\nDescripción: {self.desc}\nFormato: {self.formato}'
    