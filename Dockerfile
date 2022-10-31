FROM python:3.8-slim-buster

# Exit immediately if a command exits with a non-zero status.
RUN set -e

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
    apt-transport-https

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /usr/src/app

COPY ./ ./

EXPOSE 8000
