docker build -t 15604715/static_flask 
docker run -d -p 5000:8000 --name practica3 15604715/static_flask
docker login 
docker push 15604715/static_flask 
docker ps -a

Link Dockerhub: https://hub.docker.com/r/15604715/static_flask