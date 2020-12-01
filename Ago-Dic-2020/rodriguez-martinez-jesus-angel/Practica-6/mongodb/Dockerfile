# Image
FROM mongo:latest

# Dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get -y install python3.7-dev
RUN pip3 install pymongo
# Directories
WORKDIR /home/DAS_Sistemas/Ago-Dic-2020/rodriguez-martinez-jesus-angel/
# Files
ADD populate.py .
ADD find.py .
# Port
EXPOSE 27017
