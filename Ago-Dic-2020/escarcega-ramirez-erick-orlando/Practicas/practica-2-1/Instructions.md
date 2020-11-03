# STEPS TO RUN THE DOCKER CONTAINER | Practica: 2-1 | Erick O. Escárcega Rmz.

## 1 - Open the terminal and type the following comands:
- cd DAS_Sistemas\Ago-Dic-2020\escarcega-ramirez-erick-orlando\Practicas\practica-6
- docker build .
- docker run -d -p 27017:27017 --name m1 mongo
- python populate.py
- python find.py
- docker run --name moadmin -d --link m1:db -p 8080:80 thinkcube/phpmoadmin

## 2 - Go to your web browser and type the following:
- localhost:8080 (You can also Open DockerDesktop and click on **OPEN IN BROWSER**)
- click on the dropbox and change it to "*4. mi-db (0mb)*"
- click on *Change database*