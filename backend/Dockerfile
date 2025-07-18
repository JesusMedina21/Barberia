FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requiriments.txt
RUN pip install -r requiriments.txt
COPY . /app/

CMD python manage.py runserver 0.0.0.0:8000
