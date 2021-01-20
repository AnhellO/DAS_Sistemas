# How to get Started with Docker | @pmckee

## Agenda
- Que son los contenedores y por que nos importa?
- Instalar Docker
- Escribir Dockerfiles y construir Imagenes
- Correr y administrar Imagenes
- Enviar Imagenes a la nube
- Docker Compose para desarrollo local

### Por que Docker?
El problema es principal por el cual se utiliza Docker es simple, todas las Maquinas individuales o las maquinas virtuales llevan mucho trabajo (Instalar SO, parchearlo, installar dependencias para la aplicacion) asi como tener en cuenta que estas maquinas deben tenerse al dia, actualizar su seguridad. Basicamente la solucion que se tiene para ahorrar todo ese trabajo, espacio y tiempo es utilizar Docker, al momento de utilizarlo estamos juntando todo nuestro codigo, soporte binario y configuraciones en un paquetito muy choncho llamado Imagen y estas despues se van a servidores y si cae, solo agregas otra, ya que son Ephimerales, lo que significa que estas imagenes tiene un promedio corto de vida.

### Las 3 fases de Docker
- **Construir la Imagen**: Empaquetar todo lo que necesitas para correr tu aplicacion de una manera consistente.
- **Embarcar/Enviar la Imagen**: Enviar estas Imagenes de una manera facil para que sean utilizadas en tu nube o en tu maquina desarrollo local.
- **Correr la Imagen**: Executar tu aplicacion de una manera facil y consistente.

Y con estas tres fases podemos tener todos los beneficios de un programa normal: *Continous integration*, *Continuos Deployment*, *Versiones diferentes*, *Roll Forward*.

### Docker for Desktop
Y la manera mas sencilla para iniciar con Docker es utilizando Docker for Desktop. solo se necesita entrar y descargar.

### Demo
Un Dockerfile es una lista de comandos que es emviada a la Docker engine para construir una imagen, este lee de arriba hacia abajo con singularidad alegria.
Los comandos mas comunes utilizados en los Docker files son:
- **FROM:**  Establece la imagen base desde donde se va a construir tu programa con todo lo que necesitas.
- **WORKDIR:**  Establece el directorio de trabajo para cualquier instrucción dentro del Dockerfile.
- **ENV:**  Establece variables de entorno
- **COPY:**  Copia los archivos de un lugar en el host hacia el contenedor en el WORKDIR.
- **RUN**: Ejecuta cualquier comando que se le diga.
- **CMD:**  Proporciona el comando por defecto que corre un contenedor al ser ejecutado.

Comandos importantes al utilizar Docker:
- **Docker build .**: Este se utiliza para construir una imagen (a base de un dockerfile en el mismo directorio).
- **Docker build --help**: Ver que comandos podemos usar.
- **Docker images**: Nos muestra las imagenes que tenemos en nuestra maquina.
- **Docker run**: Corre las imagenes
- **Docker ps**: Ver que esta corriendo en tu maquina
- **Docker ps -a**: Ver todas las imagenes en tu maquina

### Docker hubbing 
Docker hub es basicamente la utopia de las imagenes, un repositorio en la nube donde todas las imagenes pueden vivir, trabajar, reproducirse. necesitas un Docker ID para utilizar y crear un Repositorio para agregar tus imagenes en la nube.