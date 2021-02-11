cd pymongoDockerfile
sudo docker build -t mongopractica1 .
sudo docker run -d -p 27017:27017 --name mongopractica mongopractica1
cd ..
cd phpMoAdminDockerfile
sudo docker build -t phpmoadminpractica1 .
docker run --name moadmin -d --link mongopractica:db -p 8080:80 phpmoadminpractica1
cd ..
sudo docker exec -it mongopractica python3 populate.py