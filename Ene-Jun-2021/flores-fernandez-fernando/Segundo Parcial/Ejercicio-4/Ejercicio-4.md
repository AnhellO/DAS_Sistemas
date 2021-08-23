Ejercicio-4
==================

Me decidi por un diagrama por capas por que sentí que era la manera mas sencilla de poder explicar el funcionamento
dividiendolo en partes que pudieran tener un objetivo en especifico.



Presentation layer
---------------
aqui tenemos las carpetas de hello o assets las cuales manejan todo lo que tiene que ver con la vista del programa 
- hello tenemos los templates para crear las vistas y tambien las extensiones que se usan en la pagina 
- page tenemos unos scripts para que trabajen en las vistas y templates
- assets tenemos css y las imagenes del sitio 

Bussiness Layer
--------------
aqui se maneja el control de la aplicacion 
- bin aqui tenemos scripts para las imagenes que se guarden en el lugar correcto, tenemos tambien la instalacion de los requerimientos de las librerias 
- en el archivo app de la carpeta hello, podemos ver el flijo de la aplicacion ya mas al fondo, donde manda a llamar lo que es
de la base de datos y el frontend aqui se crea la app e introduce las extenciones y templates del frontend.

- en lib se tienen las pruebas para una iniciar sesion y el cliente 
- en test se tienen los testeos para las vistas de las paginas 

Access Data Layer
----------------
- config se tiene lo que es la comunicacion de la app con la base de datos inicio de sesiones y parametros.

Data Layer 
-------------
- aqui tenemos los datos de la base de datos para el inicio se sesion. 

