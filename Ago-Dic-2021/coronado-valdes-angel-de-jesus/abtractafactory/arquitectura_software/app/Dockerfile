#parte de python3
FROM python:3

#comando de docker crear carpeta en la ruta 
WORKDIR /usr/src/app

#copia los archivos a la ruta del contenedor
COPY . /usr/src/app/

#instala las dependencia que requiere el programa
RUN pip install --no-cache-dir -r requirements.txt

#ejecuta python y el archivo app.py
CMD [ "python3","app.py" ]