# Síntesis 4 - Conferencia "Containerize Your Game servidor for the Best Multiplayer Experience"

## ¿Para qué sirve un servidor para juegos?
Para juegos fast paced, tiempo real, multijugador, juegos donde la latencia y rendimiento son partes críticas del juego.

## ¿Qué es un servidor para juegos?
Es una simulación completa en memoria de lo que está pasando dentro de un juego siendo hosteada en alguna parte del Internet. Todos los jugadores se conectarán a ese servidor y mandarán al servidor cosas como información de movimientos , acciones del juego (moverse, recibir/dar disparos, etc.). El servidor tiene que correr una simulación completa de las físicas, acciones de jugadores, inputs, etc. y avisar a todos los jugadores conectados sobre estas, es decir ser la autoridad del juego y decir exactamente qué está sucediendo en el juego. 

## Razones para usar servidores para juegos
- Mejor conexión de los jugadores.
- Justo - Imparcialidad ante eventos player vs player en el juego.
- Control sobre los recursos del sistemas.
- Pre-requisitos para el Cross-Play.

## Retos en la administración de servidor para juegos
- Requiere huella global
    - Requerimientos de latencia significa que los servidores para juego deben ser desplegados donde sea que los jugadores estén.
- Son lentos al empezar.
    - Los servidores tienen que cargar GBs de información antes de empezar, y esto puede tardar máximo un minuto.
    - Si se tiene este problema es recomendable tener servers listos para jugar para mitigar este problema
- Datos persistentes en memoria.
    - Cuando los jugadores se conectan a un servidor hay datos persistentes, en la memoria. Esto significa que el server no puede ser apagado durante una sesión de juego.

## Beneficios de los contenedores de Docker
- Ligero, portátiles, autosuficientes.
- Predecibles, inmutables
- Flexibles
- Herramientas estándar y ecosistema amplio
- Sistemas de patrones distribuidos estándar

## ¿Cómo orquestar servidores para juegos?
Agones es un proyecto diseñado como un servidor de juegos dedicado, de código abierto, construido sobre kubernetes, con la flexibilidad que necesitas para adaptarlo a las necesidades de tu juego multijugador.

## ¿Qué es más difícil con un servidor para juegos en un contenedor?
- Migrar lógica de controlador puede ser complicado.
- Altamente configurado para un hardware específico.
- Algunos servidores de juegos solo corren en Windows.
    - Es posible usar WINE, pero no es posible asegurar que funcione.


