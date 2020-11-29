FROM python:3

COPY . .

RUN pip install Flask

RUN pip install -r requirements.txt

#ENTRYPOINT ["python", "view.py"]

#CMD ["sleep", "30"]

CMD ["python", "view.py"]
#ENTRYPOINT flask run --host 0.0.0.0 