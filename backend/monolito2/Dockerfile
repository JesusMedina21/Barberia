FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app/
#COMENTO EL CMD CUANDO USE EL CONSUMER.PY
CMD python manage.py runserver 0.0.0.0:8001
