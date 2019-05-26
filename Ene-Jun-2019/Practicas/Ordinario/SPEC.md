# Ordinario

## Objetivo

Crear una especie de campaña de marketing por email que sugiera y/o recomiende animes y mangas a usuarios suscritos a una lista de correo electrónico

## Especificaciones

* Desarrolla los ejemplos de código en tu computadora, y envíalos al repositorio de la materia, siguiendo los [lineamientos de contribución del repositorio](https://github.com/AnhellO/DAS_Sistemas#contributing). La carpeta del examen tendrá que llamarse `../Ordinario/..`
* Las pruebas de tus ejercicios (es decir, los objetos que instancies y las pruebas que hagas) deberán de estar dentro de la función `main` para cada ejercicio
* No es necesario leer un input/entrada desde la consola (terminal), pero puedes hacerlo si así gustas
* **NO** envíes tu pull request hasta la hora límite (`05:00am` del `Junio 2, 2019`) para evitar que este sea copiado :wink:

## Ejercicios

#### Parte 1

* Crear un script en `python` que trabaje con la API https://jikan.moe/
  * El script deberá de leer al menos 10 elementos de cada uno de los siguientes endpoints, guardándolos en un base de datos en `SQLite`
    * Animes: https://jikan.docs.apiary.io/#reference/0/anime
    * Mangas: https://jikan.docs.apiary.io/#reference/0/manga
    * Personajes: https://jikan.docs.apiary.io/#reference/0/character
    * Tu eliges cuales resultados/ids de los endpoints guardar, y cómo hacerlo
  * Crear al menos una tabla diferente para cada uno de los endpoints/objetos anteriores

#### Parte 2

* Crea una cuenta en https://mailchimp.com/, y genera tu API Key para poder utilizar la [API](https://developer.mailchimp.com/)
  * Explora el servicio de Mailchimp
  * Lee la [documentación oficial](https://mailchimp.com/help/getting-started-with-mailchimp/)
* Depués de familiarizarte con Mailchimp, su funcionalidad y su API, crea un script en `python` que se encargue de suscribir a cada uno de [tus compañeros de la clase y al maestro](https://www.dropbox.com/s/40pzif0bgyjg4dy/Screenshot%202019-05-25%2019.44.31.png?dl=0) a la audiencia/lista de suscriptores, utilizando ya sea tus propios métodos, funciones y objetos, o bien, el siguiente [paquete](https://github.com/VingtCinq/python-mailchimp).

#### Parte 3

* Crear un último script en `python` que lea los datos guardados en la BD durante la parte 1 del proyecto utilizando el [ORM de Peewee](https://www.fullstackpython.com/peewee.html), y que haga lo siguiente con ellos:
  * Agruparlos en una lista o diccionarios para cada tipo (es decir, **Anime**, **Manga** y **Personaje**). Puedes elegir la estructura de datos que más te convenga
  * Generar un archivo o string en formato `HTML` que contenga la información anterior procesada. Puedes generar desde una simple tabla hasta algo más elaborado, ya queda en ti :wink:
  * El `HTML` generado deberá ser enviado en forma de correo electrónico de marketing a los emails de tu audiencia/lista en Mailchimp, suscritos durante la parte 2 del proyecto. El correo deberá de ser enviado utilizando la [API de Mailchimp](https://developer.mailchimp.com/documentation/mailchimp/reference/campaigns/#action-post_campaigns_campaign_id_actions_send). Puedes enviar desde el simple `HTML` hasta algo más estilizado y con forma de [campaña de marketing por email](https://blog.hubspot.com/blog/tabid/6307/bid/32854/10-simply-awesome-examples-of-email-marketing.aspx), pero recuerda que todos podremos ver tu email :wink:

#### Puntos extra

* El email más creativo/estilizado se lleva buenos puntos extra :wink:
