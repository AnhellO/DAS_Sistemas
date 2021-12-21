#parte de python3
FROM python:3
#crear carpeta 
WORKDIR /usr/src/app
#copia los archivos a la ruta
COPY . /usr/src/app/
#instala las dependencia
RUN pip install --no-cache-dir -r requirements.txt
#ejecuta python
CMD [ "python3","app.py" ]