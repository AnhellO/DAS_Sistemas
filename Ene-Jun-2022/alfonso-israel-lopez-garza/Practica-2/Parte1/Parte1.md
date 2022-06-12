# Preguntas
1. ¿Qué lenguaje de programación utiliza el equipo de Netflix?
R = Java
2.- ¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
R = Que cuando se caia la base, se caia todo en general.
3.- ¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?
R = Todos contribuian a un codigo base que se implementaba por semana o quincena. Entonces les genero un problema cuando hubo un cambio que hizo que fuera dificil diagnosticar el álbum.
4.- ¿A qué autor cita el ponente cuando da el concepto de un microservicio?
R = Martin fowler
5.- ¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
R = Separacion de intereses, Escalabilidad, Virtualizacion y elasticidad.
6.- ¿Qué analogía se utiliza para comparar los microservicios con la vida real?
R = Como los órganos de un sistema nervioso.
7.- Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
R = a/b: Que es para pruebas de llamado, Suscripcion: Obtiene la informacion de los clientes, sistema de recomendacion para crear las listas de peliculas que muestran, Servicios de plataforma: que realiza las capacidades mas fundamentales de enrutamiento.
8.- ¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
R = Dependencia, escala, varianza y cambio
9.- ¿Qué es el falló en cascada?
R = Un servicio falla con defensas inadecuadas y ese servicio que falla puede caer en cascada y eliminar todo su servicio para los miembros. 
10.- ¿Qué es Hystrix?
R = El historial, se creo para lidiar con el problema de cascada que se encarga de manejar los tiempos, en caso que no se pueda conectar al servicio, permite al usuario seguir usando el producto.
11.- ¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?
R = con inyectar un virus para que desarrolle anticuerpos y defenderse.
12.- ¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
R = Con microservicios criticos, que son lo necesario para que funcione la funcionalidad basica.
13.- ¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
R = Estrategia multiregional con estreptococos cono tres regiones de AWS.
14.- ¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
R = Escenario de servicio sin estado, escenario de servicio con estado, servicio hibrido.
15.- ¿De qué manera se describe un "stateless service" en el video?
R = not a cache or a database, frequently accessed metadata, no tendra afinidad de instancia, la perdida de un nodo es esencialmente un no evento.
16.- ¿Qué es Chaos Monkey?
R = Herramienta de dolor de caos.
17.- ¿Qué es un microservicio híbrido?
R =  es una combinacion de los servicios con estados y sin estado. 
18.- ¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
R = fueron varias, dejar de martillar el mismo conjunto de sistemas para el cache de solicitudes. un token.
19- ¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
R = docker, node.js
20.- ¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
R = poductivity tooling, insight y triage capabilities, base image fragmentation, node management, library/ platform duplication, leraning curve.
21.- ¿Qué es Spinnaker?
R = Es una plataforma de entrega, es una plataforma global de administracion de la nube.
22.- ¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
R = blade runner, las capas de NCCP se descompusieron y se integraron directamente en la capar proxy, puerta enlace de API, y las piezas apropiedas se insertaron en nuevos microservicios.
23.- ¿Qué es "chaos engineering" o "ingeniería del caos"?
R = Es el enfoque para probar y construir un sistema que soporta fallas o condiciones inesperadas.