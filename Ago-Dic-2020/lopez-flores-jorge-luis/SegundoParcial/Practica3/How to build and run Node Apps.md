

			How to Build and Run Node Apps with Docker and Docker Compose

Containers are an essential part of today's microservice ecosystem, as they allow developers and operators to maintain standards of reliability
 and reproducibility in fast-paced deployment scenarios. And while there are best practices that extend across stacks in containerized environments,
 there are also things that make each stack distinct, starting with the application image itself.

Containers and Virtual Machines
Virtual Machine These servers allow you to run multiple full systems on a single physical host. A hypervisor manages, the multiple running machines and shares hardware resources between them
Containers are like virtual machines, but they provide some additional advantages. They accomplish the goals of sandbox applications and provide consistent, reproducible runtime environments much more efficiently.
Building an Image for a Node App
Build the base FROM node: 12-apline

Install container-level dependencies RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app

Set working directory & user USER node WORKDIR /home/node/app

Copy code, set permissions and install project dependencies COPY package.json ./* COPY --chown=node:node . . RUN npm install

Expose ports and invoke commands EXPOSE 8080 CMD ["node", "app.js"]

Acquired knowledg
The best practices to build and run Node applications with database backends using Docker and Compose.