FROM python:3

# Copy the current directory contents into the container at /app
COPY . /usr/src/app

# Set the working directory to /usr/src/app
WORKDIR /usr/src/app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Add the wait script to the image
# ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
# RUN chmod +x /wait

# run the command
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]