docker build -t robertohr/static_flask .
docker run -d -p 5000:8000 --name flask robertohr/static_flask
docker push robertohr/static_flask

Link Dockerhub: https://hub.docker.com/u/robertohr 
