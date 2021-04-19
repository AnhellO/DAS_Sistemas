# Imagen
FROM python:3.8 


# crea el workdir del contenedor
WORKDIR /home/DAS_Sistemas/Ene-Jun-2021/monjaras-granados-alicia-montserrat/Practica2_segundoParcial

#Agrega los scripts de python, para que la aplicación se ejecute 
COPY . /home/DAS_Sistemas/Ene-Jun-2021/monjaras-granados-alicia-montserrat/Practica2_segundoParcial

# Instalar Dependencias
RUN pip install --no-cache-dir -r requirements.txt 



# Corre el comando
CMD ["python", "./app.py"]

