### Comentarios

Fue una practica muy interesante, pude sentir que hice las cosas mejor si me baso en la primera.
Fue muy divertido, algo tricky la parte de esperar a que un container levante su servicio para que la librería
de otro contenedor que la necesite no falle (esa parte aún siento que puede mejorar, vi un poco de docker wait pero esperaré para probarlo con más calma después).
En fin, las ventajas son infinitas, las desventajas aparecerán cuando haga mal las cosas :)
Sólo hace falta correr con docker-compose up --build para que funcione. No tomé capturas, me encargué
de que funcionaran las cosas sin necesidad de ir capturando cada detalle y sin que se tenga
que entrar al exec -it bash de cada servicio aunque se puede usar si se quiere comprobar manualmente las cosas :) y limité los registros a 5 (puede cambiarse el parámetro a 100, fue más por motivos de pruebas).

En la terminal saldrán mensajes como:
mongodb    | WARNING: no logs are available with the 'none' log driver
flask_1    | Iniciando servidor de Flask...
flask_1    |  * Serving Flask app "app" (lazy loading)
flask_1    |  * Environment: production
flask_1    |    WARNING: This is a development server. Do not use it in a production deployment.
flask_1    |    Use a production WSGI server instead.
flask_1    |  * Debug mode: on
flask_1    |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
flask_1    |  * Restarting with stat
flask_1    |  * Debugger is active!
flask_1    |  * Debugger PIN: 167-227-905
python     | Insertando registros en la base de datos...
python     | Generando una nueva conexión a la base de datos...
python     | Conexión realizada con éxito en:
python     | mongodb://root:1234@mongodb:27018
python     | Se han registrado 100 personas en la base de datos...

Para que pueda dar seguimiento sin necesidad de que entre al exec -it bash. Le metería más cosas pero el tiempo
nada más no me ayuda ultimamente so, sorry por no hacer otras tareas a veces, trabajar, estudiar, programar, tener pareja x) es una vida increíble y me encanta pero últimamente el tiempo escasea, saludos maestro, nos vemos en el trabajo!