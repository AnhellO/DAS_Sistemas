# Descargando la imagen base Python3
FROM python:3

# Estableciendo el directorio de trabajo en /usr/src
WORKDIR /usr/src

# Copiando el archivo de texto de los requerimientos
# dentro del contenedor
COPY requirements.txt ./

# Instalando los requerimientos
RUN pip install --no-cache-dir -r requirements.txt 

# Clonando el repositorio
RUN git clone https://github.com/joaoventura/flask-static-site.git

# Exponiendo el puerto 8000 ya que es el puerto por default
#según el repositorio
EXPOSE 8000

# Ejecutando el archivo site.py dentro de la carpeta que crea git
# por default al clonar un repositorio
CMD [ "python", "./flask-static-site/site.py" ]