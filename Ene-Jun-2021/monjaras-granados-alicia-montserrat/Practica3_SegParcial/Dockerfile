# Imagen
FROM python:3

#  directorio de trabajo es desde donde se ejecuta el contenedor al iniciarse
WORKDIR /usr/src

# Clonar repositorio
RUN git clone https://github.com/joaoventura/flask-static-site.git

# Agrega los scripts de python, para que la aplicación se ejecute 
COPY . /usr/src

# Instalar Dependencias
RUN pip install --no-cache-dir -r requirements.txt 

# puerto
EXPOSE 8000

# muestra archivos
RUN ls -la

# Corre el comando
CMD ["python3", "flask-static-site/site.py"]