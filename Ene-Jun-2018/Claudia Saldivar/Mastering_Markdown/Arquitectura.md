#Arquitectura monolítica

Es un modelo en el cual el sistema operativo y todos los servicios fundamentales residen en
un monitor monolítico que se accede a través de un mecanismo de llamada al **núcleo**.

###Funcionamiento

Para corregir algunos de los problemas de la configuración "ejecutivo en tiempo real", algunos vendedores de RTOS han adoptado una arquitectura monolítica.
En este modelo, el sistema operativo y todos los servicios fundamentales, tales como **file system**, residen en un monitor monolítico que se accede a través
de un mecanismo de llamada al núcleo.
Las llamadas al núcleo hacen la transición del modo aplicación (o usuario) al modo supervisor. Se proporciona protección de modo que sólo se puede acceder a
recursos del núcleo en modo supervisor; las aplicaciones se ponen en ejecución generalmente como procesos que tienen espacios de direccionamiento separados con
protección entre ellos.

##Ventajas

Con un monitor monolítico, los servicios fundamentales que requieran acceso a los recursos del núcleo deben residir en este. De esta forma, la complejidad del núcleo aumenta, aumentando la probabilidad de encontrar errores. Asimismo, el acceso a entrada-salida, al vector de interrupciones y a la memoria física se puede restringir al núcleo por razones de la seguridad, lo que significa que la mayoría de los drivers de dispositivos deben residir en el núcleo.

Cruzar la barrera kernel/aplicación es con frecuencia costoso, así en algunos casos, los drivers que de otro modo se podrían poner en ejecución modo usuario, tal como drivers de gráficos, se incorporan en el núcleo por razones de performance.

Mientras que las aplicaciones no pueden corromper el núcleo, cualesquiera de estos drivers de dispositivos pueden – aumentando la probabilidad de que ocurran errores fatales

##Desventajas

Aunque, después de lo dicho hasta ahora parezca difícil de creer, una infraestructura cliente/servidor también tiene sus inconvenientes:

-Coste elevado. Tanto la instalación como el mantenimiento son más elevados debido al perfil muy técnico del lado servidor.
-Dependencia del servidor. Toda la red está construida al rededor del servidor y si éste deja de funcionar o lo hace con un rendimiento inadecuado, afectará a toda la infraestructura.

Afortunadamente, este último inconveniente está superado, al menos en parte, gracias a sistemas como los servidores redundantes, la tolerancia a fallos y los sistemas de almacenamiento en modo RAID.

##Tipos de software al cual aplica este Estilo Arquitectonico

    -Firmware
    -Software base de Sistema Operativo(Servicios, demonios, Kernell)
    -Pequeñas utilidades especificas(Desde virus, keyloggers, sniffers)

##Diagrama

![Arquitectura monolitica](http://2.bp.blogspot.com/-vdHKIg5Hchg/T4JbVor_QBI/AAAAAAAAAFQ/soMxXgICrJc/s1600/monolitica.png)

###Arquitectura de micro servicios

La Arquitectura de micro- servicios, conocido por las siglas **MSA** (del inglés Micro Services Architecture) es una aproximación para el desarrollo de software que consiste en construir una aplicación como un conjunto de pequeños servicios, los cuales se ejecutan en su propio proceso y se comunican con mecanismos ligeros (normalmente una API de recursos HTTP). Cada servicio se encarga de implementar una funcionalidad completa del negocio. Cada servicio es desplegado de forma independiente y puede estar programado en distintos lenguajes y usar diferentes tecnologías de almacenamiento de datos.

##Ventajas

-Servicios pequeños e independientes (principio de responsabilidad única).
-Unidades de despliegue pequeñas.
-Reducción de tiempo de desarrollo.
-Agilidad en hot fixes (consecuencia de las anteriores).
-Multitecnología.
-Fácil escalado horizontal.

##Desventajas

-Alto consumo de memoria
-Necesidad de tiempo para poder fragmentar distintos microservicios
-Complejidad de gestión de un gran número de servicios
-Necesidad de desarrolladores para la solución de problemas como latencia en la red o balanceo de cargas
-Pruebas o testeos complicados al despliegue distribuido

##Diagrama
#Arquitectura monolítica

Es un modelo en el cual el sistema operativo y todos los servicios fundamentales residen en
un monitor monolítico que se accede a través de un mecanismo de llamada al **núcleo**.

###Funcionamiento

Para corregir algunos de los problemas de la configuración "ejecutivo en tiempo real", algunos vendedores de RTOS han adoptado una arquitectura monolítica.
En este modelo, el sistema operativo y todos los servicios fundamentales, tales como **file system**, residen en un monitor monolítico que se accede a través
de un mecanismo de llamada al núcleo.
Las llamadas al núcleo hacen la transición del modo aplicación (o usuario) al modo supervisor. Se proporciona protección de modo que sólo se puede acceder a
recursos del núcleo en modo supervisor; las aplicaciones se ponen en ejecución generalmente como procesos que tienen espacios de direccionamiento separados con
protección entre ellos.

##Ventajas

Con un monitor monolítico, los servicios fundamentales que requieran acceso a los recursos del núcleo deben residir en este. De esta forma, la complejidad del núcleo aumenta, aumentando la probabilidad de encontrar errores. Asimismo, el acceso a entrada-salida, al vector de interrupciones y a la memoria física se puede restringir al núcleo por razones de la seguridad, lo que significa que la mayoría de los drivers de dispositivos deben residir en el núcleo.

Cruzar la barrera kernel/aplicación es con frecuencia costoso, así en algunos casos, los drivers que de otro modo se podrían poner en ejecución modo usuario, tal como drivers de gráficos, se incorporan en el núcleo por razones de performance.

Mientras que las aplicaciones no pueden corromper el núcleo, cualesquiera de estos drivers de dispositivos pueden – aumentando la probabilidad de que ocurran errores fatales

##Desventajas

Aunque, después de lo dicho hasta ahora parezca difícil de creer, una infraestructura cliente/servidor también tiene sus inconvenientes:

-Coste elevado. Tanto la instalación como el mantenimiento son más elevados debido al perfil muy técnico del lado servidor.
-Dependencia del servidor. Toda la red está construida al rededor del servidor y si éste deja de funcionar o lo hace con un rendimiento inadecuado, afectará a toda la infraestructura.

Afortunadamente, este último inconveniente está superado, al menos en parte, gracias a sistemas como los servidores redundantes, la tolerancia a fallos y los sistemas de almacenamiento en modo RAID.

##Tipos de software al cual aplica este Estilo Arquitectonico

    -Firmware
    -Software base de Sistema Operativo(Servicios, demonios, Kernell)
    -Pequeñas utilidades especificas(Desde virus, keyloggers, sniffers)

##Diagrama

Hyperlink: [arquitectura_microservicios][]
[Arquitectura_microservicios]:https://www.mindmeister.com/es/952818710/arquitecturas-orientadas-a-servicios-soa
