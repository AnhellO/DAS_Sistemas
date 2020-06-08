# Using Docker and Compose to Simplify Integration Testing
Not one developer feels good about writing scripts to clean up their test residue. Docker and containerization clean this mess up for us and also spin it up in record time. The consistency, convenience, and certainty provided makes integration testing a doddle, proving Docker to be invaluable. not just as an infraestructure solution, but as part of the developers toolkit. 
Docker also allows us to easily spin up and destroy all of out development and testing dependencies without worrying about trivial matters, such as having to install several database servers on out machine or writing cleanup scrips for development databases, to clear up any test residue 

## Integration Testing
1. Tests out application against it's required dependencies
2. Databases
3. Transport mechanisms 
4. How we interact with out external dependencies will determine how much value we get out of then

## Using Docker to Run Tests (Why?)
1. Sanitized environment
2. Easier to hook up to our Containerized dependencies
3. If our service is going to run in a container then we should test it in a container 

## Running our Dependencies in a Container 
Two common dependencies
- Mongo Database
- Google Pub/Sub Emulator
Can be applied to any dependency 
- SQL Database
- Redis

## Using Docker compose to put it altogether
Create docker-compose.yaml

We're going to run our mongo database and the Google Pub/Sub emulator
Build our application and run the Test using the containerized dependencies 

## Summary 
- Docker as part of the developers Toolkit
- Containerized testing dependencies 
- Docker Compose does all the hard work for us 
- How we interact with out dependencies determines how much value we get out of them. 


### Acquired knowledge
I learned how to do integration tests using containers, I found it extremely useful since they are usually a bit complex when it comes to executing, I did some tests with a project of my quality subject.