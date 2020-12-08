FROM python:3

# Copy the current directory contents into the container at /app
COPY . /home/salguer/breaking
# Set the working directory to /usr/src/app
WORKDIR /home/salguer/breaking

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 5000

# run the command
CMD [ "python", "./countriesapp.py" ]
