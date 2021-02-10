FROM python:3

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Set the working directory to /usr/src/app
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /app
COPY . /usr/src/app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# run the command
CMD ["python", "./appMarvel.py"]
