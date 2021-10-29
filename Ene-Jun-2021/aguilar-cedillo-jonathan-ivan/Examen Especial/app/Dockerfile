FROM python:3
EXPOSE 7777
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./scraper.py"]