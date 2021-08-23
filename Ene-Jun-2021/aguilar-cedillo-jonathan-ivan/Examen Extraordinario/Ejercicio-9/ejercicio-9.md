# Construir la imagen 
docker build --tag ejercicio-9 .

# correr la imagen 
docker run --name ejercicio-9 -p 80:80 -d ejercicio-9