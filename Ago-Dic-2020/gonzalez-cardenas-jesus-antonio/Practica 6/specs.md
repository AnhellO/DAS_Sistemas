# Práctica 6 de DAS

Estas son las instrucciones para correr el contenedor de docker:

1. Bajar esta carpeta del repo y entrar a ella
2. Correr el comando en la terminal: 
    
    ``` docker build -t mongo_app .  ```
3. Despues de que se haya terminado de construir la imagen, para correrla en un contenedor, usar:

    ``` docker run -d -p 27017:27017 --name m1 mongo_app ```

4. Hay que entrar al contenedor y correr el script:

    ``` docker exec -it m1 /bin/bash ```
    
    ``` ./py_scripts.sh ```

5. Salimos de nuestro contenedor    

5. Para usar phpMoadmin con la base de datos corra el siguiente comando:

    ``` docker run --name moadmmin -d --link m1:db -p 8080:80 thinkcube/phpmoadmin  ```
