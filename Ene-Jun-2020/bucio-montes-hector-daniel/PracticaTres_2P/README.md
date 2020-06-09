* REDIS

    - Lo que me gustó de esta tecnología sin duda fue su rapidez, te 
      da al momento la información que solicitas ya que guarda todo en memoria.

        * Pros de Redis
            - Su configuración sencilla.
    
            - Su rapidez para trabajar, guarda todos los datos en RAM, 
            por lo que cuando el microprocesador le pide un dato, lo busca 
            en la RAM sin tocar el disco duro.  
    
            - Puedes elegir como quien dice un nivel de complejidad de
            tus llaves únicas con generadores sha256, sha1, md5 por ejemplo,
            ya que al checarlos cada uno da llaves de mayor o menor longitud .
      
        * Contras de Redis 
            - Hasta el momento no le encontré ninguna, pero leyendo un poco 
            se menciona que el método de persistencia RDB consume mucho I/O 
            (escritura en disco).
      
            - Y otra fue que todos los datos trabajados deben encajar en la memoria 
            en caso de no usar persistencia física.
          