FROM python:3.8-slim-buster

ENV VIRTUAL_ENV=/env \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 

COPY requirements.txt /


RUN apt update && apt install -y \
    build-essential \
    python3-dev \
    python3-pip \
    python3-venv \
    python3-pip \
    python3-dev \
    libpq-dev \
    apt-transport-https \
    postgresql \
    postgresql-contrib \
    openjdk-11-jdk \
    openjdk-11-jre \
    curl

# create user and db
RUN service postgresql start && \
    su - postgres -c "psql -c \"CREATE USER myuser WITH PASSWORD 'mypass';\"" && \
    su - postgres -c "psql -c \"CREATE DATABASE mydb WITH OWNER myuser;\"" && \
    su - postgres -c "psql -c \"ALTER USER myuser CREATEDB;\"" && \
    service postgresql stop

RUN curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add -
RUN echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-7.x.list
RUN apt update && apt install elasticsearch -y
RUN service elasticsearch start

# RUN pip install psycopg2-binary
RUN pip install -r requirements.txt

WORKDIR /usr/src/app

COPY ./ ./

RUN python manage.py generate_test_data 1000

EXPOSE 8000
CMD gunicorn src.wsgi:application --bind 0.0.0.0:8000