# Proyecto Ordinario - Microservices Architecture

## Especificaciones

### Inicio

Crear un nuevo repositorio para el proyecto final en la cuenta de cualquiera de los miembros del equipo.

Los miembros restantes deberán de crear un fork de este repositorio y contribuir en él conforme se vaya desarrollando la práctica.

Al final cada elemento del equipo deberá de subir un link al repositorio del proyecto final en su propia carpeta de alumno dentro de un archivo `.md` el cual deberá de estar bajo una nueva sub-carpeta que se llame `Ordinario`.

### Desarrollo

Crear un archivo `docker-compose.yml` por medio del cual se instancien **múltiples** contenedores que satisfagan la siguiente propuesta de problema.

Necesitamos construir una API sencilla que nos permita registrar transacciones de usuario y tener un panorama general de como usan su dinero.

Para llevar esto a cabo, tienes que implementar una API que nos permita almacenar transacciones de usuario.

Cada transacción tiene `referencia` (única), `fecha`, `total`, `tipo` y `categoría`, y luce de la siguiente manera:

```json
{
    "reference": "000051",
    "date": "2020-01-13",
    "amount": "-51.13",
    "type": "outflow",
    "category": "groceries",
    "user_email": "janedoe@email.com"
}
```

Se tienen que tomar en cuenta los siguientes puntos:

* La `referencia` de una transacción es única
* Solamente existen dos tipos de transacción: `inflow` y `outflow`
* Todas las transacciones de tipo `outflow` son numeros decimales negativos
* Todas las transacciones de tipo `inflow` son numeros decimales positivos
* Es posible recibir transacciones en masa también, ya sea por medio de un archivo externo o dentro de una misma petición
* Las transacciones que recibamos pueden ya existir en nuestro sistema, por lo que es necesario validarlas para evitar duplicados en nuestra base de datos

### Objetivos

Dado el siguiente ejemplo de entrada de datos:

```json
[
    {
        "reference": "000051",
        "date": "2020-01-03",
        "amount": "-51.13",
        "type": "outflow",
        "category": "groceries",
        "user_email": "janedoe@email.com"
    },
    {
        "reference": "000052",
        "date": "2020-01-10",
        "amount": "2500.72",
        "type": "inflow",
        "category": "salary",
        "user_email": "janedoe@email.com"
    },
    {
        "reference": "000053",
        "date": "2020-01-10",
        "amount": "-150.72",
        "type": "outflow",
        "category": "transfer",
        "user_email": "janedoe@email.com"
    },
    {
        "reference": "000054",
        "date": "2020-01-13",
        "amount": "-560.00",
        "type": "outflow",
        "category": "rent",
        "user_email": "janedoe@email.com"
    },
    {
        "reference": "000051",
        "date": "2020-01-04",
        "amount": "-51.13",
        "type": "outflow",
        "category": "other",
        "user_email": "johndoe@email.com"
    },
    {
        "reference": "000689",
        "date": "2020-01-10",
        "amount": "150.72",
        "type": "inflow",
        "category": "savings",
        "user_email": "janedoe@email.com"
    }
]
```

1.- Queremos ser capaces de ver un resumen que nos muestre el `inflow` y `outflow` total por usuario. Ejemplo:

```json
GET /transactions?group_by=type

[
    {
        "user_email": "janedoe@email.com",
        "total_inflow": "2651.44",
        "total_outflow": "-761.85"
    },
    {
        "user_email": "johndoe@email.com",
        "total_inflow": "0.00",
        "total_outflow": "-51.13"
    }
]
```

2.- Queremos poder ver un resumen de usuario por categoría que muestre la suma de cantidades por categoría de transacción. Ejemplo:

```json
GET /transactions/{user_email}/summary

{
    "inflow": {
        "salary": "2500.72",
        "savings": "150.72"
    },
    "outflow": {
        "groceries": "-51.13",
        "rent": "-560.00",
        "transfer": "-150.72"
    }
}
```

### Expectativas

