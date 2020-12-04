# Examen Extraordinario

## Previo

- Desarrolla los ejemplos de código en tu computadora y envíalos al repositorio de la materia siguiendo los [lineamientos de contribución del repositorio](https://github.com/AnhellO/DAS_Sistemas#contributing)
- La carpeta del examen tendrá que llamarse `../Extraordinario/..`
- Cada ejercicio tendrá que ir en una carpeta por separado dentro de la carpeta de `Extraordinario/`, por ejemplo `Extraordinario/Ejercicio-1/..`
- Si el ejemplo solamente necesita comandos escritos entonces agregalos en un archivo `.md` (Markdown) que anexes por separado dentro de tu carpeta con las soluciones al examen. También es importante adjuntar las demás evidencias que se piden por cada ejercicio.

## Ejercicios

### Ejercicio 1

Elabora una clase `Figura`. De esta clase heredarán las clases `Circulo`, `Triangulo` y `Rectangulo`:

- Para cada clase, agrega la función `area`
- Para cada clase, sobreescribe la función de `__str__` de tal manera que podamos obtener una representación del objeto como string
- Crea la respectiva función `main` en la cual instancies y juegues con al menos 3 objetos diferentes para cada una de las clases pedidas anteriormente
- Finalmente crea una función dentro de tu test principal la cual reciba como parámetros una lista de objetos tipo `Figura` junto a un `string` que represente a un tipo de figura en específico (`'circulo'`, `'triangulo'` y `'rectangulo'`, o `'C'`, `'T'` y `'R'` por ejemplo). La función tendrá que devolver una nueva lista pero ahora filtrada con los objetos del tipo especificado en el segundo parámetro. Asegúrate de probar que la funcionalidad de este método es la esperada

### Ejercicio 2

Partiendo de la suite de tests unitarios en el archivo [`factory_method_test.py`](ejercicio-2/factory_method_test.py):

- Imagina que tenemos un sistema que se puede conectar a múltiples motores de bases de datos. Tenemos una conexión a `Oracle`, otra a `MySQL`, y una más a `MongoDB`, y queremos ser capaces de conectarnos a cada una creando múltiples conexiones a lo largo de todo el código de la aplicación
- Crea un nuevo archivo/módulo llamado `factory_method.py` e implementa la funcionalidad necesaria para que nuestro sistema sea capaz de crear múltiples conexiones a cada una de las bases de datos a través del patrón de diseño [`Factory Method`](https://refactoring.guru/es/design-patterns/factory-method). Esta "_factory_" deberá de ser capaz de conectarse a la base de datos deseada y en caso de que ninguna conexión se especifique, entonces tendrá que conectarse a `MySQL` por default
- Por motivos prácticos y de ejemplo la conexión a las bases de datos nos retornará solamente un `string` (revisa las salidas esperadas de los tests :wink:), no hay necesidad de implementar ninguna lógica de conexión ni nada complejo detrás
- Asegúrate de que la suite de tests unitarios pasa sin mayores problemas una vez que implementaste tu solución

### Ejercicio 3

Crea 2 contenedores por medio del cliente `CLI` de `docker`:

- El **1er contenedor** ejecutará un servidor de [`MongoDB`](https://hub.docker.com/_/mongo) y su nombre deberá de ser `m1`
- El **2do contenedor** ejecutará un cliente de [`Mongo Express`](https://hub.docker.com/_/mongo-express) el cual se llame `mexpress` y que se conectará al contenedor `m1` creado en el punto anterior. Otro requisito más es que este cliente tiene que estar protegido por medio de las siguientes credenciales:
  - Usuario: `DAS`
  - Password: `extra123`

Anexa los comandos utilizados para tu solución así como los screenshots necesarios que sirvan de evidencia para comprobar que llevaste a cabo este ejercicio en tu equipo.

### Ejercicio 4

Crea un `Dockerfile` que cumpla con los siguientes requisitos:

- Que extienda de la imágen base de [`Python 3`](https://hub.docker.com/_/python)
- Que utilice el directorio `/home/anonymous/app` como el directorio de trabajo
- Que copie el archivo [`server.py`](ejercicio-4/server.py) dentro del contenedor
- Que instale las dependencias necesarias para correr la aplicación que se encuentra en el archivo `server.py`
- Que ejecute el archivo `server.py`

Construye una imágen basada en el `Dockerfile` que acabas de crear, que use la versión `extraordinario` y que se llame `{mi-user}/hello_flask`, donde `{mi-user}` equivale a tu usuario de [`DockerHub`](https://hub.docker.com/). Una vez que hayas creado la imagen envíala a tu cuenta de `DockerHub`. Debe de estar accesible similar a como lo está en [este ejemplo](https://hub.docker.com/r/anhellojz/hello_flask). Asegúrate de adjuntar el link a ella en tus resultados del ejercicio.

Para finalizar, ejecuta un nuevo contenedor basado en la imágen que recién acabas de crear y que deberá de llamarse `hflask`. Este tendrá que correr "_daemonizado_", y deberá de estar accesible a través del puerto `9999` de tu máquina. Asegúrate de verificar que funciona de manera correcta :wink:.

Recuerda que **todo debe de funcionar** por medio de `docker`, es decir, nada debe de hacerse manualmente ni instalando algo en el equipo host.

Anexa los comandos utilizados para tu solución así como los screenshots necesarios que sirvan de evidencia para comprobar que llevaste a cabo este ejercicio en tu equipo.

### Ejercicio 5

Crea un archivo `docker-compose.yml` que ejecute 3 contenedores:

- El **1er contenedor** ejecutará un servidor de [`MySQL`](https://hub.docker.com/_/mysql) y su nombre deberá de ser `mysql`
- El **2do contenedor** ejecutará un servidor de [`PHPMyAdmin`](https://hub.docker.com/r/phpmyadmin/phpmyadmin/) el cual debe de tener acceso al servidor de la base de datos del _1er contenedor_. El contenedor deberá de llamarse `myadmin` y tendrá que estar protegido con el password `extra-admin123`
- El **3er contenedor** ejecutará un script que obtendrá los datos de la siguiente API pública: <https://restcountries.eu/>
  - Este tendrá que obtener **todos los países** de la API y guardarlos en una tabla `paises` dentro de la base de datos del _1er contenedor_
  - Para crear la base de datos y sus tablas puedes ayudarte de alguno de los `ORM` vistos en clase (como [`Peewee`](https://github.com/coleifer/peewee) por ejemplo), o bien, crear la base de datos y la(s) tabla(s) durante la creación del primer contenedor. Recuerda utilizar los recursos vistos en clase para apoyarte en este punto :wink:

Recuerda que **todo debe de funcionar** por medio de `docker-compose`, es decir, nada debe de hacerse manualmente ni instalando algo en el equipo host.

Anexa los comandos utilizados para tu solución así como los screenshots necesarios que sirvan de evidencia para comprobar que llevaste a cabo este ejercicio en tu equipo.

## Deadline

- `Lunes 7 de Diciembre a las 02:00pm`
