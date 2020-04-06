## Link
https://hub.docker.com/repository/docker/emiliobg1997/pokepy
## Instructions
   1. DOWNLOADING THE IMAGE:
      
      Downloading the image is really simple.
      Open a terminal and enter the following line:
      - Linux:
         > $ sudo docker pull emiliobg1997/pokepy:1.0
         
      - Windows: (may or may not need elevated privileges):
         > docker pull emiliobg1997/pokepy:1.0
      

   2. RUNNING THE IMAGE
       - Verify the download:
           First, let's see if the image was downloader correctly. 
           Open a terminal and enter the following line:
           - Linux:
               > $ sudo docker images
               
           - Windows (again, may or may not need elevated privileges):
               > docker images
               
       - Run the image
         Let's create and run container with the image.
           Open a terminal and enter the following line:
           - Linux:
               > $ sudo docker run -it -p 5000:5000 emiliobg1997/pokepy:1.0
               
           - Windows (again, may or may not need elevated privileges):
               > docker run -it -p 5000:5000 emiliobg1997/pokepy:1.0

   3. ENJOY:
       - Open your web browser and access the url http://0.0.0.0:5000 to get a random pokémon.
       - You can also choose a pokemon if you access: http://0.0.0.0:5000/POKEMON 
         change POKEMON to the name the monster of your choice (eg: http://0.0.0.0:5000/charizard)
       - Feel free to fork and add/delete features to the app. just make sure to give credits
         to the original developer __anhellojz__

