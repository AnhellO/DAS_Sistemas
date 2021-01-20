FROM python:3-onbuild
LABEL "Correo:"=d.rdz.mtz314@gmail.com

WORKDIR /home/DAS_Sistemas/Ago-Dic-2020/drdz/Practica7/ContenedorB

COPY ./requirements.txt /requirements.txt
COPY fetch.py .

CMD ["python3", "fetch.py"]