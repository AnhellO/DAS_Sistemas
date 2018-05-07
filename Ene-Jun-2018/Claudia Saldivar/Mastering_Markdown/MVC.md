###Modelo vista controlador (MVC)

**Modelo Vista Controlador** (MVC) es un estilo de arquitectura de software que separa los datos de una aplicación, la interfaz de usuario, y la lógica de control en tres componentes distintos.

Se trata de un modelo muy maduro y que ha demostrado su validez a lo largo de los años en todo tipo de aplicaciones, y sobre multitud de lenguajes y plataformas de desarrollo.
-El Modelo que contiene una representación de los datos que maneja el sistema, su lógica de negocio, y sus mecanismos de persistencia.
-La Vista, o interfaz de usuario, que compone la información que se envía al cliente y los mecanismos interacción con éste.
-El Controlador, que actúa como intermediario entre el Modelo y la Vista, gestionando el flujo de información entre ellos y las transformaciones para adaptar los datos a las necesidades de cada uno.

##El modelo es el responsable de:

-Acceder a la capa de almacenamiento de datos. Lo ideal es que el modelo sea independiente del sistema de almacenamiento.
-Define las reglas de negocio (la funcionalidad del sistema). Un ejemplo de regla puede ser: "Si la mercancía pedida no está en el almacén, consultar el tiempo de entrega estándar del proveedor".
-Lleva un registro de las vistas y controladores del sistema.
-Si estamos ante un modelo activo, notificará a las vistas los cambios que en los datos pueda producir un agente externo (por ejemplo, un fichero por lotes  que actualiza los datos, un temporizador que desencadena una inserción, etc.).

##El controlador es responsable de:

-Recibe los eventos de entrada (un clic, un cambio en un campo de texto, etc.).
-Contiene reglas de gestión de eventos, del tipo "SI Evento Z, entonces Acción W". Estas acciones pueden suponer peticiones al modelo o a las vistas. Una de estas peticiones a las vistas puede ser una llamada al método "Actualizar()". Una petición al modelo puede ser "Obtener_tiempo_de_entrega ( nueva_orden_de_venta )".

##Las vistas son responsables de:

-Recibir datos del modelo y los muestra al usuario.
-Tienen un registro de su controlador asociado (normalmente porque además lo instancia).
-Pueden dar el servicio de "Actualización()", para que sea invocado por el controlador o por el modelo (cuando es un modelo activo que informa de los cambios en los datos producidos por otros agentes).

##Ventajas

-Podrás dividir la lógica de negocio del diseño, haciendo tu proyecto más escalable.
-Te facilitará el uso de URL amigables, importantes para el SEO (Posicionamiento web), la mayoría de frameworks MVC lo controlan.
-Muchos frameworks MVC ya incluyen librerías de Javascript como Jquery, lo que te facilitará validar formularios (Ej. Jquery.Validate) en el cliente y en el servidor.
-Puedes utilizar abstracción de datos, como lo hace Ruby on Rails o con frameworks como Hibernate para Java o NHibernate para ASP .NET MVC, facilitando la realización de consultas a la base de datos.
-La mayoría de frameworks controlan el uso de la memoria Caché, hoy en día muy importante para el posicionamiento web, ya que buscadores como google dan prioridad a las webs que tengan menor tiempo de descarga.
-En el caso de proyectos donde hay varios desarrolladores, el seguir métodos comunes de programación, hace que el código sea más entendible entre estos, pudiendo uno continuar el trabajo de otro. En estos casos es conveniente utilizar herramientas de control de versiones como Subversion.
-Los frameworks están creados para facilitar el trabajo de los desarrolladores, encontrarás clases para controlar fechas, URL's, Webservices, etc. lo que tiene una gran ventaja en cuanto a productividad. Inicialmente como es lógico habrá una curva de aprendizaje, pero luego tendrás muchos beneficios.
-Poco a poco el desarrollo web se orienta a lo que se denomina "Agile Web Development" (Desarrollo ágil de aplicaciones web), con frameworks como Ruby on Rails que ayudan a crear proyectos de calidad y en corto tiempo. Existen varios frameworks en PHP e incluso ASP .NET que en su nueva vesión ya contempla el MVC con Visual C#.
-Utilizar herramientas con tecnología escalable hace más atractivo tu proyecto en caso de buscar inversión externa, muchas veces para hacer crecer un proyecto, es necesario buscar socios o Bussines Angels que te ayuden a impulsarlo.
-Un Framework MVC te ayuda a controlar los recursos del servidor, evitando Bugs que puedan repercutir en el rendimiento, por ejemplo, muchas veces olvidamos cerrar conexiones a la base de datos, sobrecargando el servidor.

##Desventajas

-Para desarrollar una aplicación bajo el patrón de diseño MVC es necesario una mayor dedicación en los tiempos iniciales del desarrollo. Normalmente el patrón exige al programador desarrollar un mayor número de clases que, en otros entornos de desarrollo, no son necesarias. Sin embargo, esta desventaja es muy relativa ya que posteriormente, en la etapa de mantenimiento de la aplicación, una aplicación MVC es mucho más mantenible, extensible y modificable que una aplicación que no lo implementa.
-MVC requiere la existencia de una arquitectura inicial sobre la que se deben construir clases e interfaces para modificar y comunicar los módulos de una aplicación. Esta arquitectura inicial debe incluir, por lo menos, un mecanismo de eventos para poder proporcionar las notificaciones que genera el modelo de aplicación; una clase Modelo, otra clase Vista y una clase Controlador genéricas que realicen todas las tareas de comunicación, notificación y actualización que serán luego transparentes para el desarrollo de la aplicación.
MVC es un patrón de diseño orientado a objetos por lo que su implementación es sumamente costosa y difícil en lenguajes que no siguen este paradigma.

##Diagrama

Hiperlink:[mvc][]
[MVC]:http://www.juntadeandalucia.es/servicios/madeja/contenido/recurso/122
