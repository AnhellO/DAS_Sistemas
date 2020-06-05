### Predicting space weather with Docker


En esta ocasión el desarrollador de software Chris Lauer, se encargó de esta sesión donde nos cuenta
principalmente que su lugar de trabajo que es el Centro de Predicción de Clima Espacial, son una parte
del gobierno federal y que en la sección donde está trabajando son alrededor de 12 personas, aunque en
ocasiones el tamaño del equipo de trabajo varía entre 6 y 10 personas, cuentan con un administrador de
Linux y con uno o dos administradores de Windows, por si nos preguntamos si en realidad había demasiada
gente trabajando en esto, pues ya sabemos que no es así.
Dado que cuentan con un sistema de alta seguridad FISMA, son un sistema crítico nacional, lo que según
el nos dice que esto significa que no tienen permitido ser hackeados por lo que la agencia dijo que no pueden
trabajar en la nube, así que para estar seguros tienen que mantenerse en sus instalaciones a la hora de trabajar.

¿Qué es el clima espacial?
Según Chris, el clima espacial abarca casi todo eso que está sucediendo en los 93 millones de millas que
existen entre la Tierra y el Sol, así que hay algunos tipos diferentes de fenómenos, como la radiación
electromagnética (como rayos x) y esto puede afectar las comunicaciones, a los humanos y al espacio.
Las partículas cargadas de energía que provienen de las llamaradas y eyecciones de masa coronal que
pueden impactar los satélites y comunicaciones de alta frecuencia, especialmente cerca de los polos,
esos son protones y electrones volando desde el Sol realmente rápido y golpeándonos.
Y los impactos del campo magnético pueden obtener plasma magnetizado que interactúa con el campo 
magnético de la Tierra que es lo que causa algunas auroras, pero igual puede afectar la red eléctrica de
maneras bastante negativas.

**Después Chris cuenta que hicieron y cómo comenzaron, en 2017...**
	1° - Tomaron un poco de entrenamiento en Jenkins/CI, con Docker.
	2° - Etiquetado a la antigua: integración de base de datos compartida.
	3° - Leyeron sobre una nueva forma: Construyendo Microservicios.
	4° - Encontraron un proyecto pequeño de alto valor (Servicio de Verificación).
	5° - Un equipo en dos: equipos de bases de datos y microservicios.
	6° - Desarrollan el Servicio de Verificación con nuevas reglas

Y ¿por qué Docker?
Pues una de las cosas principales son los problemas del software científico ya que a menudo tiene conflictos
delicados y simplemente dependencias extrañas, bibliotecas de las que realmente no hemos oído hablar...
pero se dieron cuenta que al transferir este tipo de cosas a Docker, esta fue la primera vez en la que esas
dependencias han sido bien documentadas y les permite iterar en descubrir eso, ya que si pierdes uno,
simplemente lo agrega a su Dockerfile y se construye de nuevo... y esto fue realmente una ayuda enorme 
para ellos, además de que hay una gran mejora y calidad en su software.

**Sus nuevas reglas:**

	* Solo una cosa habla con la base de datos.
		- Solo un servicio puede hablar a la base de datos.
	* Microservicios.
		- Una colección de servicios altamente cohesivos que resuelven cada parte del problema.
	* Pruebas automatizadas de extremo a extremo.
		- Jenkins puede levantar todos los componentes y dependencias, soltar algunos datos, etc.
	* Evento accionado.
		- Baja latencia. Se usa mensajería asíncrona para el acoplamiento.
	* Prácticas de 12factor.net
		- El nuevo valor predeterminado, especialmente la configuración en el entorno.
	* ¡Nuevas cosas!
		- Adoptaron Python Flask y Python en general en estos momentos, rabbitmq para
		  esa mensajería asincrónica, y usan contenedores Docker para todo.

Todo esto cambió a los desarrolladores, estaban muy contentos ya que dice que es muy emocionante aprender
nuevas tecnologías contemporáneas. El ritmo de aprendizaje fue rápido, los cambios iterativos fueron más fáciles.
Además de que el cliente estaba encantado con las capacidades que pudieron crear y con qué rapidez fueron enviadas,
ahora todo está n ese contenedor, todos pueden ejecutarlo en las máquinas de los demás y es mucho más rápido.


Lo aprendido en esta charla fue:

	- Gracias a esta charla, aunqué ya sé que Docker sirve para muchas cosas, no sabía que les puede ser muy
	  útil hasta esta clase de personas que se encargan de monitorear el clima espacial y bueno además 
	  obtuve información sobre qué es en realidad esta clase clima, igual fue interesante saber cómo aunque 
	  son pocas personas pueden encargarse de esta clase de trabajo tan importante, fue bueno saber que 
	  Docker realmente les está ayudando a facilitarles mucho el trabajo y me sigue impresionando la cantidad
	  de datos que puede manejar, porque supongo que deben de ser cantidades enormes ya que están hablando
	  sobre el espacio y para nada debe ser una tarea fácil.