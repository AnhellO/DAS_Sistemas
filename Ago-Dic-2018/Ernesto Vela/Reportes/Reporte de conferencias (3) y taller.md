#Voice Search
##Web content optimization for VoiceSearch

#Que es VoiceSearch?
Funcion que permite a los usuarios buscar en internet, usando comandos de voz
en lugar de escribir

#Datos Estructurados
Ayudan a los navegadores a entender el contenido de los sitios web de manera
ordenada sin la necesidad de leer datos adicionales, son como etiquetas y aunque
el usuario no los ve, las maquinas si.

#Tipos de datos Estructurados
-Microdata
-RDFA (Resoruce Description Framework in Atributes)
-JSON Ld (JavaScript Object Notation for Linked Data)

Google esta empujando mucho el machine learning

#Como optimizar mi contenido?
-Formato preguntas y respuestas
-Terminos clave y conversacionales
-Datos Estructurados

Google my business

#Sitios populares optimizados
-Amazon
-Google
-Youtube
-Netflix

#Teconologia de este anio:
GOOGLE DUPLEX

#El futuro que esperamos:
google duplex
voice shopping
smart homes

Opinion:
Me gusto mucho esta conferencia ya que es muy inovadora, es lo que estamos viviendo
en este momento y muy probablemente es algo que se vovlera parte de nuestras
vidas diarias, en lo que vamos a in evolicionando, me interesa aprender mas
sobre estos temas aunque se que es algo grandisimo, pero mas vale in empezando
de una vez ;)

___

###DevOps
TXM Enrique Vargas

Development operations no es un rol, es una cultura/metodologia de trabajo que
utiliza google, amazon, es un desarrollo de software.

No se usa el ciclo casual (cascada), sino que uno en espiral que es mas veloz.

Enfocado en la metodologia SCRUM y metodologias de desarrollo tipo AGILE.

#DevOps ocupa
1.Aplication Development
2.Aplication Testing QA

DevOps promueve una entrega mas rapida, productos de mejor calidad y una mejor
estabilidad de la aplicacion, lo que permite a los desarrolladores centrarse
en las funciones principales.

#Objetivos de DevOps
-Desarrollos mas rapidos
-Mayor calidad
-Mayos estabilidad
-Reduccion de costos

#Factores de exito para DevOps:
-Compromiso y liderazgo
-Debe haber separacion de resposabildiades
-Proceso de equipo documentados
-Herramientas adecuadas para el trabajo
-Planes de comunicacion internos y externos en su lugar y activos

#Porque es importante DevOps?
Mayor eficiencia y calidad reduciendo el downtime y riesgo de produccion.
Clientes ven la reduccion de costos con una entrega mas rapida y mejor calidad .

Opinion:
Me gusto la conferencia porque entendi de lo que hablaban, ya que semestres antras
lleve una clase sobre el tema este, y todo l oque iban mencionando y explicando ya
lo conocia, y verlo en el area laboral y profecional ,e gusto bastante, darme
cuenta que si estoy aprendiendo y que lo que estoy aprendiendo si se utilzia
al momento de ir a trabajar.

___

#ClickIt
##Introduccion a Docker

Que es?
Una compania y un producto
Tecnologia para la generacion de contenedores

#Objetivo principal
Aisalr procesos y aplicaciones del sistema principal(host) y brindar mayor
seguridad a las aplicaciones y sistema

#Que es un contenedor?
Es una forma de separar procesos de manera independiente, pueden ser agrupados
en imagenes, hace uso del kernel.

Una virtualizacion normal tendria que emular cada aspecto del sistema que desea
lanzar

#Que es una imagen docker?
Un conjunto de capas, cada que se realize un cambio se genera una capa diferente

#Comandos principales
1.Maintain
2.From
3.Add
4.Copy
5.Run
6.Env
7.Entrypoint
8.CMD

##Ejemplo:

~~~
Maintain "Darwin" "dwin.1@history.com"
From cuerpo:2010
Add int
Add Paciencia
Add H. Prog
Add Ropa
Add apt update 8.8 apt install kokoro lang frances \
    reloj alas venas

CDM ["cerebro"]
~~~

#Porque usar Docker?
Porque permite la creacion de ambientes inmutables ademas de ser muy portable.
Nos brinda seguridad al manejar un ambiente aislado.

#Es seguro?
El principal problema de docker es el mismo que le da sus ventajas,
ya que al usar secciones de kernel de host, un ataque puede relaziarse para
ganar acceso al kernel principal.
Para esoo debes asegurarte que los procesos corran en ambientes sin
privilegios de root, para que en caso de un ataque solo se tenga acceso
a una seccion del contenedor y no a todo.

Opinion:
Muy buena conferencia, y como fue despues de haber tomado el taller de Docker
pues entendi muy bien de todo lo que hablaron, mencionaron gran parte de la
info aprendida en el taller, aunque de todas formas dieron a conocer mas
informacion sobre todo teoria que no vi en el taller, y eso me hizo complementar
lo aprendido.

___

#Taller
##Aplicaciones y servicios basados en arquitectura Docker

###paybook
####Docker basics

#Arquitecturas
1.Traditional servers (bare metal)
#PROS:
-utilization of raw resources
-isolation
#CONS:
-veri slow deployment time
-expensive
-wasted resurces
-difficult to scale
-difficult to migrate
-complex configuration

2.Virtual machines
#(hypervisor)
software que controla las maquinas virtuales y les manda los recursos
(el sistema operativo de la base puede ser diferente al de la maquina virtual)
#PROS:
-good use of resoruces
-easy to scale
-easy to backup and migrate
-cost efficiency
-flexibility

#CONS:
-resoruce allocation
-vendor locjin
-complex configuration

3.Containers
#(OS kernel)
#(Container runtime)
#Contenedores hechos en windows corren en linux
de linux a windows no

#PROS:
-isolation
-lightweight
-resource effective
-easy to migrate
-security
-low overhead
-mirror environments

#CONTS:
-architecture
-resoruce heavy apps

#¿Qué es un contenedor?
unidad de software que viene empaquetado

#Opinion:
En este taller aprendimos de manera rapida lo que es el uso de los contenedores
Docker, el primer dia nos ensenaron los conceptos basicos, los ccomandos que
utilizariamos a lo largo del taller, y ademas de conocerlos ,los utilziamos.
El segundo dia ya fue un poco mas de practica, ya que vimos todas las imagenes
que tiene Docker, ademas de que antes aprendimos a instalar docker y la maquina
virual para trabajar con el.
El ultimo dia, ademas de haber usado todos los comandos, creamos procesos y Una
vinculacion con una base de datos sql, donde podiamos ver cuertos codigos desde
el navegador, que fue lo que se me hizo mas intereesante a mi.
