from page import Page
from website import Website


def buscador(website, nombre):
    if nombre in website.paginaweb.keys():
        page = website.paginaweb[nombre]
    return page


if __name__ == "__main__":
    page = Page(
        "titulo de pagina",
        "texto de la pagina",
        "cuerpo, descripcion de la pagina",
        "URL de pagina",
        "imagenes que muestra la pagina",
        "carpetas de la pagina",
        "links para tener acceso a la pagina",
        "cabezera de pagina",
        "scripts de la pagina",
        "css de pagina")
       
    print(page)

    website = Website(
        "URL de website",
        "dominio website",
        "subdomino website",
        "servidorweb website",
         {"pagina_principal":page},
        "motordebusqueada website",
        "sitioweb website")
    print(website)

    pagina_principal = buscador(website, "pagina_principal")
    print(pagina_principal)
