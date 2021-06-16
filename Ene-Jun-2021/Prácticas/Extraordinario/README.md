# Examen Extraordinario

## Previo

- Desarrolla los ejemplos de código en tu computadora y envíalos por correo electrónico al email de <asjz2892@gmail.com> por medio de un achivo comprimido `.zip` y con el siguiente asunto de correo: `DAS Sistemas Ene-Jun-2021 - Examen Extraordinario - {1er Nombre y 1er Apellido}` i.e. `DAS Sistemas Ene-Jun-2021 - Examen Extraordinario - Angel Jaime`. La carpeta del examen tendrá que llamarse `../Examen Extraordinario/..` y dentro de esta carpeta deberá de venir una carpeta dedicada para cada ejercicio, por ejemplo `../Examen Extraordinario/Ejercicio-1/..`
- Si el ejemplo solamente necesita comandos escritos entonces agregalos en un archivo `.md` que anexes por separado dentro de tu carpeta con las soluciones al examen. También es importante adjuntar las demás evidencias que se piden por ejercicio.

## Ejercicios

### Ejercicio 1

Crea una clase `Triangulo`. Su método constructor `__init __()` debe de tomar los siguientes atributos como argumentos:

- `self`
- `angulo1`
- `angulo2`
- `angulo3`
- `lado1`
- `lado2`
- `lado3`

Asegúrate de inicializarlos de forma adecuada en el cuerpo del método `__init __()`.

Una vez que hayas creado el esqueleto de la clase, asegúrate de implementar los siguientes puntos:

- Crea una variable de clase llamada `numero_de_lados` e inicialízala a `3`
- Crea un método llamado `verificar_angulos` que revise si la suma de los tres ángulos de un triángulo es igual a `180`, y en caso de que así sea deberá de devolver `True`, o `False` en caso contrario
- Crea una variable llamada `mi_triangulo` y configúrala a que sea igual a una nueva instancia de la clase `Triangulo`. Pásale tres ángulos que sumen `180` (por ejemplo, `90`, `30`, `60`).
- Agrega una función que nos de la representación en string de una instancia de la clase `Triangulo` con todos sus atributos

### Ejercicio 2

Crea tres nuevas clases llamadas `Isosceles`, `Equilatero` y `Escaleno`, las cuales deben de heredar de la clase `Triangulo` creada en el ejercicio 1.

Agrega una nueva función abstracta para la validación del tipo de triangulo llamada `validar_triangulo`, la cual deberá de implementarse en cada una de las nuevas clases heredadas y tendrá que verificar si el tipo de triangulo inicializado como instancia es del tipo valido de la clase.

### Ejercicio 3

Crea un diagrama UML que modele y represente a cada una de las clases creadas en el ejercicio 2. Puedes hacerlo a mano o por medio de alguna herramienta de software, como a ti te sea más cómodo, solamente asegúrate de adjuntar screenshots o fotografías de los diagramas de UML que hayas creado.

### Ejercicio 4

Implementa el patrón de diseño [`Factory Method`](https://refactoring.guru/es/design-patterns/factory-method) para las clases e instancias del ejercicio 2.

### Ejercicio 5

Crea una suite de tests unitarios para tu solución del ejercicio anterior. Puedes utilizar la librería nativa de `Python`, [`unittest`](https://docs.python.org/3/library/unittest.html), o bien una librería externa como [`pytest`](https://docs.pytest.org/en/stable/).

### Ejercicio 6

Partiendo del diagrama UML propuesto en el archivo [`memento_uml`](memento_uml.png), implementa el patrón de diseño `Memento` respetando la jerarquía de clases, atributos y funciones definida en el diagrama `UML`.

### Ejercicio 7

Partiendo del diagrama UML propuesto en el archivo [`facade_uml`](ejercicio-8/facade_uml.png), y de las clases existentes en la carpeta de [`facade/`](facade/), implementa el patrón de diseño `Facade` respetando la jerarquía de clases, atributos y funciones definida en el diagrama `UML`.

### Ejercicio 8

¿Cuál es el comando que necesito ejecutar para poder levantar un contenedor de `Docker` que corra un servidor de [`MySQL`](https://hub.docker.com/_/mysql) versión **8** y que cumpla con los siguientes puntos?

- Que el contenedor se llame `database_mysql`
- Que el contenedor se ejecute en el background (es decir, que se mantenga en ejecución)
- Que el puerto asignado a la máquina host sea el `4444`
- Que el usuario sea `extra`
- Que el password sea `ordinario123!`
- Que se cree una base de datos llamada `pruebas`

¿Con qué comando(s) puedo conectarme a mi base de datos de `MySQL` corriendo dentro de mi contenedor de `mysql_db`?

Finalmente, ¿qué comando necesito utilizar para ejecutar un contenedor de [`adminer`](https://www.adminer.org/) que funja como DBMS y que se conecté a la base de datos de `MySQL` creada previamente?

Puedes utilizar `Docker Compose` si te es más sencillo.

Anexa los comandos utilizados para llevar a cabo este ejercicio, así como screenshots de evidencia de que llevaste este ejercicio a cabo en tu equipo.

### Ejercicio 9

Contesta a los siguientes cuestionamientos partiendo del [archivo `app.py` existente en la carpeta de `ejercicio-9/`](ejercicio-9/app.py):

- ¿Cuál es el archivo `Dockerfile` que necesito crear para construir una imágen que corra mi `app.py`?
- ¿Qué comando necesito ejecutar para construir una imágen basada en el `Dockerfile` creado en la pregunta anterior?
- ¿Qué comando(s) necesito ejecutar para poner mi pequeña aplicación en funcionamiento?

Puedes utilizar `Docker Compose` si te es más sencillo.

Anexa los comandos utilizados para llevar a cabo este ejercicio, así como screenshots de evidencia de que llevaste este ejercicio a cabo en tu equipo.

### Ejercicio 10

Crea el diagrama de arquitectura para el ejercicio anterior. Puedes utilizar la herramienta que gustes para llevar esto a cabo, solamente asegúrate de adjuntar el diagrama resultante dentro de tus respuestas.

## Deadline

* `Sábado 19 de Junio a las 11:59pm`
