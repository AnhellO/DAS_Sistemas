# Parte 2
  * ¿Qué lenguaje de programación utiliza el equipo de Netflix?
        Java Web

  * ¿Qué sucedía con la base de datos de Oracle del monolito de Netflix?
        La base de datos también era monolítica, era una pieza de hadware que ejecutaba una gran base de datos

  * ¿Cuál fue una de las principales desventajas que el equipo de Netflix tuvo con la arquitectura monolítica?

  * ¿A qué autor cita el ponente cuando da el concepto de un microservicio?
        Martin Fowler

  * ¿Cuáles son las 3 principales ventajas que el ponente cita sobre los microservicios?
        Separación de intereses
        Escalabilidad de coordinación
        Virtualización y elasticidad

  * ¿Qué analogía se utiliza para comparar los microservicios con la vida real?
        Un sistema de órganos, cada órgano tiene un propósito  y cuando estos se unen forman un organismos

  * Describe al menos 3 diferentes tipos de servicios que Netflix tenía en su arquitectura en aquel entonces
        ZUL que hace el enrutamiento dinámico
        NCCP que admitía los dispositivos anteriores más la capacidad de reproducción fundamental
        API que es la puerta de enlace que hoy es parte del núcleo de la arquitectura moderna, llamando a los demás servicios para cumplir con las solicitudes de los clientes
        
  * ¿Cuáles son las áreas primarias que se proponen para los retos y soluciones de utilizar microservicios?
        Dependencia, Escala, Varianza y Cambio

  * ¿Qué es el falló en cascada?
        Es cuando un servicio falla y esta conectado a otros servicios que comienzan a fallar y tumban todo el servicio para tus clientes

  * ¿Qué es Hystrix?
        Es la estructura para el manejo de tiempos de espera que permite que el cliente continúe usando el servicio en lugar de simplemente obtener un error

  * ¿Qué analogía utiliza el ponente para comparar las librerias de cliente con la vida real?
        Una infección parasitaria ya que al igual que un parasito puede debilitarte pasa lo mismo en las librerías, provocan fallas dentro de la aplicación y debilitar tu servicio

  * ¿De qué manera el equipo de Netflix manejo el problema de la persistencia en microservicios?
        Con el Teorema de CAP dice que la presencia de una partición de red debe elegir entre la consistencua y la disponibilidad
  * ¿Cuál fue la estrategia de Netflix después de que sufrieron la caída del 24 de Diciembre del 2012?
        Desarrollo una estrategia multirregional con tres regiones de AWS de modo que si alguna de ellas fallaba por completo, se podía enviar todo el tráfico a las otras regiones supervivientes

  * ¿Cuáles son los 3 escenarios/casos que se plantean para la parte de escalamiento?
        stateless services, Stateful services y Hybrid services

  * ¿De qué manera se describe un "_stateless service_" en el video?
        Es una base de datos que no está almacenando información, y si se pierde un nodo no es un evento

  * ¿Qué es Chaos Monkey?
        Es una herramienta para probar tu servicio y asegurarse de que pueda volver a funcionar rápidamente

  * ¿Qué es un microservicio híbrido?
        La combinación de EVCache Writes y EVCache Reads

  * ¿Cómo solucionó el equipo de Netflix el problema con el anti-patrón de carga excesiva?
        partición de carga de trabajo, almacenamiento en caché a nivel de solicitud y con el respaldo de token seguro

  * ¿Qué tecnologías nuevas integró el equipo de Netflix cuando comenzó a manejar contenedores?
        Python, Ruby, node.js y docker

  * ¿Cuáles fueron algunos de los principales costos de varianza del equipo de Netflix?
        Herramientas de productividad, capacidades insight & triage, fragmentacion de la imagen base, gestión de nodos

  * ¿Qué es Spinnaker?
        Es una plataforma automatizada que esta diseñada para integrar mejor las aplicaciones

  * ¿Cómo manejo Netflix el problema de las arquitecturas híbridas?
        Primero  vieron las soluciones , luego el equipo que tenian , y refactorizaron los servicios  para respaldar mejor su arquitectura

  * ¿Qué es "_chaos engineering_" o "_ingeniería del caos_"?
        Son pruebas definidas por Netflix para testear su sistema y testear la estabilidad, fragilidad, etc. de su sistema


