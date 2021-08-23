docker build -t georgehdz94/static_flask .  

docker push georgehdz94/static_flask 

docker run -p 5000:8000 --name=flask georgehdz94/static_flask 