FROM python:3-onbuild
LABEL "Correo:"=d.rdz.mtz314@gmail.com

WORKDIR /home/DAS_Sistemas/Ago-Dic-2020/drdz/Practica7/ContenedorC

COPY ./requirements.txt /requirements.txt
COPY view.py .
COPY app.py .
COPY static/ ./static
COPY templates/ ./templates

CMD ["python3", "app.py"]