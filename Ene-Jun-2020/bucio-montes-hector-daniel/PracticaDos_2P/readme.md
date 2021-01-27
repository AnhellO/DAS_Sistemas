INFORMACIÓN E INSTRUCCIONES SOBRE APLICACIÓN DE AGE OF EMPIRES II

La siguiente aplicación almacena información de la API 
de Age of Empires II en una base de datos.

Se utilizó sqlite3 para la creación de dicha bd y también
se hizo uso de la ORM Peewee para poder agregar los datos 
recolectados de la API.


* Link de API de Age of Empires II:

https://age-of-empires-2-api.herokuapp.com/


Bueno para poder hacer uso de ésta aplicación se tiene que correr el
archivo api_n_databs.py para que cree la base de datos AoEII.db,
luego corre el archivo app.py y da click en el siguiente link
para que la pueda abrir en tu navegador:

    * http://0.0.0.0:5000/ 
 
***
***

* Ésta aplicación le dara información sobre los cuatro campos que
tiene la API de AoE que son:
    * Información acerca de Civilizaciones
    * Información acerca de Unidades
    * Información acerca de Estructuras
    * Información acerca de Tecnologías
    
Importante: 
    
      * La aplicación sólo le dará algunos campos de cada cosa
        ya que no se incluyeron todos.
        
        Pero igual podrá ver que si se incluyen: 
         * 18 Civilizaciones,
         * 104 Unidades 
         * 59 Estructuras
         * 140 Tecnologías