* Construye la aplicación utilizando `Python`
* Los endpoints o rutas son solo ejemplos, siéntete libre de cambiarlos de acuerdo a tus necesidades, solamente se espera que sigas el formato de respuesta
* Agrega test unitarios y/o de integración
* Optimiza en función del tiempo disponible y no del rendimiento de la aplicación
* Dockeriza tu aplicación en base a lo visto en clase :wink:
* Utiliza [`Flask`](https://flask.palletsprojects.com/en/2.1.x/) (y [`flask-restful`](https://flask-restful.readthedocs.io/en/latest/)), [`FastApi`](https://fastapi.tiangolo.com/) o [`Django`](https://www.djangoproject.com/) (y [`DRF`](https://www.django-rest-framework.org/)) como alguno de los frameworks para tu API
* La base de datos es libre

#### Opcional - Puntos Extra

Los siguientes puntos son opcionales, sin embargo implementarlos provee **3** puntos extra por cada uno sobre la **calificación total final**.

* Utilizar [Swagger](https://swagger.io/) en tu proyecto y agregar un contenedor nuevo con el [`Swagger UI`](https://hub.docker.com/r/swaggerapi/swagger-ui) de la aplicación
* Agregar [RabbitMQ](https://www.rabbitmq.com/) para alguna o todas las operaciones CRUD de la aplicación
* Agregar un contenedor extra que provea un frontend (GUI) que consuma la API que creaste. Acá puedes utilizar tecnologías como `HTML`, `CSS`, `Javascript`, `Bootstrap`, `Vue`, `Angular` o `ReactJS` para hacer más rápido este proceso. Queda a tu criterio, imaginación y creatividad el cómo luzca la interfaz final :wink:
* Agregar testing y/o automatización de pruebas por medio de <https://github.com/testcontainers/testcontainers-python>

### Conclusión

Crear un archivo `README.md` en el que se incluya lo siguiente:

* Un diagrama de la arquitectura de tu proyecto y un diagrama de la base de datos (`DER`). Pueden apoyarse de algunas herramientas como <https://github.com/mingrammer/diagrams> o <https://app.diagrams.net/> para generar los diagramas del proyecto. Este diagrama también debe de incluirse como imágen dentro del proyecto final
* Los pasos a seguir detallados y concisos que indiquen como hacer funcionar el proyecto, de tal manera que pueda ser revisado sin mayores complicaciones

Finalmente, agreguen un video en equipo, en donde se exponga a detalle su proyecto y se hagan pruebas con él. Queda a criterio del propio equipo el como llevar a cabo la presentación, pero sí es necesario que cada miembro participe en la misma.

* Llevar a cabo este punto por medio de `MS Teams` y subir el archivo `.mp4` a algún drive público adjuntando el link de acceso al video al archivo `README`.md
* La exposición no debe tener una duración mayor a **15** minutos

## Recursos

### Arquitectura

* <https://www.oreilly.com/library/view/software-architecture-patterns/9781491971437/ch04.html>
* <https://www.microservices.com/>
* <https://microservices.io/patterns/microservices.html>
* <https://medium.com/hashmapinc/the-what-why-and-how-of-a-microservices-architecture-4179579423a9>
* <https://github.com/GoogleCloudPlatform/microservices-demo>
* <https://microservices-scaffold.readthedocs.io/en/latest/>
* <https://medium.com/@sonusharma.mnnit/building-a-microservice-in-python-ff009da83dac>
* <https://www.paradigmadigital.com/dev/como-construir-microservicios-en-python-1-2/>
* <https://codigofacilito.com/articulos/microservcios>
* <https://steemit.com/spanish/@jza/nameko-framework-de-microservicios-con-python>
* <https://ichi.pro/es/microservicios-de-python-api-objetos-y-modelos-de-datos-de-almacenamiento-170228015369526>

### Librerías

* <https://www.rabbitmq.com/getstarted.html>
* <https://github.com/Pungyeon/go-rabbitmq-example/blob/master/README.md>
* <https://kafka.apache.org/>
* <https://redislabs.com/blog/use-redis-event-store-communication-microservices/>
* <https://docs.celeryproject.org/en/stable/getting-started/introduction.html>
* <https://autobahn.readthedocs.io/en/latest/asynchronous-programming.html>
* <https://xpdays.com.ua/programs/event-driven-systems-with-mongodb/>
* <https://github.com/python-microservices>
* <https://nameko.readthedocs.io/en/stable/>

## Deadline

* `Domingo 12 de Junio a las 11:59pm`
