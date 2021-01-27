FROM python:3

# set a directory for the app
WORKDIR /home/daniel/PycharmProjects/DAS_CYPS/DAS_Pract3

# copy all the files to the container
COPY . /home/daniel/PycharmProjects/DAS_CYPS/DAS_Pract3

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# run the command
CMD ["python", "./app.py"]