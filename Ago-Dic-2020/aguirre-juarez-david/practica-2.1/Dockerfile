# A partir de la imagen de python 3
FROM python:3

# Instalo pymongo con pip
RUN pip install pymongo

# Guardo los archivos find.py y populate.py
COPY ./scripts/*.py .

# Ejecuto el script de python para llenar la base de datos
# Y luego find para mostrar la información
ENTRYPOINT python ./populate.py && python ./find.py