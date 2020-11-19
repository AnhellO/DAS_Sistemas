FROM postgres:12

ENV POSTGRES_DB random_cats
ENV POSTGRES_USER the_cat
ENV POSTGRES_PASSWORD secretcat123

COPY init.sql /docker-entrypoint-initdb.d/