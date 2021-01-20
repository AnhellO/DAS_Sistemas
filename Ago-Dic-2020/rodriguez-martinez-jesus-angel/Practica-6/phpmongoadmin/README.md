# phpMoAdmin Docker image

Run phpMoAdmin with Alpine Linux


Following examples will bring you phpMoAdmin on http://localhost:8080

## Usage with linked server

You can link this image to a running mongodb container.

```
docker run --name moadmin -d --link mongodb_server:db -p 8080:80 thinkcube/phpmoadmin
```
