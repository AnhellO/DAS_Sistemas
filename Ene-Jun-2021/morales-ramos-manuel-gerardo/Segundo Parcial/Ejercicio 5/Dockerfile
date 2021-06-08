# Extendiendo de Python 3
FROM python:3

# Estableciendo /app como directorio de trabajo
WORKDIR /usr/src/app

# Copiando todos los demás archivos en el contenedor
COPY . /usr/src/app

# Instalando los requerimientos
RUN pip install --no-cache-dir -r requirements.txt

# Estableciendo el volumen
VOLUME [ "redis_volume" ]

# Ejecutando el script
CMD [ "python", "./script.py" ]