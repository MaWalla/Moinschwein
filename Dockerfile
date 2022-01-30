FROM python:3.10
ENV DJANGO_SETTINGS_MODULE=moinschwein.settings.docker
RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

RUN apt-get update && apt-get install -y gettext && python manage.py compilemessages

CMD uwsgi --ini /app/uwsgi/docker.ini