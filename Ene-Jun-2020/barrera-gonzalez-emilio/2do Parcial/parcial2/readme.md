# PARCIAL 2
Funciona!!!!

## Nombre
Emilio Barrera González

## Matricula
13001112


## Como Correr
Despues de unas horas de troubleshooting, troubleshooting y un poco más de troubleshooting, por fin pude llegar a la conclusión de que tenía que reiniciar el examen :'P

pero suficiente de tragedias

### Paso 1
Clonar el repositorio (si ya lo clonaste, pullea cambios)

### Paso 2
Una vez clonado el repo, muevete a la carpeta
DAS_Sistemas>Ene-Jun-2020>barrera-gonzalez-emilio>"2do Parcial">parcial2

### Paso 3
Creo que es gracioso que despues de tanto batallar para programarlo, sea tan facil correrlo XD
abre una terminal en la carpeta y ejecuta el siguiente codigo

Linux:
```$ sudo docker-compose up```

    nota: si no tenías instaladas las imagenes de mysql o phpmyadmin, 
    es muy probable que durante la 1era ejecucion te encuentres con un error que reza: 
    <<ERR 111 - Connection Refused>>
    la solucion es sencilla, solo hay que detener la ejecucion del contenedor (¡SIN FORZARLA!)
    despues, simplemente volver a correr el codigo mencionado anteriormente

Windows:
``` C:> docker-compose up ```

    nota: Probablemente windows te pida que lo hagas con permiso de admin
    para eso, presiona la tecla windows, escribe "CMD" sin comillas, y en el icono de la consola
    haz click derecho y luego selecciona "ejecutar como administrador.

### Paso 4
entra a http://0.0.0.0:5000 y disfruta de mi trabajo:P


#### Lista de URLS en la App
Harcodeadas solo se encuentra el endpoint de la api
- https://www.breakingbadapi.com/api/characters

sin embargo, la api, para cada personaje incluye una url para sus imagenes

