# How to Build and Run Node Apps with Docker and Dcoker Compose

Containers are an essential part of today's microservice ecosystem, as they allow developers and operators to maintain standards of reliability and reproducibility in fast-paced deployment scenarios. And while there are best practices that extend across stacks in containerized environments, there are also things that make each stack distinct, starting with the application image itself.

### Containers and Virtual Machines
1. Virtual Machine 
    These servers allow you to run multiple full systems on a single physical host. A hypervisor manages, the multiple running machines and shares hardware resources between them
2. Containers are like virtual machines, but they provide some additional advantages. They accomplish the goals of sandbox applications and provide consistent, reproducible runtime environments much more efficiently. 

## Building an Image for a Node App 
1. Build the base
**FROM node: 12-apline**

2. Install container-level dependencies
**RUN mkdir -p /home/node/app/node_modules && chown**
**-R node:node /home/node/app**
3. Set working directory & user
**USER node**
**WORKDIR /home/node/app**
4. Copy code, set permissions and install project dependencies
**COPY package*.json ./**
**COPY --chown=node:node . .**
**RUN npm install**
5. Expose ports and invoke commands
**EXPOSE 8080**
**CMD ["node", "app.js"]**

### Acquired knowledg
The best practices to build and run Node applications with database backends using Docker and Compose.