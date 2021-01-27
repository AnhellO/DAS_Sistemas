### How to improve your image builds using advance Docker build


Nicholas Dille, quien es ingeniero DevOps y trabaja para Houfe Group en Alemania, habló de cómo mejorar
las compilaciones de imagen de nuestro contenedor usando BuildKit.
Docker sigue siendo la herramienta estándar para crear imágenes de contenedores. Durante más de 
un año, Docker se entrega con BuildKit como un generador de imágenes alternativo, que proporciona 
funciones avanzadas para la gestión de caché, pero ¿Qué es BulidKit según Nicholas?, 
él dice que Docker viene con dos motores de construcción, el primero es el motor de compilación heredado, 
es el valor predeterminado cuando ejecuta los comandos de compilación de un acoplador,  y al mismo 
tiempo Docker trae el segundo motor que es BuildKit, que es un componente del proyecto Moby y ya se ha 
integrado a Docker, solo que no está habilitado, pero menciona que habilitar BuildKit es tan fácil como crear 
una variable de entorno.
Entonces al configurar buildkit en 1 o sea así ---> docker_buildkit=1, esto le dará acceso a todas las excelentes
funciones y mejoras en el generador de imágenes. 
Luego muestra una demostración donde ejecuta una misma compilación pero lo hace para poder
enseñarnos la diferencia entre el motor de compilación heredado y luego lo hace con BuildKit,
y cuando utiliza el motor heredado se muestran todos los pasos ejecutándose de uno en uno y al final
nos muestra que la construcción general tarda casi 28 segundos en completarse, al realizar de nuevo la
compilación pero ahora con BuildKit, podemos apreciar que la construcción general solo tardó cerca de
12 segundos por lo que lo que más recalca Nicholas es la rapidez con la que trabaja BuildKit.


Lo aprendido en esta sesión fue:

	- Obtuve algo de información acerca de BuildKit y fue bueno ya que no había escuchado de este
	  motor de construcción de imágenes, viendo los ejemplos que muestra Nicholas se puede
	  apreciar que si es considerablemente más rápido pero al estar viendo los comentarios de las
	  personas que escribían en el chat en vivo, leí que parece ser que BuildKit no está disponible
	  para Windows :c  por lo que creo que solo es posible utilizarlo en Linux.
