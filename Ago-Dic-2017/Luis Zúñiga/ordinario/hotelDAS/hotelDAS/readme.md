# Aplicación Hotel DAS con django (MVC)

## Estructura de la aplicación


hotelDAS

	manage.py
	
	app	
		migrations		
		static		
		templates
			
			app
				about.html
				contact.html
				index.html
				layout.html
				login.html
				loginpartial.html
				muestrareservacion.html
				registracliente.html
				reservacion.html
		
		admin.py
		forms.py
		models.py
		tests.py
		views.py		
	
	hotelDAS
		settings.py
		urls.py
		wsgi.py
		
	

Como podemos observar en la estructura anterior, con [django](https://www.djangoproject.com/) tenemos una carpeta principal para el proyecto, misma que contiene el archivo manage.py, que es desde donde realizan diversas actividades de administración del proyecto, como el de ejecutar el servidor con python manage.py runserver.

En esa carpeta principal se incluyen dos carpetas, hotelDAS, que es la que contiene la configuración principal del proyecto, y app, que es la aplicación que contiene propiamente el sitio web.

Dentro de la carpeta app (no confundir con la otra del mismo nombre, que es la que contiene los html) encontramos los archivos que, de acuerdo a su estructura, nos advierte la utilización del patrón de arquitectura de software Modelo Vista Controlador.

### Modelos (Models.py)

Aquí encontramos las definiciones de las clases que vamos a utilizar y, por tanto, también los modelos de persistencia de datos en la BD.

### Vistas (forms.py y HTML)

La carpeta app que contiene los archivos HTML es la que participa como la Vista dentro de este patrón de arquitectura.
Por otra parte, el archivo forms.py define formularios para mostrar al usuario final.

### Controlador (views.py)

Aunque el archivo se llama views, éste define la información que es mostrada al usuario y funge como pleno intermediario entre el sistema (en este caso la aplicación del hotel) y el usuario que realizará la reservación. No olvidemos que el autor mismo del patrón MVC define una vista como un "filtro de presentación" y un controlador como un "filtro de información"


