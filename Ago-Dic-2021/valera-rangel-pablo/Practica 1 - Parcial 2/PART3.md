# Parte 3 
## Monolito
Una gran parte de las aplicaciones que nosotros conocemos estan hechas por medio de la arquitectura de monolito, esto debido a que muchas de ellas van empezando y algunas de disponen de un presupuesto muy elevado para poder tener una arquitectura de microservicios.
En la aplicaciones monoliticas todo depende de un servicio lo cual hace mas simple el manejo de la misma, esto tiene sus pros y sus contras

Una de las desventajas seria que al tener nosotros una aplicacion sumamente grande, se nos complicara demasiado hacer una actualizacion porque practicamente se debe reescribir el codigo entero.

Estas son dificiles de escalar y generan costos de quiebre, esta siento que es su mayor desventaja que es demasiado dependiente de las demas funciones, y por ende si una funcion deja de funcionar: deja de funcionar toda la aplicacion.

## Microservicios
Ahora volteando del lado de los microservicios cambia totalmente la cosa, aqui ya entrarian las grandes empresas que tienen que tienen cantidad de dinero necesaria para poder llevar a cabo este tipo de arquitectura.

Aqui siento yo que tiene desventajas pero serian desventajas de costo a corto plazo, pero esto es muchisimo mejor a la de monolito, que si se cae un servicio se cae todo, me refiero al costo en corto plazo debido a todo el personal que debe estar activo monitoreando.

Aca las ventaja es que igual derivado de esa desventaja cada quien tiene una funcion por hacer en su microservicio.

## Duda
Aqui inicia una pregunta, contexto: Hace poco las paginas de cine tuvieron una caida masiva debido a que inicio la preventa de Spiderman, yo supongo que la estructura de este tipo de cines debe ser de microservicios, y que al momento de que esta tuvo su caida solo se cayo el microservicio de la interfaz para el usuario, aun sabiendo esto igualmente la caida fue de un aproximado de 12 horas, y aun asi presentaba fallas, la pregunta es: ¿Que hubiera pasado, cuanto tiempo mas hubieran tardado en levantar la pagina si fuera escrita en monolito?

## Opinion
Luego de la inmensa lectura y de quedarme ciego por la pagina en blanco considero que la mejor arquitectura es la de microservicios, esto pensando a largo plazo, pero para evitar costes de tener que transferir la arquitectura en un momento en el que la de monolito ya no pueda mas, yo implementaria esta desde un inicio, se de la desventaja de las personas que deben trabajar en la de microservicios, pero al ser una aplicacion pequeña incial no creo que se requiera de monitoreo intensivo en cada una de los microservicios, ya en un futuro si la pagina crece entonces ahi si, pero si crece significa que se cuenta ya con mas presupuesto.

## Preguntas a cambiar
No cambiaria ninguna, pero si cambiaria mi forma de pensar en cual es mejor de las dos.

