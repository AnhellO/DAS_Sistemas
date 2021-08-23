class PaginaWeb():
    def __init__(self,url,ruta,form,cont,title,slug,mtags:list):
        self.url=url
        self.ruta=ruta
        self.formato=form
        self.contenido=cont
        self.titulo=title
        self.slug=slug
        self.metatags=mtags

    def __str__(self):
        return f'URL: {self.url}\nRuta: {self.ruta}\nFormato: {self.formato}\nContenido: {self.contenido}\nTitulo: {self.titulo}\nSlug: {self.slug}\nMeta-Tags: {self.metatags}'

def decorador_buscador():
    def buscador(SitioWeb):
        class Searcher(SitioWeb):
            def buscar(self):
                if self.webpage in self.paginas:
                    return "Pagina existe"
                else:
                    return "Error, pagina no existe"
        return Searcher
    return buscador

@decorador_buscador()
class SitioWeb():
    def __init__(self,dom,cat,pag:list,webpage:PaginaWeb):
        self.dominio=dom
        self.categoria=cat
        self.paginas=pag
        self.webpage=webpage


    def __str__(self):
        return f"Dominio: {self.dominio}\nCategoria: {self.categoria}\nPaginas: {len(self.paginas)}\n {''.join([str(i) for i in self.paginas])}"



if __name__=="__main__":
    pagina=PaginaWeb("www.youtube.com","/rob","html","videos","video tutoriales","video-tutoriales",["matematicas","fisica"])
    paginas_list=[]
    paginas_list.append(pagina)
    pagina_busqueda=PaginaWeb("www.youtube.com","/rob","html","videos","video tutoriales","video-tutoriales",["matematicas","fisica"])

    website=SitioWeb(".com","ciencias",paginas_list,pagina_busqueda)
    print(website)

