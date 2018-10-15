# Reporte Conferencia ClickIt - Introducción a Docker

_11/10/2018_

### Docker es una tecnología de virtualización donde se puede tener de uno a muchos contenedores en ejecución.  
Un contenedor es una forma de separar la aplicación y todas sus dependencias y empaquetarlas, esto hace que puedas compartir el contenedor a otro equipo sin importar sus características o versiones de software instalado.

 Docker cuenta con imágenes de contenedores que también se crean de una manera especial las cuales serán usadas al lanzar un contenedor.  

_Una imagen de Docker es un conjunto de capas._ 

  
**Al utilizar una Máquina virtual necesitas:**  
- Host  
- Computador  
- **Se construye todo desde cero (Sistema Operativo).**  
  
**Con un container se hace uso de los recursos del equipo local.**  
  
## Comandos más comunes  
- Maintainer  
- From (de quien es la imagen)  
- Add (crea capas) 
- Copy 
- Entry point (define entrada de inicio)  
- Cmd (añade parámetros al entry point)  
- Expose (permite abrir y correr archivos dentro del container)  
  
## ¿Por qué usar Docker?  
Porque crea ambientes inmutables, es muy portable, nos brinda seguridad al manejar un ambiente aislado. Para hacer que sea seguro es necesario que los procesos NO tengan privilegios de root.

### Quién usa Docker
Empresas como:
- General Electrics
- Spotify
- Netflix
- Riot Games
- Google
- Ebay
- PayPal
- Disney
- The New York Times

