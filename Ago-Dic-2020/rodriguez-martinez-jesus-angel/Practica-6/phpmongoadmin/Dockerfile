# Image
FROM alpine:3.4

# Dependencies

RUN apk update

RUN apk add --no-cache php5-cli php5-ctype php5-xml php5-gd php5-zlib php5-bz2 php5-zip php5-openssl php5-curl php5-opcache php5-json curl ca-certificates

# Files
COPY sgerrand.rsa.pub /etc/apk/keys/

COPY php5-mongo-1.6.14-r0.apk /tmp/

COPY index.php /www/

COPY run.sh /run.sh

RUN update-ca-certificates

RUN apk add /tmp/php5-mongo-1.6.14-r0.apk

# Ports


EXPOSE 80

ENTRYPOINT ["/run.sh"]
