
## VERSIÓN DE PYTHON
FROM python:3.9.4

## DIRECTORIO
WORKDIR /app

## SCRIPTS PARA LA EJECUCIÓN 
COPY . /app

## VOLUMEN
VOLUME [ "/var/lib/docker/volumes/redis_volume/_data" ]

## INSTALAR DEPENDENCIAS
RUN pip install --no-cache-dir -r requisitos.txt

## SCRIPT
CMD ["python","./insercion.py"]