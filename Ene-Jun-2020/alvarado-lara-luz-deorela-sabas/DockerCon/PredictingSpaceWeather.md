# Predicting Space Weather with Docker

## What's Space Weather?
Space Weather encompasses pretty much everything that's going on in the 93 million miles between the Earth and the Sun. So that's a few different kinds of phenomena, so you have electromagnetic radiation like x-rays far from x ray flares that can impact communications and humans and space. 

## Why Docker?
### Scientific Software Issues
One of the main things is the issues of scientific software. So scientific software often has delicate, conflicting and just downright weird dependencies. Libraries you haven't really heard of. 
### Easing Deployments 
We want to go faster! If it works on Dev, it should work on Staging, and it should work on Production. Docker can guarantee this if we solve configuration and data persistence for each project. 

## New Rules
### Event Driven.
Low latency. Use asynchronous messaging for loose coupling. 
### 12factor.net practices
The new default. Especially "Store configuration in the environment" and "log to standard out" 
### New Stuff! 
NoSQL (MongoDB) for a developer driendly database. Python Flask for RESTful gets/posts. RabbitMQ for messaging. **Docker containers for everything** 

## Replacing the Old Way (Using Docker)
1. Build a service (in a Docker )
2. That service needs to understand and solve 
    - The nature of data 
    - The way other applications use the data



### Acquired knowledg
Docker can be used in any work area, as in this example we can see how they adapted a system to use containers and process the data they obtain from space. It is interesting to see how parts of the project were completely changed adapting new technologies