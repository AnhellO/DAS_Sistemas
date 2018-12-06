#Descripcion y especificaciones del proyecto

  * Esta es una app de una taqueria que tiene su pag web, obtuvimos la info de
  los tacos scrapeando desde http://taco-randomizer.herokuapp.com/, usando
  BeautifulSoup y la info de los clientes desde randomuser.me

  * Mi proyecto cuenta con un "programita" xD (.py) que contiene las clases
  abstractas de taco, cliente y de la basesita con sus respectivos metodos
  (abstractas.py), otro .py que se encarga de traer los datos del cliente desde
  la api, guardarlos en una variable tipo cliente y regresarla(clientes_api), al
  igual que el .py de los taquitos que los scrapea desde un API html y los
  almacena(tako_scrap); tenemos el archivo que se encarga de crear la base de
  datos(takos_db_init), y el que incluye todos los metodos con la que funciona y 
  el setup.py llena la base con la informacion que trajimos de los clientes y
  tacos e implementa su metodo abstracto(database), y por ultimo queda el Main,
  que es el que se ecnarga de usar la base de datos, aunque en nuestro
  caso simula el "menu" del servicio de los tacos, ya que nos muestra un menusito
  que seria como acercarte a pedir los tacos (hacer el insert de la orden), nos
  permite preguntar sobre la info de nuestra orden (select) y tambien nos deja
  cancelar  la orden (delete).
  Y asi es como funciona mi aplicacionsita :D esta bien chida

  ###Referencias:


![](C:\Users\Vela\Documents\Diseño\DAS_Sistemas\Ago-Dic-2018\Ernesto Vela\Proyecto\Diagrama_ER.jpg)
![](C:\Users\Vela\Documents\Diseño\DAS_Sistemas\Ago-Dic-2018\Ernesto Vela\Proyecto\Diagrama_de_clases.jpg)
