# AOEII - API OF EMPIRES II

## How to run
In order to run this service you have two options
1. Use the docker image
2. Run the Python Scripts directly

## 1. Running the Docker Image

There's an already built image on dockerhub! You can pull it using the following command:

```sudo docker pull emiliobg1997/aoeii:1.0```
    
After that, you can run it by using:

```sudo docker run -it -p 5000:5000 emiliobg1997:/aoeii:1.0```

Now, simply open your web browser and access http://0.0.0.0:5000, the image should be running now

You can also build the image yourself directly from the github repo:
1. Clone the repo    
    
    ```git clone https://github.com/EmilioBG1997/DAS_Sistemas.git```
    
2. Move to the folder containing the image
    
    ```cd DAS_Sistemas/Ene-Jun-2020/barrera-gonzalez-emilio/2do Parcial/Practica 2/```
    
3. Build the image:

    ```sudo docker build --tag emiliobg1997/aoeii:1.0 "./aoeii"```
    
4. Run it
   
   ```sudo docker run -it -p 5000:5000 emiliobg1997:/aoeii:1.0```
   
5. Again, open your web browser and access http://0.0.0.0:5000, the image you just built should be running now

## 2. Running the Scripts:

Please note that you need the following modules for python as well as python 3.x in order to run it this way:

- flask v.1.1.2
- requests v.2.22.0
- peewee v.3.13.3

you can install them with pip:

```$pip install $PACKAGE```

Where $PACKAGE is the module you want to install.

If you already installed the modules then you can procceed to clone the repo:

```$git clone https://github.com/EmilioBG1997/DAS_Sistemas.git```

Then, move to the root folder of the app

```$cd DAS_Sistemas/Ene-Jun-2020/barrera-gonzalez-emilio/2do Parcial/Practica 2/aoeii```

Now, you will see there's a file called "AgeOfEmpiresII.db" that's our database which is already built, if you want to rebuild it yourself you should be able to do so deleting the file and then running the following command:

```$python3 dbcreation.py```

you'll be able to see what's going on if you take a look at the terminal

After that, just run the app:

```$python3 app.py```

then open your web browser and access http://0.0.0.0:5000
you'll should be able to see the index page.
