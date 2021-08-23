# CREAMOS LA IMAGEN DE DOCKER CON LA VERSIÓN DE PYTHON
FROM python:3.9.4

# DIRECTORIO DE TRABAJO
WORKDIR /usr/src

# CLONAMOS EL REPOSITORIO
RUN git clone https://github.com/joaoventura/flask-static-site.git

# SCRIPTS DE PYTHON PARA LA EJECUCIÓN DE LA APLICACIÓN
COPY . /usr/src

# INSTALAR DEPENDENCIAS
RUN pip install --no-cache-dir -r requirements.txt 

# ASIGNACIÓN DE PUESRTO
EXPOSE 8000

# MOSTRAR LOS ARCHIVOS
RUN ls -la

# SCRIPT
CMD ["python3", "flask-static-site/site.py"]