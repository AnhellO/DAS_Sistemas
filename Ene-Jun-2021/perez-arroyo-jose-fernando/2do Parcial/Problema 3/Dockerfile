FROM python:3.8

# Copy the current directory contents into the container at /app
COPY . /usr/src/app

# Set the working directory to /usr/src/app
WORKDIR /usr/src/app

VOLUME [redis_volume]

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# run the command
CMD ["python", "./data.py"]