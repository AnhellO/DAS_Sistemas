FROM python:3

# Copy the current directory contents into the container at /app
COPY . /usr/src/app

# Set the working directory to /usr/src/app
WORKDIR /usr/src/app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# run the command
CMD [ "python", "./scraper.py" ]