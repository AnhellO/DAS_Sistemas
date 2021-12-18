#utiliza la imagen de python version 3.8
FROM python:3.8
# copia el directorio
COPY . /usr/src 
# selecciona el directorio en el que se va a trabajar 
WORKDIR /usr/src
# corre el comando git clone para clonar el directorio
RUN git clone https://github.com/joaoventura/flask-static-site.git
# corre los requerimientos 
RUN pip install flask flask_flatpages frozen_flask pygments
# expone el puerto del contenedor
EXPOSE 5000
# ejecuta el script
CMD [ "python", "./site.py" ]


