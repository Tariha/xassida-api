FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
