# Composit

Es un patrón de diseño estructural que te permite componer objetos en estructuras de árbol y trabajar con esas estructuras como si fueran objetos individuales.  
Tambien nos permite construir objetos complejos partiendo de otros más sencillos utilizando una estrategia de composición recursiva.  
Podemos equiparar este patrón a un arbol y sus ramas. Cada objeto simple (Rama) puede relacionarse con otros formando una estructura más compleja (Arbol).  

Basicamente este patron de diseño nos permite crear  y manipular estructuras de objetos en forma de arbol, en la que los objetos contienen a otros,  
las estructuras de estos patrones se componen de ramas y hojas y que ambos comparten una misma Interface que define métodos que deben implementar.  

Para ver cómo funciona este patrón de diseño veamos a continuación una brebe textualizacion de su funcionamiento  
en el que gestionamos archivos y carpetas.


### ** EXPLICACIÓN: **

1. Los archivos son hojas (no contienen otros elementos) y las carpetas serían nodos ó ramas (pueden contener archivos así como otras carpetas).  

2. Las clases Archivo y Carpeta heredan de la clase abstracta Nodo, que implementa los métodos comunes y define el método mostrar() que deberán implementar. 

3. Dicho método en la clase Archivo abre el archivo para mostrar su contenido, y en la clase Carpeta muestra su contenido de forma recursiva (si contiene otras carpetas mostrará también lo que contienen).

4. Al ejecutar el programa se crea una carpeta principal y se le agregarán objetos de tipo Archivo así como otra subcarpeta que creamos posteriormente, y después mostramos su contenido.

5. A continuación eliminamos la subcarpeta y volvemos a mostrar el contenido de la principal  

