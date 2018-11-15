# Conferencia de: Docker

## ¿Qué es Docker?
* Es un proyecto desarrollado por la comunidad en conjunto con la compañía que
  lo creó, para hacer un mejor producto que pudiera ser útil para todos.

* A grandes razgos, Docker es una TECNOLOGIA DE VIRTUALIZACION usada escencialmente
  para aislar procesos y aplicaciones del sistema principal (o Host) y brindar
  mayor seguridad a las aplicaciones y al sistema que las hospeda.

## Docker:
* Se diferencía de una virtualizacion normal, la cual tendría que emular cada
  aspecto del sistema que desea lanzar.

* Se basa de:
    * Virtualización
    * Containers

## ¿Qué es una imagen de Docker?
* Una imagen de Docker es un conjunto de capas, donde cada una de estas se genera
  cada vez que realizamos algún cambio a la imagen de base que nos encontremos
  usando en ese momento.

* Esto es posible gracias a ciertos comandos que son necesarios al momento de
  la construcción de una imagen de los cuales, los más importantes son:
  * MAINTEINER
  * ADD
  * FROM
  * COPY
  * RUN
  * ENV
  * ENTRYPOINT
  * CMD

## ¿Por qué usar Docker?
* Una de las razónes para usar Docker es porque permite la creación de
  Ambientes Inmutables. Además de ser muy Portable, y es muy fácil de lanzar
  un container en caso de que se requiera uno más o que el actual falle.

* Por otra parte nos proporcionan seguridad al manejar un ambiente aíslado.

## ¿Quién usa Docker?
* IBM
* RIOT
* Google
* Netflix
* Spotify
* Paypal
* eBay
* Disney
