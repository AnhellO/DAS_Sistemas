### Hands-on Helm


En esta sesión Jessica Deen comienza diciéndonos en primer lugar lo que es Helm.
Helm es el administrador de paquetes de facto para Kubernetes, es la mejor forma de encontrar, compartir
y usar software que está específicamente construido para Kubernetes y que de hecho ayuda a gestionar
nuestra complejidad, nos ayuda a hacer actualizaciones fáciles, podemos simplemente compartir nuestros
gráficos e inluso se puede aprovechar el comando de reversión retenida (held rollback command) para
poder volver a versiones anteriores.

Kubernetes en realidad salió en mayo del 2014 y helm era el niño, por así decirlo de un proyecto 
de hackathon en una compañía llamada Deis.
Microsoft adquirió Deis hace unos años pero al parecer el hackathon tuvo lugar en octubre del 2015
por lo que debemos de tener en cuenta que es solo un año y medio más joven que Kubernetes.

  * Versión 3 de Helm:
	Esta versión se basa en los comentarios (feedback) de la comunidad, en las mejores prácticas,
	que escuchan de la comunidad. Los diferentes casos de uso, casos de uso basados en la producción,
	Helm 3 fue hecho más simple, más seguro y realmente se enfocaron en la producción y lo que 
	la comunidad se encontraba haciendo en producción.
	También se eligió hacer a Helm más nativo a Kubernetes, eso se sumaría a la dramática simplificación.
	En primer lugar hereda los controles de seguridad directamente desde kubeconfig para que no
	tengas que salir y configurar una cuenta de servicio.

  * Algunos cambios realizados: 
	- helm delete ------> helm uninstall
	- helm inspect -----> helm show
	- helm fetch --------> helm pull
	- helm search -----> helm search repo


Lo aprendido en esta sesión fue:

    - Un poco de información que fue compartida acerca de Kubernetes, además de:

	* Algunos comandos básicos de Helm 2 y Helm3, tales cómo:
		- helm version  	-------> 	h3 version
		- helm ls 		------->	h3 ls
	* Comandos de instalación y desinstalación:
		- h3 repo add stable http://storage.googleapis.com/kubernetes-charts  
		- h3 repo ls
		- h3 upgrade --install nginx-ingress stable/nginx-ingress (para instalar un gráfico NGINX)
		- h3 uninstall nginx-ingress
