# Best practices for Compose-managed Python Applications | Anca Lordache

Empezar un proyecto siempre es tardado, pero utilizando Docker simplificaremos todo esto.

## Agenda
 - Como poner en marcha rapidamente un entorno de desarrollo reproducible administrada por compose para una aplicacion de python.
 - Aplicar actualizaciones codigo y debug a las aplicaciones de python en contenedores

teniendo en cuenta estos datos empezaremos por:
>Bootstrapping un proyecto de python:
- **Decomposicion de la applicacion**: la estructura del proyecto
- **Contenedores**: Dockerfile y Docker-Compose

>Lanzar utilizando Docker-compose:
- **Actualizar el codigo python**
- **Debuggear el codigo python**

Se empiza separando un proyecto de python en 3 partecitas
> La UI -> La logica (Flask) -> Data (MySQL)

Es bien dicho que una buena manera de estructurar los servicios es tener un directorio por servicio

### Best practices for Dockerfiles
**From**: 
- Utiliza la imagen de python (basada en debian) como imagen base
- para que la imagen sea lo mas pequena posible, y el optimizar estos utiliza *Python:< version >-alpine*

**Copy & Run**:
- Copia solo los archivos de las dependecias y luego instalalos
- Aprovecha los cache de las versiones para en el futuro acelerar el proceso.

**Copy & CMD**:
- Copia los archivos fuente y corre el servidor de python

### Best pracrtices for compose file
- **No network defined**: todos los servicios estaran en el mismo canal
- Definir volumenes para los datos que se usan en las bases de datos persistentes
- Definir secretos para de manera segura pasar credeciales a los servicios

### Managing Code Updates
Un ciclo visto en la presentacion fue:
Update Source Code -> Build Docker Image -> Re-Run Process/Container -> Debug Code.