### Labels, Labels, Labels


Andy Clemenko, quien es ingeniero de soluciones en StackRox, nos comenta por qué decidió dar esta charla
acerca de etiquetas, diciendo que una de las cosas que siempre le ha parecido interesante fue la falta de 
comprensión en torno a las etiquetas. Nos comienza a contar que él como ex contratista del Departamento de
Defensa, había construído un gran registro pero tuvo algunas preguntas que recibía constantemente, la cuales eran...
¿de dónde vino esta imagen?, ¿qué hay ahí dentro?, ¿cómo llegó esto aquí?, ¿cuándo fue construida?, etc., y una 
de las cosas que hicieron para poder aliviar algunas de esas preguntas fue estableciendo un conjunto básico de etiquetas.
Las etiquetas realmente están diseñadas para proporcionar tantos metadatos alrededor de la imagen como sea posible, 
por lo que una forma interesante de prevenir algunos de estos problemas es a través del uso de estas mismas.
¿Qué es el Label Schema?
Es solo un valor clave, es cualquier clave y prácticamente cualquier valor, así que para comenzar podríamos tener 
algunas de las siguientes claves como:
	
	- Autor
	- Fecha
	- Descripción
	- Versión
	- Y más...

Estas claves anteriores son parte de la información básica sobre la imagen, pero que realmente sería bastante útil tener,
y ¿qué pasa con las Etiquetas específicas para CI (Integración Continua)?, estas podrían ser como:

	- Fuente de control de versiones   (Ya sea Git, GitLab, GitHub, etc.)
	- Número de commit (Serviría en términos de seguimiento)
	- Cómo se construye (Serviría para el trabajo de desarrollo)
	- Dónde fue construido 
	- Número de compilación

Pero no sólo podemos hablar de Integración Continua, también lo podemos hacer sobre seguridad, como por
ejemplo las siguientes Etiquetas para Seguridad:

	- Servidor que lo construyó
	- Número de control de versión
	- Número específico de commit
	- Cómo fue construído
	- Número de compilación

Ahora Andy nos muestra algunos ejemplos de etiquetas en un ejemplo real:

	- "org.opencontainers.image.authors":"clemenko@gmail.com",
	- "org.opencontainers.image.source":"https://github.com/clemenko/dc20_labels/tree/master/demo_flask",
	- "org.opencontainers.image.build":"docker build -t clemenko/flask_demo...",
	- "org.opencontainers.image.build_number":22,
	- "org.opencontainers.image.build_server":http://jenkins.dockr.file/,
	- "org.opencontainers.image.commit":"98c997f"
	- "org.opencontainers.image.description":"05/07/20"

¿Pero dónde construímos etiquetas?  - La forma en que se agregan etiquetas es a través del Dockerfile.
¿Cómo podemos ver las etiquetas?  - Hay 2 formas principales de ver las etiquetas, la primera es obviamente 
un estibador y una inspección de estibador, podemos extraer la imagen localmente, podemos inspeccionarla, etc.
La otra forma que nos presenta, que encontró recientemente, fue Skopeo de Red Hat, esto permite consultar
realmente el servidor de registro, por lo tanto ni siquiera tiene que extraer la imagen inicialmente, y puede ser
realmente útil si estás en una estación de trabajo de desarrollo realmente pequeña y quieres implementar aplicaciones
de una manera muy simple.


Lo aprendido en esta charla fue:

	- Obtener información acerca de las etiquetas, qué es el Label Schema, recomendaciones tales como que es muy bueno
 	  utilizarlas ya que es una forma integrada de documentar todos los aspectos de las imagenes en sí, y lo que Andy espera 
	  es que aquellas personas que estuvieron en esta sesión puedan estandarizar las etiquetas en el lugar en el que se 
	  encuentren trabajando, ya que cómo lo comenta, hay mucha falta de comprensión en torno a estas.