# Proyecto Ordenario
  ##Descripcion
  * Esta aplicacion simula un puesto de tacos que tiene su propia pagina web online
  ##Especificaciones de funcionamiento
  * Esta App cuaenta con 9 files para su corecta implementacion las cuales 3 de
    ella son clases abstractas que se usan para manejor los objetos Taquito y
    usuario asi como los metodos de una base de datos los cuales son AbstracUsers
    la cual contiene un constructor y una clase para buscar un usuario, AbstracTaco
    tambien con un constructor y metodo para buscar un taco, AbstracDB contiene todos
    los metodos para utilisar la base de datos, a su vez utilize 3 files para implementar
    los metodos abstractos de estas 3 files para traer los datos de cada API y
    las guardan en una vairable tipo Taquitoo usuario respectivamente las cuales
    se llaman Scrapi_taco y API_User claro Scrapi_taco utiliza scraping para poder
    traerse los datos de la la API html, la API_User se trae los datos de un usuario
    random de la API de clientes proporsionada para este proyecto, ambos metodos
    guardan los dstos traidos de las API's en variables tipo Taquito y Useres respectivamente,
    el file Data_Base contiene los metodos usandos para el manejo de la base de datos,
    y para crear la base de datos utilizo el file db_init .
    Por ultimo el file setup_Taqueria utiliza los 3 files anteriores para meter
    los 50 tacos a la base de datos asi como 25 clientes de las API's respectivamente,
    el file principal es Main donde se administran las ordenes con los datos ya
    insertados en la base de dastos.
    ##Referrancias
  * ![](C:\Users\user\DAS_Sistemas\Ago-Dic-2018\ArmandoGarcia\Ordinario\diagrama_de_clases.png)
  * ![](C:\Users\user\DAS_Sistemas\Ago-Dic-2018\ArmandoGarcia\Ordinario\diagrama_entidad_relacion.png)
  * <http://www.sqlitetutorial.net/sqlite-create-table/>
  * <https://code.tutsplus.com/es/tutorials/scraping-webpages-in-python-with-beautiful-soup-the-basics--cms-28211>
  * <https://jarroba.com/scraping-python-beautifulsoup-ejemplos/>
