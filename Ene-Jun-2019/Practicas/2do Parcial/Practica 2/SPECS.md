# Práctica 2 - `argparse` y `slugify`

## Objetivo

* Aprender a utilizar más la habilidad de scripting de `Python` a través de la creación de una sencilla aplicación basada en línea de comandos
* Aprender a manejar más las librerías externas/de-terceros de `Python`

## Preparaciones

* Si no tienes `pip`, instálalo en tu máquina local
* Una vez que tengas `pip` funcionando, instala el siguiente paquete: https://github.com/un33k/python-slugify

## Especificaciones

Crear una sencilla aplicación que funcione desde línea de comandos utilizando `argparse`. La aplicación deberá de tomar un nombre completo y hacer lo siguiente con él, basado en las opciones proporcionadas mediante la línea de comandos:
* Convertirlo a un slug válido
  * Ejemplo: `Luisito Pérez` a `luisito-perez`
* Convertirlo a mayúsculas
  * Ejemplo: `Luisito Pérez` a `LUISITO PÉREZ`
* Convertirlo a minúsculas
  * Ejemplo: `Luisito Pérez` a `luisito pérez`
* Convertirlo a su valor total en ASCII (es decir, la suma del valor de cada caractér del string en ASCII)
  * Ejemplo: `Luisito Pérez` a `1427`
* Invertir el nombre de la persona
  * Ejemplo: `Luisito Pérez` a `zeréP otisiuL`

El comando podrá recibir los siguientes parámetros:
* `nombre`: igual al primer y/o segundo nombre de la persona (Obligatorio)
* `apellido`: igual al primer y/o segundo apellido de la persona (Obligatorio)
* `--slug`: si se quiere convertir el nombre a slug (Opcional)
* `--mayus`: si se quiere convertir el nombre a mayúsculas (Opcional)
* `--minus`: si se quiere convertir el nombre a minúsculas (Opcional)
* `--ascii`: si se quiere obtener el valor ASCII del nombre (Opcional)
* `--reverse`: si se quiere invertir el nombre de la persona (Opcional)

Por cada argumento opcional, deberá de imprimirse el resultado en una línea por separado, con un formato similar al siguiente:

* Corriendo el comando: `python practica-2.py Luisito Pérez --slug --reverse`
* Resultado de la salida:
```
El nombre proporcionado es *Luisito Pérez*:
- Su valor en slug es: luisito-perez
- Su valor invertido es: zeréP otisiuL
```

## Requisitos
* Enviar la práctica siguiendo los lineamientos del repositorio: [https://github.com/AnhellO/DAS_Sistemas/blob/development/README.md](https://github.com/AnhellO/DAS_Sistemas/blob/development/README.md)

## Deadline

* `2019-05-02`