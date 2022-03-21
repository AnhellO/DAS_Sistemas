from page import Page

'''
Se implementa el patrón decorador, decora el contenido de las paginas las cuales
su formato sea HTML.
'''

# Funcion decoradora
def decorador(funcion):
    def agregarCSS(pagina): # Función que agrega CSS al contenido
        formato = funcion(pagina)   # Agrega valor a la variable formato
        if formato == 'HTML':   # Verifica el formato
            print("La página si es de formato HTML")
            contenidoPagina = pagina.contenido            
            index = contenidoPagina.index('>')
            contenidoNvo = ' style="color:blue;text-align:center;"'     # Contenido a agregar
            contenido = contenidoPagina[:index] + contenidoNvo +contenidoPagina[index] + contenidoPagina[index+1:]      # Contenido completo
            pagina.contenido = contenido    # Se establece el contenido en la página
            return
        print("La página NO es de formato HTML")
        return
    return agregarCSS

@decorador  
def paginaDecorar(pagina : Page):   # Función que llama el decorador
    return pagina.formato   # Retorna el formato

def main():
    page = Page()   # Objeto de tipo Page, formato HTML
    page.setUrl('www.themeforest.net')    
    page.setHipervinculos('<a href="https://themeforest.net/category/wordpress?sort=date">Hipervinculo</a>')
    page.setTitulo('<h1>Forest</h1>')
    page.setContenido('<p>Contenido de la página.</p')
    page.setFormato('HTML')


    print(f"Contenido anter de decorar: {page.contenido}")
    paginaDecorar(page)
    print(f"Contenido después de llamar a la función paginaDecorar: {page.contenido}")
    
    '''
    Contenido anter de decorar: <p>Contenido de la página.</p
    La página si es de formato HTML
    Contenido después de llamar a la función paginaDecorar: <p style="color:blue;text-align:center;">Contenido de la página.</p
    '''

    
    print()
    page1 = Page()  # Objeto de tipo Page, formato XAMP
    page1.setUrl('https://www.youtube.com/')    
    page1.setFolder('proyecto') 
    page1.setTitulo('<h1>YouTube</h1>')
    page1.setContenido('<p>Contenido de la página.</p')
    page1.setFormato('XAMP')

    print(f"Contenido anter de decorar: {page1.contenido}")
    paginaDecorar(page1)
    print(f"Contenido después de llamar a la función paginaDecorar: {page1.contenido}")

    '''
    Contenido anter de decorar: <p>Contenido de la página.</p
    La página NO es de formato HTML
    Contenido después de llamar a la función paginaDecorar: <p>Contenido de la página.</p
    '''

if __name__ == '__main__':
    main()